import unittest
from kanbanflow_cli.kanban_board import KanbanBoard


class TestKanbanBoardAPICalls(unittest.TestCase):
    board = KanbanBoard()

    def test_board_api_url(self, board_obj=board):
        self.assertEqual(
            'https://kanbanflow.com/api/v1/board', board_obj.api_url)

    def test_board_users_api_url(self, board_obj=board):
        self.assertEqual('https://kanbanflow.com/api/v1/users',
                         board_obj.users_api_url)

    def test_board_json_is_dict(self, board_obj=board):
        self.assertIsInstance(board_obj.board_json, dict)

    def test_board_users_json_is_list(self, board_obj=board):
        self.assertIsInstance(board_obj.board_users_json, list)

    def test_board_users_json_more_than_zero(self, board_obj=board):
        self.assertGreater(len(board_obj.board_users_json), 0)


if __name__ == "__main__":
    unittest.main()
