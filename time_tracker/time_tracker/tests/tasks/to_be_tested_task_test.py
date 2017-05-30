import http
import json
from unittest import TestCase

from zsl.application.containers.web_container import WebContainer
from zsl.unittest.http import HTTPTestCase
from zsl.unittest.zsl import ZslTestCase, ZslTestConfiguration


class ToBeTestedTaskTestCase(ZslTestCase, HTTPTestCase, TestCase):
    ZSL_TEST_CONFIGURATION = ZslTestConfiguration(app_name='time_tracker', container=WebContainer, version=None,
                                                  profile=None)

    def test_task_XY(self):
        with self.getHTTPClient() as client:
            DATA = {
                'test-data': 'the to be tested task just returns a copy'
            }

            rv = self.requestTask(client, '/task/to_be_tested_task', DATA)
            self.assertHTTPStatus(http.client.OK, rv.status_code, "OK status is expected.")
            self.assertJSONData(rv, DATA, "Correct data copy must be returned.")
