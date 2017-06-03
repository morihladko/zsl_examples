from unittest import TestCase

from zsl import Zsl
from zsl.application.containers.web_container import WebContainer

from flask.testing import FlaskClient

from db.install import install


class TaskTestCase(TestCase):
    def setUp(self):
        app = Zsl(__name__, modules=WebContainer.modules())
        install()
        app.testing = True

        self.app = app
        self.client: FlaskClient = app.test_client()
