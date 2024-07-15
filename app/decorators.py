from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def email_confirmed_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            flash('Please confirm your email address to access this page.', 'warning')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function