import jwt
from typing import Optional

from zsl import inject, Config
from zsl.service import Service, transactional

from sqlalchemy.orm.exc import NoResultFound

from flask import request

from time_tracker.models.persistent import User as DbUser
from time_tracker.models.serializable import User


class AuthError(Exception):
    pass


def get_request_auth_token() -> Optional[str]:
    return request.headers.get('Authorization', None)


class AuthService(Service):
    JWT_ALGORITHM = 'HS256'

    @inject(config=Config)
    def __init__(self, config: Config):
        super().__init__()

        self._config: Config = config

    def _get_request_auth_token(self) -> Optional[str]:
        return get_request_auth_token()

    @transactional
    def authenticate(self, username: str, password: str) -> User:
        if password != 'password':
            raise AuthError('Wrong password')

        try:
            db_user = self._orm.query(DbUser).filter(
                DbUser.username == username
            ).one()
        except NoResultFound:
            raise AuthError('Wrong username')

        return db_user.get_app_model()

    def create_token(self, user: User) -> str:
        return jwt.encode(user.get_attributes(), self._config['SECRET'],
                          algorithm=self.JWT_ALGORITHM)

    def get_current_user(self) -> User:
        token: str = self._get_request_auth_token()

        if not token or not token.startswith('Bearer '):
            raise AuthError('User is not logged')

        token = token[7:]

        user = jwt.decode(token, self._config['SECRET'],
                          algorithm=self.JWT_ALGORITHM)

        return User(user)

    def is_admin(self) -> bool:
        return self.get_current_user().get_id() == 1
