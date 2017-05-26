from zsl import inject
from zsl.resource.guard import ResourcePolicy, Access

from time_tracker.services.auth_service import AuthService, AuthError


class MustBeAdminPolicy(ResourcePolicy):
    @inject(auth_service=AuthService)
    def __init__(self, auth_service: AuthService):
        self._auth_srv: AuthService = auth_service

    @property
    def default(self):
        try:
            if self._auth_srv.is_admin():
                return Access.ALLOW
        except AuthError:
            pass

        return Access.CONTINUE
