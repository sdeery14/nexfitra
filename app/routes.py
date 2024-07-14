# app/routes.py
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt, mail
from app.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
import logging

logger = logging.getLogger(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
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
            return redirect(url_for('login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form, field).label.text} - {error}", 'danger')
    return render_template('register.html', title='Register', form=form)


def send_confirmation_email(user):
    token = user.get_reset_token()
    msg = Message('Confirm Your Email',
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f'''To confirm your email, visit the following link:
{url_for('confirm_email', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
    logger.info(f"Sent confirmation email to {user.email} with token: {token}")  # Logging statement

@app.route("/confirm_email/<token>")
def confirm_email(token):
    logger.info(f"Received token: {token}")  # Logging statement
    user = User.verify_reset_token(token)
    if user is None:
        logger.warning('Invalid or expired token')
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('register'))
    
    logger.info(f"User found: {user.username}")
    
    user.confirmed = True
    try:
        db.session.commit()
        logger.info("Database updated successfully")
    except Exception as e:
        logger.error(f"Error updating database: {e}")
        db.session.rollback()
        flash('There was an issue confirming your email. Please try again.', 'danger')
        return redirect(url_for('register'))
    
    flash('Your email has been confirmed!', 'success')
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form, token=token)




@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
