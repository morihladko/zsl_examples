import json
from pathlib import Path
from datetime import datetime

from sqlalchemy.engine import Engine
from typing import List

from zsl import inject
from zsl.application.modules.alchemy_module import SessionHolder

from time_tracker.models.persistent import Base, TimeEntry, User
from time_tracker.models.serializable import DATE_FORMAT


CURRENT_DIR = Path(__file__).parent
USER_JSON = 'users.json'
TIME_ENTRY_JSON = 'time_entries.json'


def get_users() -> List[User]:
    with open(CURRENT_DIR / USER_JSON) as user_file:
        users = json.load(user_file)

    user_list = []
    for user in users:
        user_list.append(User(**user))

    return user_list


def get_time_entries() -> List[TimeEntry]:
    with open(CURRENT_DIR / TIME_ENTRY_JSON) as te_file:
        entries = json.load(te_file)

    te_list = []
    for te in entries:
        te['start_time'] = datetime.strptime(te['start_time'], DATE_FORMAT)
        te['end_time'] = datetime.strptime(te['end_time'], DATE_FORMAT)

        te_list.append(TimeEntry(**te))

    return te_list


@inject(engine=Engine)
def create_schema(engine: Engine):
    Base.metadata.create_all(engine)


@inject(session=SessionHolder)
def install(session: SessionHolder):
    create_schema()

    session = session()

    session.add_all(get_users())
    session.add_all(get_time_entries())

    session.commit()


