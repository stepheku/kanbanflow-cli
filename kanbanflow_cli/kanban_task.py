from urllib.parse import urljoin
from kanbanflow_cli.kanban_subtask import KanbanSubTask
import kanbanflow_cli.api as api


class KanbanTask:
    def __init__(self, task_json: dict, task_list=None):
        # TODO: Task index would be taken care of by the list of dictionaries
        # when obtaining kanban task list

        self.api_url = urljoin(api.base_url, 'tasks')

        self.id = task_json['_id']
        self.name = task_json['name']
        self.description = task_json['description']
        self.color = task_json['color']
        self.column_id = task_json['columnId']
        self.responsible_user_id = task_json.get('responsibleUserId')
        if task_json.get('subTasks'):
            self.sub_task_list = self.subtask_json_list_to_subtask_obj_list(
                task_json.get('subTasks'))

        if task_list is not None:
            if task_json not in task_list.all_task_json:
                self.create_task(task_json)

    @classmethod
    def create_task(cls, data: dict) -> str:
        """
        Creates KanbanFlow Task and adds to board

        :param data: Task dictionary (keys 'name' and 'columnId' required)
        :return: taskId str of the task created
        """
        required_keys = ['name', 'columnId']
        for key in required_keys:
            if data.get(key) is None:
                raise KeyError('Missing required key: {}'.format(key))

        api_url = urljoin(api.base_url, 'tasks')

        return api.post_with_api_headers(api_url, data).get('taskId')

    def subtask_json_list_to_subtask_obj_list(self,
                                              subtask_json_list: list) -> list:
        return [KanbanSubTask(subtask) for subtask in subtask_json_list]

    def __repr__(self):
        return 'KanbanTask object: {}'.format(self.name)

    def __str__(self):
        return 'KanbanTask object: {}'.format(self.name)
