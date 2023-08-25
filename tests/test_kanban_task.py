import unittest
import os
from kanbanflow_cli.kanban_board import KanbanBoard
from kanbanflow_cli.kanban_task_list import KanbanTaskList
import setup_tests


class TestKanbanTaskAPICalls(unittest.TestCase):
    def setUp(self):
        setup_tests.set_kbflow_api_environ_var(config_ini_path="config.ini")
        self.board = KanbanBoard()
        self.first_column_name = self.board.column_dict_list[0].get("name")
        self.first_column_id = self.board.column_dict_list[0].get("uniqueId")
        self.first_column_task_list_by_id = KanbanTaskList(
            column_id=self.first_column_id
        )
        self.first_column_task_list_by_name = KanbanTaskList(
            column_name=self.first_column_name
        )

        self.limit = 1
        self.first_column_task_list_by_id_limit = KanbanTaskList(
            column_id=self.first_column_id, limit=self.limit
        )
        self.first_column_task_list_by_name_limit = KanbanTaskList(
            column_name=self.first_column_name, limit=self.limit
        )

        self.all_tasks = KanbanTaskList()

    def test_get_all_tasks_is_list(self):
        self.assertIsInstance(self.all_tasks.task_list, list)

    def test_all_tasks_number_of_columns_equal_to_board_number_of_columns(self):
        """
        Number of columns in the KanbanBoard object matches the number of
        columns returned when getting all tasks with the KanbanTaskList
        """
        board_number_of_columns = len(self.board.column_dict_list)
        all_task_number_of_columns = len(self.all_tasks.task_list)
        self.assertEqual = (board_number_of_columns, all_task_number_of_columns)

    def test_column_name_column_id_args_create_attribute_error(self):
        """
        Having both a column_name and column_id argument in the KanbanTaskList
        object results in an attribute error because of ambiguous parameters
        """
        self.assertRaises(AttributeError, KanbanTaskList, "test", "test")

    def test_get_tasks_by_column_id_returns_list(self):
        self.assertIsInstance(self.first_column_task_list_by_id.task_list, list)

    def test_get_tasks_by_column_name_returns_list(self):
        self.assertIsInstance(self.first_column_task_list_by_name.task_list, list)

    def test_get_tasks_by_column_id_or_name_return_same_list_len(self):
        len_by_id = len(self.first_column_task_list_by_id.task_list)
        len_by_name = len(self.first_column_task_list_by_name.task_list)
        self.assertEquals(len_by_id, len_by_name)

    def test_get_tasks_by_column_id_or_name_limit_return_same_list_len(self):
        len_by_id = len(self.first_column_task_list_by_id_limit.task_list)
        len_by_name = len(self.first_column_task_list_by_name_limit.task_list)
        print(len_by_id)
        self.assertEquals(len_by_id, len_by_name)

    def tearDown(self):
        del os.environ["KBFLOW_API"]


if __name__ == "__main__":
    unittest.main()
