from datetime import datetime

from zsl.db.model.app_model import ISO_8601_FORMAT

from time_tracker.resources.admin_resource import AdminResource
from time_tracker.models.persistent import TimeEntry

def parse_date(date_str: str, fmt: str ='%Y-%m-%dT%H:%M:%S') -> datetime:
    if date_str.endswith('Z'):
        date_str = date_str[:-5]

    return datetime.strptime(date_str, fmt)


class TimeEntriesResource(AdminResource):
    __model__ = TimeEntry

    @staticmethod
    def _parse_data(data: dict):
        data = data.copy()

        if 'start_time' in data:
            data['start_time'] = parse_date(data['start_time'])

        if 'end_time' in data:
            data['end_time'] = parse_date(data['end_time'])

        return data

    def create(self, params, args, data):
        super().create(params, args, self._parse_data(data))

    def update(self, params, args, data):
        super().update(params, args, self._parse_data(data))
