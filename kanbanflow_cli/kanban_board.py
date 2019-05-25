import requests
import json
import kanbanflow_cli.api as api


class KanbanBoard:
    def __init__(self):
        self.api_url = api.base_url + 'board'
        self.users_api_url = api.base_url + 'users'
        self.board_json = self.get_board_json()
        self.board_users_json = self.get_board_users()
        self.board_name = self.get_board_name()

    def get_board_json(self) -> dict:
        """
        Initial API call to get board name and properties, depending
        on the api_key stored in the header
        """
        return api.get_with_api_headers(self.api_url)

    def get_board_name(self) -> str:
        return self.board_json['name']

    def get_board_columns_names(self) -> list:
        return [col['name'] for col in self.board_json['columns']]

    def get_board_columns_ids(self) -> list:
        return self.board_json['columns']

    def get_board_users(self) -> list:
        return api.get_with_api_headers(self.users_api_url)

    def get_board_colors(self):
        pass


if __name__ == "__main__":
    pass
