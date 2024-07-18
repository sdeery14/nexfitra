import unittest
from app import create_app, db, bcrypt
from app.models import User
from flask import url_for
from flask_testing import TestCase
from flask_login import current_user
from datetime import datetime, timedelta

class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        db.create_all()
        hashed_password = bcrypt.generate_password_hash('Password1!').decode('utf-8')
        user = User(username='testuser', email='test@example.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestUserRegistration(BaseTestCase):
    def test_registration_page(self):
        response = self.client.get(url_for('routes.register'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('register.html')

    def test_successful_registration(self):
        response = self.client.post(url_for('routes.register'), data=dict(
            username='newuser',
            email='new@example.com',
            password='Password123!',
            confirm_password='Password123!',
            accept_tos=True
        ), follow_redirects=True)
        self.assertIn(b'An email has been sent with instructions to confirm your email address.', response.data)
        user = User.query.filter_by(email='new@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'newuser')

    def test_registration_with_existing_username(self):
        response = self.client.post(url_for('routes.register'), data=dict(
            username='testuser',
            email='newuser@example.com',
            password='Password123!',
            confirm_password='Password123!',
            accept_tos=True
        ), follow_redirects=True)
        self.assertIn(b'Username - That username is taken. Please choose a different one.', response.data)

    def test_registration_with_existing_email(self):
        response = self.client.post(url_for('routes.register'), data=dict(
            username='newuser',
            email='test@example.com',
            password='Password123!',
            confirm_password='Password123!',
            accept_tos=True
        ), follow_redirects=True)
        self.assertIn(b'That email is taken. Please choose a different one.', response.data)

    def test_registration_with_missing_fields(self):
        response = self.client.post(url_for('routes.register'), data=dict(
            username='newuser',
            email='new@example.com',
            password='',
            confirm_password='Password123!',
            accept_tos=True
        ), follow_redirects=True)
        self.assertIn(b'This field is required.', response.data)

    def test_registration_with_invalid_email(self):
        response = self.client.post(url_for('routes.register'), data=dict(
            username='newuser',
            email='invalid-email',
            password='Password123!',
            confirm_password='Password123!',
            accept_tos=True
        ), follow_redirects=True)
        self.assertIn(b'Invalid email address.', response.data)

    def test_registration_with_password_mismatch(self):
        response = self.client.post(url_for('routes.register'), data=dict(
            username='newuser',
            email='new@example.com',
            password='Password123!',
            confirm_password='DifferentPassword!',
            accept_tos=True
        ), follow_redirects=True)
        self.assertIn(b'Field must be equal to password.', response.data)

    def test_registration_with_weak_password(self):
        response = self.client.post(url_for('routes.register'), data=dict(
            username='newuser',
            email='new@example.com',
            password='weak',
            confirm_password='weak',
            accept_tos=True
        ), follow_redirects=True)
        self.assertIn(b'Password must be at least 8 characters long.', response.data)
        self.assertIn(b'Password must contain at least one number.', response.data)
        self.assertIn(b'Password must contain at least one uppercase letter.', response.data)
        self.assertIn(b'Password must contain at least one special character.', response.data)

class TestUserLogin(BaseTestCase):
    def test_login_page(self):
        response = self.client.get(url_for('routes.login'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('login.html')

    def test_successful_login(self):
        response = self.client.post(url_for('routes.login'), data=dict(
            email='test@example.com',
            password='Password1!',
            remember=False
        ), follow_redirects=True)
        self.assertIn(b'You have been logged in!', response.data)
        self.assertTrue(current_user.is_authenticated)

    def test_login_with_incorrect_password(self):
        response = self.client.post(url_for('routes.login'), data=dict(
            email='test@example.com',
            password='wrongpassword',
            remember=False
        ), follow_redirects=True)
        self.assertIn(b'Login Unsuccessful. Please check email and password', response.data)
        self.assertFalse(current_user.is_authenticated)

    def test_login_with_non_existent_email(self):
        response = self.client.post(url_for('routes.login'), data=dict(
            email='nonexistent@example.com',
            password='Password1!',
            remember=False
        ), follow_redirects=True)
        self.assertIn(b'Login Unsuccessful. Please check email and password', response.data)
        self.assertFalse(current_user.is_authenticated)

    def test_login_with_locked_account(self):
        user = User.query.filter_by(email='test@example.com').first()
        user.account_locked_until = datetime.now() + timedelta(minutes=15)
        db.session.commit()
        response = self.client.post(url_for('routes.login'), data=dict(
            email='test@example.com',
            password='Password1!',
            remember=False
        ), follow_redirects=True)
        self.assertIn(b'Account is locked. Try again later.', response.data)
        self.assertFalse(current_user.is_authenticated)

if __name__ == '__main__':
    unittest.main()
