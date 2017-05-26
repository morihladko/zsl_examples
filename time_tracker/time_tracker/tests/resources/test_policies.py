from unittest import TestCase, mock

from zsl.application.modules.alchemy_module import SessionHolder
from zsl.resource.guard import Access

from time_tracker.models.persistent import User
from time_tracker.services.auth_service import AuthService
from time_tracker.resources.policies import MustBeAdminPolicy


class TestMustBeAdminPolicy(TestCase):

    def setUp(self):
        from time_tracker.time_tracker import app

        self.orm = app.injector.get(SessionHolder)()
        self.auth_service: AuthService = app.injector.get(AuthService)

    def _getAdminToken(self) -> str:
        user = self.orm.query(User).filter(User.id == 1).one()
        return self.auth_service.create_token(user.get_app_model()).decode(
            'utf-8')

    def _getNotAdminToken(self) -> str:
        user = self.orm.query(User).filter(User.id != 1).first()
        return self.auth_service.create_token(user.get_app_model()).decode(
            'utf-8')

    def testAllowAdmin(self):
        token = 'Bearer ' + self._getAdminToken()

        with mock.patch('time_tracker.services.auth_service.'
                        'get_request_auth_token',
                        mock.Mock(return_value=token)):
            policy = MustBeAdminPolicy()

            self.assertEqual(Access.ALLOW, policy.default,
                             "should return ALLOW for admin")

    def testDenyOtherUsers(self):
        token = 'Bearer ' + self._getNotAdminToken()

        with mock.patch('time_tracker.services.auth_service.'
                        'get_request_auth_token',
                        mock.Mock(return_value=token)):
            policy = MustBeAdminPolicy()

            self.assertNotEqual(Access.ALLOW, policy.default,
                                "should return ALLOW for admin")
