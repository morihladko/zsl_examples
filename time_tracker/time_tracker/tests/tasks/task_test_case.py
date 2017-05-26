from unittest import TestCase

from flask.testing import FlaskClient


class TaskTestCase(TestCase):
    def setUp(self):
        from time_tracker.time_tracker import app
        app.testing = True

        self.app = app
        self.client: FlaskClient = app.test_client()
