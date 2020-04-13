"""
reports_util.py
~~~~~~~~~~~~~~~~~~~~
Module contains functions that are specific for reporting, such as:
- Tasks that have been worked on in the last 24 hours
- Time spent on certain tasks
"""

import requests
import json
import csv
from urllib.parse import urljoin
from datetime import datetime
from datetime import timedelta
import kanbanflow_cli.api as api
from kanbanflow_cli.kanban_task_list import KanbanTask, KanbanTaskList

DATETIME_STR_FORMAT = "%Y-%m-%dT0000Z-5"


def get_time_entries_for_board(from_time: str, to_time: str) -> list:
    api_url = urljoin(api.base_url,
                      'time-entries?from={}&to={}'.format(from_time, to_time))

    return api.get_with_api_headers(api_url)


def get_time_entries_for_board_last_day() -> list:
    last_day_from = datetime.strftime(
        datetime.today() + timedelta(days=-1), format=DATETIME_STR_FORMAT
    )
    last_day_to = datetime.strftime(
        datetime.today(), format=DATETIME_STR_FORMAT
    )
    return get_time_entries_for_board(
        from_time=last_day_from, to_time=last_day_to
    )


def get_time_entries_for_board_current_day() -> list:
    last_day_from = datetime.strftime(
        datetime.today(), format=DATETIME_STR_FORMAT
    )
    last_day_to = datetime.strftime(
        datetime.today() + timedelta(days=1), format=DATETIME_STR_FORMAT
    )
    return get_time_entries_for_board(
        from_time=last_day_from, to_time=last_day_to
    )


def get_task_names_for_time_entries(time_entries: list,
                                    task_list: KanbanTaskList) -> list:
    """
    When doing a GET request to get time entries, a list of dictionaries is
    returned with the taskId. This function uses the taskId to give a list of
    task names in the time entry list

    :param: time_entries: List of dictionaries of time entries, from GET request

    :param: task_list: KanbanTaskList object that contains all tasks on the 
    board

    :return: Returns a list of task names in the time entrylist
    """
    return [task_list.get_task_name_by_task_id(task_id=x.get('taskId')) 
            for x in time_entries]


if __name__ == "__main__":
    print('Connecting to KanbanFlow task list...')
    task_list = KanbanTaskList()
    print('Connected to task list')
    a = get_time_entries_for_board('2020-04-01T00:00Z-5', '2020-04-02T00:00Z-5')
    task_names = get_task_names_for_time_entries(time_entries=a, 
                                                 task_list=task_list)
    uniq_task_names = set(task_names)
    with open('output.csv', 'w', newline='') as f:
        header = ['Task name']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for task in uniq_task_names:
            writer.writerow({'Task name': task})