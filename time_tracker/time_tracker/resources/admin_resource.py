from zsl.resource.json_server_resource import JsonServerResource
from zsl.resource.guard import guard, GuardedMixin

from .policies import MustBeAdminPolicy


@guard([MustBeAdminPolicy()])
class AdminResource(JsonServerResource, GuardedMixin):
    pass
