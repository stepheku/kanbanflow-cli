import unittest
from kanbanflow_cli.api import KanbanFlowAPICalls
from kanbanflow_cli.kanban_task_list import KanbanTaskList
import configparser
from pathlib import Path
import os
import setup_tests

class TestAPICalls(unittest.TestCase):
    def setUp(self):
        self.api_caller = KanbanFlowAPICalls()
        setup_tests.set_kbflow_api_environ_var("config.ini")
        self.all_tasks = self.api_caller.get_all_tasks()
        self.sample_task_id = self.all_tasks[0].get("tasks")[0].get("_id")
        self.sample_column_id = self.all_tasks[0].get("columnId")
        self.sample_column_name = self.all_tasks[0].get("columnName")

    def test_get_board(self):
        """
        get_board() method returns a valid dict
        """
        board_json = self.api_caller.get_board()
        self.assertIsInstance(board_json, dict)

    def test_get_task_by_id(self):
        """
        sample task_id returns a dict with the task_id
        """
        task_json = self.api_caller.get_task_by_id(task_id=self.sample_task_id)
        self.assertEqual(task_json.get("_id"), self.sample_task_id)

    def test_get_tasks_by_column_id(self):
        """
        sample column_id returns a list of tasks
        """
        task_list = self.api_caller.get_tasks_by_column_id(
            column_id=self.sample_column_id)
        self.assertIsInstance(task_list, list)

    def test_get_tasks_by_column_name(self):
        """
        sample column_name returns a list of tasks
        """
        task_list = self.api_caller.get_tasks_by_column_name(
            column_name=self.sample_column_name)
        self.assertIsInstance(task_list, list)

    def tearDown(self):
        del os.environ["KBFLOW_API"]


if __name__ == "__main__":
    unittest.main()
