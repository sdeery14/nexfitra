# app/models.py
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from app import db, bcrypt
from flask_login import UserMixin
import logging
from datetime import datetime, timezone, timedelta
import pyotp  # For multi-factor authentication

logger = logging.getLogger(__name__)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    confirmed = db.Column(db.Boolean, default=False)
    email_change_pending = db.Column(db.String(120), nullable=True)
    date_registered = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    failed_login_attempts = db.Column(db.Integer, default=0, nullable=False)
    account_locked_until = db.Column(db.DateTime(timezone=True), nullable=True)
    mfa_secret = db.Column(db.String(32), default=lambda: pyotp.random_base32())
    mfa_enabled = db.Column(db.Boolean, default=False)
    mfa_skipped = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    login_activities = db.relationship('LoginActivity', backref='user', lazy=True)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        token = s.dumps({'user_id': self.id})
        logger.info(f"Generated token: {token}")  # Logging statement
        return token

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=expires_sec)['user_id']
            logger.info(f"Verified user_id from token: {user_id}")  # Logging statement
        except Exception as e:
            logger.error(f"Token verification failed: {e}")
            return None
        return User.query.get(user_id)
    
    def lock_account(self):
        self.account_locked_until = datetime.now(timezone.utc) + timedelta(minutes=15)  # Lock for 15 minutes
        self.failed_login_attempts = 0
        db.session.commit()

    def get_totp_uri(self):
        return f'otpauth://totp/NexFitra:{self.email}?secret={self.mfa_secret}&issuer=NexFitra'

    def verify_totp(self, token):
        totp = pyotp.TOTP(self.mfa_secret)
        return totp.verify(token)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class LoginActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    ip_address = db.Column(db.String(45))  # Supports IPv4 and IPv6
    user_agent = db.Column(db.String(200))
