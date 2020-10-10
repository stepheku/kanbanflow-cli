import os
import base64
import requests
import json
from datetime import datetime
from dateutil.parser import parse
import urllib.parse

base_url = "https://kanbanflow.com/api/v1/"


class KanbanFlowAPICalls:
    """
    Contains all documented KanbanFlow API calls
    """

    def __init__(self):
        pass

    def get_board(self) -> dict:
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["board"]))

    def get_all_tasks(self, limit: int=20):
        url = api_url_extend_path_seg(base_url, ["tasks"])
        param_dict = {'limit':limit}

        if not isinstance(limit, int):
            raise TypeError('limit is an int type')
        elif limit == 20:
            return get_with_api_headers(url)
        else:
            return get_with_api_headers(
                url_with_param(url=url, param_dict=param_dict)
            )

    def get_task_by_id(self, task_id: str) -> dict:
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id])
        )

    def get_tasks_by_column_id(self, column_id: str=None) -> list:
        if column_id is not None:
            url = api_url_extend_path_seg(base_url, ["tasks"])
            param_dict = {'columnId': column_id}

            return get_with_api_headers(
                url_with_param(url=url, param_dict=param_dict)
            )

    def get_tasks_by_column_name(self, column_name: str=None) -> list:
        if column_name is not None:
            url = api_url_extend_path_seg(base_url, ["tasks"])
            param_dict = {"columnName": urllib.parse.quote(column_name)}

            return get_with_api_headers(
                url_with_param(url=url, param_dict=param_dict)
            )

    def get_subtasks(self, task_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id, "subtasks"])
        )

    def get_task_labels(self, task_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id, "labels"])
        )

    def get_task_collaborators(self, task_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id, "collaborators"])
        )

    def get_task_comments(self, task_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id, "comments"])
        )

    def get_task_attachments(self, task_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id, "attachments"])
        )

    def get_task_time_entries(self, task_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id, "time-entries"])
        )

    def get_task_manual_time_entry(self, task_id: str, manual_time_entry_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(
                base_url,
                ["tasks", task_id, "manual-time-entries", manual_time_entry_id],
            )
        )

    def get_task_relations(self, task_id: str):
        return get_with_api_headers(
            api_url_extend_path_seg(base_url, ["tasks", task_id, "relations"])
        )

    def get_users(self):
        return get_with_api_headers(api_url_extend_path_seg(base_url, ["users"]))


def api_url_extend_path_seg(base_url: str, path_segments: list) -> str:
    """
    Given a list of path segments to extend on a base url, this will 
    return the extended path segment
    """
    if not isinstance(path_segments, list):
        raise TypeError("Argument path_segments must be a list type")
    elif not all(isinstance(n, str) for n in path_segments):
        raise TypeError("All path segments must be a string type")

    if base_url[-1] != "/":
        base_url += "/"

    return base_url + "/".join(path_segments)


task_valid_parameters = [
    "columnId",
    "columnIndex",
    "columnName",
    "startTaskId",
    "startGroupingDate",
    "limit",
    "order",
]


def api_key_b64_header(api_key: str) -> dict:
    if not api_key:
        raise (EnvironmentError("Missing API key from function"))
    elif not isinstance(api_key, str):
        raise (AttributeError("API key must be in a String format"))
    else:
        api_key = api_key.encode("utf-8")
        api_key_b64 = base64.b64encode(b"apiToken:" + api_key)
        headers = {"Authorization": "Basic {}".format(api_key_b64.decode("utf-8"))}
        return headers


def get_with_api_headers(url: str) -> dict:
    """
    Runs a GET with headers per KanbanFlow API
    :param url: URL to be retrieved
    """
    api_key = os.environ.get("KBFLOW_API")
    headers = api_key_b64_header(api_key)
    return json.loads(requests.get(url, headers=headers).text)


def post_with_api_headers(url: str, data: dict) -> requests.post:
    """
    Runs a POST with headers per KanbanFlow API

    :param url: URL to be retrieved
    :param data: Data to be posted in a dictionary
    """
    api_key = os.environ.get("KBFLOW_API")
    headers = api_key_b64_header(api_key)
    headers["Content-type"] = "application/json"
    return requests.post(url=url, json=data, headers=headers)


def url_with_param(url: str, param_dict: dict=None) -> str:
    """
    Returns an appended URL for a GET with a supplied parameter and value
    """
    if param_dict is None:
        return url
    else:
        return url + '?' + '&'.join('{}={}'.format(k, v) 
                                    for (k, v) in param_dict.items())


def check_mandatory_fields(
    mandatory_fields: list = None,
    or_mandatory_fields: list = None,
    local_vars: dict = None,
) -> list:
    keys_without_values = []
    if mandatory_fields:
        for k, v in local_vars.items():
            if k in mandatory_fields and not v:
                keys_without_values.append(k)
        if not keys_without_values:
            return True
        else:
            raise (
                AttributeError(
                    "Mandatory fields are blank: {}".format(
                        ", ".join(keys_without_values)
                    )
                )
            )
    elif or_mandatory_fields:
        for k, v in local_vars.items():
            if k in or_mandatory_fields and v is not None:
                keys_without_values.append(k)
        if set(or_mandatory_fields) != set(keys_without_values):
            return True
        else:
            raise (
                AttributeError(
                    "One of the mandatory fields are blank: {}".format(
                        ", ".join(keys_without_values)
                    )
                )
            )


def format_group_date(datetime_str: str = None, datetime_obj: datetime = None) -> str:
    datetime_format = "%Y-%m-%d"
    if datetime_str:
        return parse(datetime_str).strftime(datetime_format)
    elif datetime_obj:
        return datetime_obj.strftime(datetime_format)
