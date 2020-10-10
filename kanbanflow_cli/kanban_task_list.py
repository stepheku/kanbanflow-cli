import requests
import json
import kanbanflow_cli.api as api
from kanbanflow_cli.kanban_task import KanbanTask
from kanbanflow_cli.kanban_subtask import KanbanSubTask


class KanbanTaskList:
    def __init__(
        self, column_name: str = None, column_id: str = None, limit: int = None
    ):
        self.api_connector = api.KanbanFlowAPICalls()

        if column_name is not None and column_id is not None:
            raise (
                AttributeError(
                    "Ambiguous parameters to get tasks. "
                    "Define column_name or column_id, but not both. "
                    "\n"
                    "column_name given: {}"
                    "\n"
                    "column_id given: {}".format(column_name, column_id)
                )
            )

        elif column_name is None and column_id is None:
            self.task_list = self.api_connector.get_all_tasks()

        elif column_id is not None:
            self.task_list = self.api_connector.get_tasks_by_column_id(
                column_id=column_id
            )

        elif column_name is not None:
            self.task_list = self.api_connector.get_tasks_by_column_name(
                column_name=column_name
            )

    def task_json_list_to_task_obj_list(self, task_json_list: list) -> list:
        if task_json_list:
            return [KanbanTask(task) for task in task_json_list]


if __name__ == "__main__":
    pass
