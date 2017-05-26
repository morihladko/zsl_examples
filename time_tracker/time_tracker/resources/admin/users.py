from time_tracker.models.persistent import User
from time_tracker.resources.admin_resource import AdminResource


class UsersResource(AdminResource):
    __model__ = User
