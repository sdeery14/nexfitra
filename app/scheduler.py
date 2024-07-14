from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timezone, timedelta
from app.models import User
from flask import url_for
from app.routes import send_confirmation_email
from app import app
import logging

logger = logging.getLogger(__name__)

def send_email_verification_reminders():
    with app.app_context():
        users = User.query.filter_by(confirmed=False).all()
        for user in users:
            time_since_registration = datetime.now(timezone.utc) - user.date_registered
            if timedelta(days=1) < time_since_registration < timedelta(days=7):
                # Generate the URL within the app context
                token = user.get_reset_token()
                confirm_url = url_for('confirm_email', token=token, _external=True)
                send_confirmation_email(user, confirm_url)
                logger.info(f"Sent email verification reminder to {user.email}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Change the interval to minutes for testing
    scheduler.add_job(func=send_email_verification_reminders, trigger="interval", days=1)
    scheduler.start()
