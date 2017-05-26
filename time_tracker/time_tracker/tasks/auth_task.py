from typing import Dict, Any

from zsl import inject
from zsl.task.task_data import TaskData
from zsl.task.task_decorator import json_output, json_input, required_data

from time_tracker.services.auth_service import AuthService


class AuthTask:
    @inject(auth_service=AuthService)
    def __init__(self, auth_service: AuthService):
        self._auth_srv: AuthService = auth_service

    @json_input
    @json_output
    @required_data('username', 'password')
    def perform(self, data: TaskData) -> Dict[str, Any]:
        data = data.get_data()

        user = self._auth_srv.authenticate(
            username=data['username'],
            password=data['password']
        )

        token = self._auth_srv.create_token(user)

        return {
            "token": token.decode('utf-8')
        }
