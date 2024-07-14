# app/models.py
from itsdangerous import URLSafeTimedSerializer as Serializer
from app import db, app
from flask_login import UserMixin
import logging
from datetime import datetime, timezone, timedelta

logger = logging.getLogger(__name__)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    confirmed = db.Column(db.Boolean, default=False)
    date_registered = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        token = s.dumps({'user_id': self.id})
        logger.info(f"Generated token: {token}")  # Logging statement
        return token

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=expires_sec)['user_id']
            logger.info(f"Verified user_id from token: {user_id}")  # Logging statement
        except Exception as e:
            logger.error(f"Token verification failed: {e}")
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
