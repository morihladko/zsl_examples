from .task_test_case import TaskTestCase

import json
from http import HTTPStatus
from flask import Response

from time_tracker.models.persistent import TimeEntry
from zsl.application.modules.alchemy_module import SessionHolder


class TestTimerTask(TaskTestCase):
    PATH = '/task/timer_task'

    def setUp(self):
        super().setUp()

        self.orm = self.app.injector.get(SessionHolder)()

    def testPerform(self):
        time_entry = {
            'user_id': 1,
            'start_time': '2017-05-01 13:00:20',
            'end_time': '2017-05-01 17:32:23',
            'what': 'fixing bug'
        }

        count_before = self.orm.query(TimeEntry).count()

        response: Response = self.client.post(self.PATH,
                                              data=json.dumps(time_entry),
                                              content_type="application/json")
        data = json.loads(response.data)

        count_after = self.orm.query(TimeEntry).count()

        self.assertEqual(HTTPStatus.OK.value, response.status_code,
                         "should return status 200")
        self.assertEqual(count_before + 1, count_after,
                         "should insert the time entry")
        self.assertIn('id', data,
                      "should return newly created object with an id ")

