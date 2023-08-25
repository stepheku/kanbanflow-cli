import requests
import json
import kanbanflow_cli.api
import urllib.parse

class KanbanSubTask:
    def __init__(self, subtask_json: dict, subtask_idx: int=None, 
                 task_id: str=None):
        self.name = subtask_json['name']
        self.finished = subtask_json['finished']
        self.index = subtask_idx
        self.task_id = task_id

    def __repr__(self):
        return 'KanbanSubTask object: {}'.format(self.name)

    def __str__(self):
        return 'KanbanSubTask object: {}'.format(self.name)

    def update_subtask(self, name: str=None, finished: bool=None):
        if self.index is not None:
            search_method = 'by-index'
            search_param = str(self.index)
        elif name is not None:
            search_method = 'by-name'
            search_param = urllib.parse.quote(name)

        data = {'finished': finished}

        url_addition = '/'.join([
            'tasks', self.task_id, 'subtasks', search_method, search_param])
        url = kanbanflow_cli.api.base_url + url_addition

        return kanbanflow_cli.api.post_with_api_headers(url=url, data=data)


if __name__ == "__main__":
    pass