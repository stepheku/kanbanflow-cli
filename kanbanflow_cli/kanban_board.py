import requests
import json
import kanbanflow_cli.api as api



class KanbanBoard:
    def __init__(self):
        self.api_connector = api.KanbanFlowAPICalls()
        self.board_json = self.api_connector.get_board()
        self.board_users_json = self.api_connector.get_users()
        self.board_name = self.get_board_name()
        self.column_dict_list = self.get_board_column_ids()
        self.color_dict_list = self.get_board_colors()

    def get_board_name(self) -> str:
        return self.board_json["name"]

    def get_board_column_names(self) -> list:
        return [col["name"] for col in self.board_json["columns"]]

    def get_board_column_ids(self) -> list:
        """
        Using the board dict, returns a list of dictionaries with the key-value
        pairs of:
            1. "uniqueId"
            2. "name"
        """
        return self.board_json["columns"]

    def get_board_colors(self):
        """
        Using the board dict, returns a list of dictionaries with the key-value
        pairs of:
            1. "name"
            2. "value" (primary key, this is used to designate colors when 
                updating or creating tasks)
        """
        return self.board_json["colors"]


if __name__ == "__main__":
    pass
