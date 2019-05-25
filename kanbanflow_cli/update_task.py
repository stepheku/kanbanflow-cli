import requests
import json
import kanbanflow_cli.api as api


def create_task(name=None, columnId=None, swimlaneId=None, position=None,
                color=None, description=None, number=None,
                responsibleUserId=None, totalSecondsSpent=0,
                totalSecondsEstimate=0, pointsEstimate=0, groupingDate=None,
                dates=None, subTasks=None, labels={}, collaborators=[]):
    api.check_mandatory_fields(mandatory_fields=['name', 'columnId'],
                               local_vars=locals())

    post_data = {key: val for (key, val) in locals().items() if val}

    return api.post_with_api_headers(url='https://kanbanflow.com/api/v1/tasks',
                                     data=post_data)


def add_comment_to_task(task_id=None, text=None, authorUserId=None,
                        createdTimeStamp=None):
    api.check_mandatory_fields(mandatory_fields=['task_id'],
                               local_vars=locals())
    post_data = {key: val for (
        key, val) in locals().items() if key not in 'task_id' and val}
    task_comments_url = 'https://kanbanflow.com/api/v1/tasks/{}/comments'.format(
        task_id)
    return api.post_with_api_headers(url=task_comments_url, data=post_data)


def update_task(task_id=None, name=None, columnId=None, swimlaneId=None,
                position=None, color=None, description=None, number=None,
                responsibleUserId=None, totalSecondsSpent=0,
                totalSecondsEstimate=0, pointsEstimate=0, groupingDate=None,
                dates=None, subTasks=None, labels={}, collaborators=[]):
    if not task_id:
        raise(AttributeError('Function update_task requires a task_id'))
    else:
        post_data = {key: val for (
            key, val) in locals().items() if key not in 'task_id' and val}
    target_url = 'https://kanbanflow.com/api/v1/tasks/{}'.format(task_id)
    return api.post_with_api_headers(url=target_url, data=post_data)
