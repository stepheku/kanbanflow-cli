import unittest
from kanbanflow_cli.api import KanbanFlowAPICalls
from kanbanflow_cli.kanban_task_list import KanbanTaskList
from kanbanflow_cli.kanban_board import KanbanBoard
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
        self.sample_create_task_id = None

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
            column_id=self.sample_column_id
        )
        self.assertIsInstance(task_list, list)

    def test_get_tasks_by_column_name(self):
        """
        sample column_name returns a list of tasks
        """
        task_list = self.api_caller.get_tasks_by_column_name(
            column_name=self.sample_column_name
        )
        self.assertIsInstance(task_list, list)

    def tearDown(self):
        del os.environ["KBFLOW_API"]


class TestCreateDeleteTaskAPICalls(unittest.TestCase):
    def setUp(self):
        self.api_caller = KanbanFlowAPICalls()
        setup_tests.set_kbflow_api_environ_var("config.ini")
        self.board = KanbanBoard()
        self.sample_column_id = self.board.column_dict_list[0].get("uniqueId")

    def test_create_task_without_name_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.api_caller.create_task(name=None, columnId=self.sample_column_id)

    def test_create_task_without_column_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.api_caller.create_task(name="Test Task", columnId=None)

    def test_create_task_delete_task_(self):
        create_task_resp = self.api_caller.create_task(
            name="Test Task", columnId=self.sample_column_id
        )
        create_task_id = create_task_resp.get("taskId")

        self.assertIsInstance(create_task_resp, dict)

        delete_task_resp = self.api_caller.delete_task(task_id=create_task_id)

        self.assertEquals(delete_task_resp.status_code, 200)

    def tearDown(self):
        del os.environ["KBFLOW_API"]


class TestCreateDeleteSubtaskAPICalls(unittest.TestCase):
    def setUp(self):
        self.api_caller = KanbanFlowAPICalls()
        setup_tests.set_kbflow_api_environ_var("config.ini")
        self.board = KanbanBoard()
        self.sample_column_id = self.board.column_dict_list[0].get("uniqueId")

    def test_create_subtask_without_name_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.api_caller.create_subtask(task_id="testId", name=None)

    def test_create_subtask_without_task_id_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.api_caller.create_subtask(task_id=None, name="Test Subtask")

    def test_create_task_create_subtask_delete_task_by_index(self):
        create_task_resp = self.api_caller.create_task(
            name="Test Task", columnId=self.sample_column_id
        )
        create_task_id = create_task_resp.get("taskId")

        create_subtask_resp = self.api_caller.create_subtask(
            task_id=create_task_id, name="Test subtask"
        )
        create_subtask_index = create_subtask_resp.get("insertIndex")

        self.assertIsInstance(create_subtask_resp, dict)

        delete_subtask_by_index_resp = self.api_caller.delete_subtask(
            task_id=create_task_id, index=str(create_subtask_index)
        )

        self.assertEquals(delete_subtask_by_index_resp.status_code, 200)

        self.api_caller.delete_task(task_id=create_task_id)

    def test_create_task_create_subtask_delete_task_by_name(self):
        create_task_resp = self.api_caller.create_task(
            name="Test Task", columnId=self.sample_column_id
        )
        create_task_id = create_task_resp.get("taskId")

        create_subtask_resp = self.api_caller.create_subtask(
            task_id=create_task_id, name="Test subtask"
        )

        self.assertIsInstance(create_subtask_resp, dict)

        delete_subtask_by_index_resp = self.api_caller.delete_subtask(
            task_id=create_task_id, name="Test subtask"
        )

        self.assertEquals(delete_subtask_by_index_resp.status_code, 200)

        self.api_caller.delete_task(task_id=create_task_id)

    def tearDown(self):
        del os.environ["KBFLOW_API"]


if __name__ == "__main__":
    unittest.main()
