import unittest
import os
from kanbanflow_cli.kanban_board import KanbanBoard
import setup_tests


class TestKanbanBoardAPICalls(unittest.TestCase):
    def setUp(self):
        setup_tests.set_kbflow_api_environ_var(config_ini_path="config.ini")
        self.board = KanbanBoard()

    def test_board_json_is_dict(self):
        self.assertIsInstance(self.board.board_json, dict)

    def test_board_users_json_is_list(self):
        self.assertIsInstance(self.board.board_users_json, list)

    def test_board_users_json_more_than_zero(self):
        self.assertGreater(len(self.board.board_users_json), 0)

    def test_board_column_ids_is_list(self):
        column_ids = self.board.get_board_columns_ids()
        self.assertIsInstance(column_ids, list)

    def tearDown(self):
        del os.environ["KBFLOW_API"]


if __name__ == "__main__":
    unittest.main()
