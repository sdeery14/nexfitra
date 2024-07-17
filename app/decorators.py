# app/decorators.py
from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def email_confirmed_required(f):
    """
    Decorator to ensure that the current user's email is confirmed.
    If the email is not confirmed, it flashes a warning message and redirects to the home page.
    
    :param f: The decorated function
    :return: The wrapped function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            flash('Please confirm your email address to access this page.', 'warning')
            return redirect(url_for('routes.home'))
        return f(*args, **kwargs)
    return decorated_function
