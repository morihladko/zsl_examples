from zsl.router.task import TaskConfiguration

TASKS = TaskConfiguration()\
        .create_namespace('task')\
            .add_packages(['time_tracker.tasks'])\
            .get_configuration()\
        .create_namespace('task/zsl')\
            .add_packages(['zsl.tasks.zsl'])\
            .get_configuration()
RESOURCE_PACKAGES = ('time_tracker.resources.admin',)

SERVICE_INJECTION = {
    'list': ['AuthService'],
    'package': 'time_tracker.services'
}

DATABASE_URI = 'sqlite:///:memory:'
DATABASE_ENGINE_PROPS = {'echo': True}
REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}
RELOAD = False
DEBUG = False
USE_DEBUGGER = False

LOG_HANDLERS = {
    'default-handler': {
        'type': 'rotating-file',
        'parameters': {
            'filename': './time_tracker.log'
        }
    },
    'console': {
        'class': 'logging.StreamHandler'
    }
}

LOG = {
    'zsl': {
        'handlers': ['default-handler'],
        'level': 'ERROR'
    }
}

CORS = {
    'origin': '*'
}

SECRET = 'f228301eff5840e7b13dee95711b06c6'
