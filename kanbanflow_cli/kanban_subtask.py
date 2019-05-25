import requests
import json
import kanbanflow_cli.api


class KanbanSubTask:
    def __init__(self, subtask_json: dict):
        self.name = subtask_json['name']
        self.finished = subtask_json['finished']

    def __repr__(self):
        return 'KanbanSubTask object: {}'.format(self.name)

    def __str__(self):
        return 'KanbanSubTask object: {}'.format(self.name)
