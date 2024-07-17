# app/routes.py
from flask import Blueprint, render_template, url_for, flash, redirect, request, session, current_app
from app import db, bcrypt, mail
from app.forms import (RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm, MFAForm, 
                       UpdateUsernameForm, UpdateEmailForm, UpdatePasswordForm)
from app.models import User, LoginActivity
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer as Serializer
import logging
from datetime import datetime, timezone, timedelta
import pyotp
from app.decorators import email_confirmed_required

bp = Blueprint('routes', __name__)
logger = logging.getLogger(__name__)

@bp.route("/")
@bp.route("/home")
def home():
    return render_template('home.html')

@bp.route("/terms_of_service")
def terms_of_service():
    return render_template('terms_of_service.html')

@bp.route("/privacy_policy")
def privacy_policy():
    return render_template('privacy_policy.html')

@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter((User.email == form.email.data) | (User.username == form.username.data)).first()
        if existing_user:
            if existing_user.email == form.email.data:
                flash('Email is already in use. Please choose a different one.', 'danger')
            if existing_user.username == form.username.data:
                flash('Username is already in use. Please choose a different one.', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            send_confirmation_email(user)
            flash('An email has been sent with instructions to confirm your email address.', 'info')
            return redirect(url_for('routes.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form, field).label.text} - {error}", 'danger')
    return render_template('register.html', title='Register', form=form)

def send_confirmation_email(user, confirm_url=None):
    if confirm_url is None:
        token = user.get_reset_token()
        confirm_url = url_for('routes.confirm_email', token=token, _external=True)
    msg = Message('Confirm Your Email',
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f'''To confirm your email, visit the following link:
{confirm_url}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
    logger.info(f"Sent confirmation email to {user.email} with URL: {confirm_url}")

@bp.route("/confirm_email/<token>")
def confirm_email(token):
    logger.info(f"Received token: {token}")  # Logging statement
    user = User.verify_reset_token(token)
    if user is None:
        logger.warning('Invalid or expired token')
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('routes.register'))
    
    logger.info(f"User found: {user.username}")
    
    user.confirmed = True
    try:
        db.session.commit()
        logger.info("Database updated successfully")
    except Exception as e:
        logger.error(f"Error updating database: {e}")
        db.session.rollback()
        flash('There was an issue confirming your email. Please try again.', 'danger')
        return redirect(url_for('routes.register'))
    
    flash('Your email has been confirmed!', 'success')
    return redirect(url_for('routes.login'))

@bp.route("/resend_confirmation")
@login_required
def resend_confirmation():
    send_confirmation_email(current_user)
    flash('A new confirmation email has been sent.', 'info')
    return redirect(url_for('routes.account'))

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.account_locked_until and user.account_locked_until > datetime.now(timezone.utc):
                flash('Account is locked. Try again later.', 'danger')
                return redirect(url_for('routes.login'))
            
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.failed_login_attempts = 0
                db.session.commit()
                login_user(user, remember=form.remember.data)
                # Log login activity
                login_activity = LoginActivity(user_id=user.id, ip_address=request.remote_addr, user_agent=request.headers.get('User-Agent'))
                db.session.add(login_activity)
                db.session.commit()
                if not user.mfa_enabled and not user.mfa_skipped:
                    return redirect(url_for('routes.setup_mfa'))
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('routes.home'))
            else:
                if user.failed_login_attempts is None:
                    user.failed_login_attempts = 0
                user.failed_login_attempts += 1
                if user.failed_login_attempts >= 5:
                    user.lock_account()
                    flash('Account locked due to too many failed login attempts.', 'danger')
                else:
                    flash('Login Unsuccessful. Please check email and password', 'danger')
                db.session.commit()
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@bp.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('routes.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@bp.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('routes.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('routes.login'))
    return render_template('reset_token.html', title='Reset Password', form=form, token=token)

@bp.route("/verify_mfa", methods=['GET', 'POST'])
@login_required
def verify_mfa():
    form = MFAForm()
    if form.validate_on_submit():
        if current_user.verify_totp(form.token.data):
            current_user.mfa_enabled = True
            db.session.commit()
            flash('MFA setup complete!', 'success')
            return redirect(url_for('routes.home'))
        else:
            flash('Invalid MFA token', 'danger')
    return render_template('verify_mfa.html', form=form)

@bp.route("/mfa", methods=['GET', 'POST'])
@login_required
def mfa():
    form = MFAForm()
    if form.validate_on_submit():
        if current_user.verify_totp(form.token.data):
            current_user.mfa_verified = True
            db.session.commit()
            return redirect(url_for('routes.home'))
        else:
            flash('Invalid MFA token', 'danger')
    return render_template('mfa.html', form=form)

@bp.route("/logout")
def logout():
    logout_user()
    session.pop('remember', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('routes.login'))

@bp.route("/account", methods=['GET'])
@login_required
def account():
    form_username = UpdateUsernameForm()
    form_email = UpdateEmailForm()
    form_password = UpdatePasswordForm()
    return render_template('account.html', 
                           form_username=form_username, 
                           form_email=form_email, 
                           form_password=form_password)

@bp.route("/update_username", methods=['POST'])
@login_required
def update_username():
    form = UpdateUsernameForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('Your username has been updated!', 'success')
    return redirect(url_for('routes.account'))

@bp.route("/update_email", methods=['POST'])
@login_required
def update_email():
    form = UpdateEmailForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.confirmed = False
        db.session.commit()
        send_confirmation_email(current_user)
        flash('Your email has been updated! Please confirm your new email address.', 'success')
    return redirect(url_for('routes.account'))

@bp.route("/update_password", methods=['POST'])
@login_required
def update_password():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        current_user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated!', 'success')
    return redirect(url_for('routes.account'))

@bp.route("/enable_mfa", methods=['POST'])
@login_required
def enable_mfa():
    current_user.mfa_skipped = False
    db.session.commit()
    return redirect(url_for('routes.setup_mfa'))

@bp.route("/setup_mfa", methods=['GET', 'POST'])
@login_required
def setup_mfa():
    if request.method == 'POST':
        if 'skip' in request.form:
            current_user.mfa_skipped = True
            db.session.commit()
            flash('MFA setup skipped. You can enable it later from the account settings.', 'info')
            return redirect(url_for('routes.home'))
        elif 'do_not_show_again' in request.form:
            current_user.mfa_skipped = True
            db.session.commit()
            flash('MFA setup skipped. You can enable it later from the account settings.', 'info')
            return redirect(url_for('routes.home'))
        elif 'setup' in request.form:
            return redirect(url_for('routes.verify_mfa'))

    if not current_user.mfa_enabled:
        current_user.mfa_secret = pyotp.random_base32()
        db.session.commit()
        flash('MFA setup initialized. Scan the QR code with your authenticator app.', 'info')
    return render_template('setup_mfa.html', user=current_user)

@bp.route("/confirm_email_change/<token>")
@login_required
def confirm_email_change(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        user = User.query.get(data['user_id'])
        if user and user == current_user:
            user.email = data['new_email']
            user.email_change_pending = None
            db.session.commit()
            flash('Your email address has been updated.', 'success')
        else:
            flash('Invalid or expired token.', 'danger')
    except Exception as e:
        flash('Invalid or expired token.', 'danger')
    return redirect(url_for('routes.account'))

@bp.route("/login_activity")
@login_required
@email_confirmed_required
def login_activity():
    activities = current_user.login_activities
    return render_template('login_activity.html', activities=activities)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('routes.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
