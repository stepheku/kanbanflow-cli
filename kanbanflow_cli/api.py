import os
import base64
import requests
import json
import pdb

class KanbanFlowConnector:
    pass


base_url = 'https://kanbanflow.com/api/v1/'

task_valid_parameters = [
    'columnId',
    'columnIndex',
    'columnName',
    'startTaskId',
    'startGroupingDate',
    'limit',
    'order',
]


def api_key_b64_header(api_key: str) -> dict:
    if not api_key:
        raise(EnvironmentError('Missing API key from function'))
    elif not isinstance(api_key, str):
        raise(AttributeError('API key must be in a String format'))
    else:
        api_key = api_key.encode('utf-8')
        api_key_b64 = base64.b64encode(b'apiToken:' + api_key)
        headers = {
            'Authorization': 'Basic {}'.format(api_key_b64.decode('utf-8'))
        }
        return headers


def get_with_api_headers(url: str) -> dict:
    """
    Runs a GET with headers per KanbanFlow API
    :param url: URL to be retrieved
    """
    api_key = os.environ.get('KBFLOW_API')
    headers = api_key_b64_header(api_key)
    return json.loads(requests.get(url, headers=headers).text)


def post_with_api_headers(url: str, data: dict) -> requests.post:
    api_key = os.environ.get('KBFLOW_API')
    headers = api_key_b64_header(api_key)
    headers['Content-type'] = 'application/json'
    return requests.post(url=url, json=data, headers=headers)


def url_with_param(url: str, param: str, param_value: str) -> str:
    """
    Returns an appended URL for a GET with a supplied parameter and value
    """
    if param and param_value:
        return '{}?{}={}'.format(url, param, param_value)


def check_mandatory_fields(mandatory_fields: list = None,
                           or_mandatory_fields: list = None,
                           local_vars: dict = None) -> list:
    keys_without_values = []
    if mandatory_fields:
        for k, v in local_vars.items():
            if k in mandatory_fields and not v:
                keys_without_values.append(k)
        if not keys_without_values:
            return True
        else:
            raise(AttributeError('Mandatory fields are blank: {}'.format(
                ', '.join(keys_without_values))))
    elif or_mandatory_fields:
        for k, v in local_vars.items():
            if k in or_mandatory_fields and v is not None:
                keys_without_values.append(k)
        if set(or_mandatory_fields) != set(keys_without_values):
            return True
        else:
            pdb.set_trace()
            raise(AttributeError('One of the mandatory fields are blank: {}'.format(
                ', '.join(keys_without_values))))


def format_group_date():
    # TODO:
    # Things to handle:
    # 1. Datetime object
    # 2. Parsed date format mm/dd/yyyy
    # 3. Parsed date format yyyy/mm/dd
    # Maybe check out the dateutil library
    pass
