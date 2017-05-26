from zsl.db.model.app_model import AppModel, DATETIME_DATA

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class User(AppModel):
    pass


class TimeEntry(AppModel):
    def __init__(self, raw, id_name='id', hints=None):
        if not hints:
            hints = {}

        if DATETIME_DATA not in hints:
            hints[DATETIME_DATA] = DATE_FORMAT

        super().__init__(raw, id_name, hints)
