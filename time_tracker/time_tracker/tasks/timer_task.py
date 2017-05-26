from datetime import datetime

from zsl import inject
from zsl.task.task_data import TaskData
from zsl.task.task_decorator import json_output, json_input, required_data

from time_tracker.models.serializable import TimeEntry, DATE_FORMAT
from time_tracker.services.timer_service import TimerService


class TimerTask:
    @inject(timer_service=TimerService)
    def __init__(self, timer_service: TimerService):
        self._timer_srv: TimerService = timer_service

    @json_input
    @json_output
    @required_data('user_id', 'start_time', 'end_time', 'what')
    def perform(self, data: TaskData) -> TimeEntry:
        data = data.get_data()

        user_id = data['user_id']
        start_time = datetime.strptime(data['start_time'], DATE_FORMAT)
        end_time = datetime.strptime(data['start_time'], DATE_FORMAT)
        what = data['what']

        return self._timer_srv.log_time(
            user_id=user_id,
            start_time=start_time,
            end_time=end_time,
            what=what
        )
