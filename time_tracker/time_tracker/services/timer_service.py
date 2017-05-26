from zsl.service import Service, transactional

from time_tracker.models.persistent import TimeEntry as DbTimeEntry
from time_tracker.models.serializable import TimeEntry
from datetime import datetime


class TimerService(Service):
    @transactional
    def log_time(self, user_id: int, start_time: datetime, end_time: datetime,
                 what: str) -> TimeEntry:

        te = DbTimeEntry()
        te.start_time = start_time
        te.end_time = end_time
        te.what = what
        te.user_id = user_id

        self._orm.add(te)
        self._orm.flush()

        self._orm.refresh(te)

        return te.get_app_model()
