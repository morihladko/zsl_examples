from .task_test_case import TaskTestCase

import json
import jwt
from http import HTTPStatus

from flask import Response

from time_tracker.services.auth_service import AuthService


class TestAuthTask(TaskTestCase):
    PATH = '/task/auth_task'

    def test_auth_request(self):
        username = 'admin'

        req_data = {
            'username': username,
            'password': 'password'
        }
        response: Response = self.client.post(self.PATH,
                                              data=json.dumps(req_data),
                                              content_type="application/json")
        data = json.loads(response.data)

        self.assertEqual(HTTPStatus.OK.value, response.status_code,
                         "Should return status 200")
        self.assertIn('token', data, "Should return token")

        user = jwt.decode(data['token'], self.app.config['SECRET'],
                          algorithms=AuthService.JWT_ALGORITHM)

        self.assertEqual(username, user['username'],
                         "Should return token with user details")
