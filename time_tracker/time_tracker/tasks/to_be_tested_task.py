from typing import Dict, Any

from zsl.task.task_data import TaskData
from zsl.task.task_decorator import json_output, json_input


class ToBeTestedTask:
    @json_input
    @json_output
    def perform(self, data: TaskData) -> Dict[str, Any]:
        return data.get_data()
