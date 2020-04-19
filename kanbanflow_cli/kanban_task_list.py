import requests
import json
from urllib.parse import urljoin
import kanbanflow_cli.api as api
from kanbanflow_cli.kanban_task import KanbanTask
from kanbanflow_cli.kanban_subtask import KanbanSubTask


class KanbanTaskList:
    def __init__(self, limit: int=None):
        self.limit = limit
        self.api_url = urljoin(api.base_url, 'tasks')
        self.all_task_json = self.get_all_task_json()

    def get_all_task_json(self) -> list:
        if self.limit and self.limit != 20 and self.limit <= 100:
            api_url = self.api_url + '?limit={}'.format(self.limit)
        else:
            api_url = self.api_url
        return api.get_with_api_headers(api_url)
    
    def get_task_name_by_task_id(self, task_id: str) -> str:
        task_name = ''

        for col in self.all_task_json:
            for task in col.get('tasks'):
                if task.get('_id') == task_id:
                    task_name = task.get('name')
                    break

        if task_name:
            return task_name

        else:
            task_resp = api.get_with_api_headers(self.api_url + '/' + task_id)
            return task_resp.get('name')

    def get_column_index(self, column_name: str = None,
                         column_id: str = None) -> int:
        if self.all_task_json and column_name:
            for idx, col in enumerate(self.all_task_json):
                if col['columnName'] == column_name:
                    return idx
        if self.all_task_json and column_id:
            for idx, col in enumerate(self.all_task_json):
                if col['columnId'] == column_id:
                    return idx

    def get_task_list_by_column(self, columnId: str = None, columnIndex: int = None,
                                columnName: str = None, startTaskID: str = None,
                                startGroupingDate: str = None, limit: int = None,
                                order: str = None):
        api.check_mandatory_fields(or_mandatory_fields=[
                                   'columnId', 'columnIndex',
                                   'columnName'], local_vars=locals())
        if columnId:
            return api.get_with_api_headers
        elif columnIndex is not None:
            return (self.get_task_list_by_column_index(columnIndex))
        elif columnName:
            return (self.get_task_list_by_column_name(columnName))

    def get_task_list_by_column_id(self, column_id: str) -> list:
        # TODO: Handle an invalid column_id
        if not self.all_task_json:
            return api.get_with_api_headers(
                api.url_with_param(
                    self.api_url, 'columnId', str(column_id))
            )[0]
        else:
            col_idx = self.get_column_index(column_id=column_id)
            return self.task_json_list_to_task_obj_list(
                self.all_task_json[col_idx]['tasks'])

    def get_task_list_by_column_index(self, column_idx: int) -> list:
        # TODO: Handle an invalid index
        if not self.all_task_json:
            return api.get_with_api_headers(
                api.url_with_param(
                    self.api_url, 'columnIndex', str(column_idx))
            )[0]
        else:
            return self.task_json_list_to_task_obj_list(
                self.all_task_json[column_idx]['tasks'])

    def get_task_list_by_column_name(self, column_name: str) -> list:
        # TODO: Need to have a way to validate column_name against columns
        if not self.all_task_json:
            return api.get_with_api_headers(
                api.url_with_param(self.api_url, 'columnName', column_name)
            )[0]
        else:
            col_idx = self.get_column_index(column_name)
            return self.task_json_list_to_task_obj_list(
                self.all_task_json[col_idx]['tasks'])

    def task_json_list_to_task_obj_list(self, task_json_list: list) -> list:
        if task_json_list:
            return [KanbanTask(task) for task in task_json_list]

if __name__ == '__main__':
    pass