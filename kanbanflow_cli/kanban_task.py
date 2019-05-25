from kanbanflow_cli.kanban_subtask import KanbanSubTask

class KanbanTask:
    def __init__(self, task_json: dict):
        # TODO: Task index would be taken care of by the list of dictionaries
        # when obtaining kanban task list
        self.id = task_json['_id']
        self.name = task_json['name']
        self.description = task_json['description']
        self.color = task_json['color']
        self.column_id = task_json['columnId']
        if task_json.get('subTasks'):
            self.sub_task_list = self.subtask_json_list_to_subtask_obj_list(
                task_json.get('subTasks'))

    def subtask_json_list_to_subtask_obj_list(self,
                                              subtask_json_list: list) -> list:
        return [KanbanSubTask(subtask) for subtask in subtask_json_list]

    def __repr__(self):
        return 'KanbanTask object: {}'.format(self.name)

    def __str__(self):
        return 'KanbanTask object: {}'.format(self.name)

