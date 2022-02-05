from unittest import TestCase
from server import app
from model import connect_to_db, db
from flask import session



class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Set up a test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        #connect to database
        connect_to_db(app)

    def test_homepage(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn(b"Welcome", result.data)

    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                  data={"email": "test@email", "password": "123"},
                                  follow_redirects=True)
        self.assertIn(b"User Profile", result.data)


class FlaskTestsNotLogIn(TestCase):

    """Test that user can't see user profile page if not log in"""

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_userprofile(self):
        result = self.client.get("/user_profile", follow_redirects=True)
        self.assertIn(b"Please log in to see user profile.", result.data)


class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session"""

    def setUp(self):

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 9
                sess['password'] = '123'

    def test_page(self):

        result = self.client.get("/user_profile", follow_redirects=True)
        self.assertIn(b"User Profile", result.data)






    
    if __name__ == "__main__":
        import unittest

        unittest.main()
