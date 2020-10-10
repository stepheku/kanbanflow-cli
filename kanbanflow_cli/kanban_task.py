from urllib.parse import urljoin
from kanbanflow_cli.kanban_subtask import KanbanSubTask
import kanbanflow_cli.api as api


class KanbanTask:
    def __init__(self, task_json: dict=None,
        name: str = None,
        columnId: str = None,
        columnIndex: int = None,
        swimlaneId: str = None,
        position: str = None,
        color: str = None,
        description: str = None,
        number: dict = None,
        responsibleUserId: str = None,
        totalSecondsSpent: int = None,
        totalSecondsEstimate: int = None,
        pointsEstimate: float = None,
        dates: dict = None,
        subTasks: list = None,
        labels: list = None,
        collaborators: list = None,):
        self.api_connector = api.KanbanFlowAPICalls()

        if task_json is not None:
            self.id = task_json['_id']
            self.name = task_json['name']
            self.description = task_json['description']
            self.color = task_json['color']
            self.column_id = task_json['columnId']
            self.responsible_user_id = task_json.get('responsibleUserId')
            if task_json.get('subTasks'):
                self.subtask_list = self.subtask_json_list_to_subtask_obj_list(
                    task_json.get('subTasks'))
        
        else:
            self.id = self.api_connector.create_task(
                name=name,
                columnId=columnId,
                columnIndex=columnIndex,
                swimlaneId=swimlaneId,
                position=position,
                color=color,
                description=description,
                number=number,
                responsibleUserId=responsibleUserId,
                totalSecondsSpent=totalSecondsSpent,
                totalSecondsEstimate=totalSecondsEstimate,
                pointsEstimate=pointsEstimate,
                dates=dates,
                subTasks=subTasks,
                labels=labels,
                collaborators=collaborators
            ).get("taskId")

            self.name = name
            self.column_id = columnId
            self.swimlane_id = swimlaneId
            self.position = position
            self.color = color
            self.description = description
            self.number = number
            self.responsible_user_id = responsibleUserId
            self.total_seconds_spent = totalSecondsSpent
            self.total_seconds_estimate = totalSecondsEstimate
            self.points_estimate = pointsEstimate
            self.dates = dates
            self.subTasks = subTasks
            self.labels = labels
            self.collaborators = collaborators

    def subtask_json_list_to_subtask_obj_list(self,
                                              subtask_json_list: list) -> list:
        return [KanbanSubTask(subtask_json=subtask, subtask_idx=idx, 
                              task_id=self.id) 
                for idx, subtask in enumerate(subtask_json_list)]
    
    def __repr__(self):
        return 'KanbanTask object: {}'.format(self.name)

    def __str__(self):
        return 'KanbanTask object: {}'.format(self.name)
