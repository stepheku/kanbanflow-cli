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
        self.assertIsInstance(self.board.column_dict_list, list)

    def test_board_column_ids_list_more_than_one(self):
        """
        There is at least one column
        """
        self.assertGreater(len(self.board.column_dict_list), 0)

    def test_board_column_ids_first_element_is_dict(self):
        """
        First element in list of column is a dictionary
        """
        self.assertIsInstance(self.board.column_dict_list[0], dict)

    def test_board_colors_is_list(self):
        """
        Colors is returned as a list
        """
        colors = self.board.color_dict_list
        self.assertIsInstance(colors, list)

    def test_board_colors_list_more_than_one(self):
        """
        There is at least one task color
        """
        self.assertGreater(len(self.board.color_dict_list), 0)

    def test_board_colors_first_element_is_dict(self):
        """
        First element in list of colors is a dictionary
        """
        self.assertIsInstance(self.board.color_dict_list[0], dict)

    def tearDown(self):
        del os.environ["KBFLOW_API"]


if __name__ == "__main__":
    unittest.main()
