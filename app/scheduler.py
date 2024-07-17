# app/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timezone, timedelta
from app.models import User
from flask import url_for, current_app
from app.routes import send_confirmation_email
import logging

logger = logging.getLogger(__name__)

def send_email_verification_reminders():
    with current_app.app_context():
        users = User.query.filter_by(confirmed=False).all()
        for user in users:
            time_since_registration = datetime.now(timezone.utc) - user.date_registered
            if timedelta(days=1) < time_since_registration < timedelta(days=7):
                # Generate the URL within the app context
                token = user.get_reset_token()
                confirm_url = url_for('routes.confirm_email', token=token, _external=True)
                send_confirmation_email(user, confirm_url)
                logger.info(f"Sent email verification reminder to {user.email}")

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    # Change the interval to minutes for testing
    scheduler.add_job(func=send_email_verification_reminders, trigger="interval", days=1)
    scheduler.start()
    app.logger.info('Scheduler started')
