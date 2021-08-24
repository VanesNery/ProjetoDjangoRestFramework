import requests

import pytest


@pytest.fixture
def response_json():
    return {
        'created_at': '2021-08-13T14:06:48.020798Z',
        'done': False,
        'id': 2,
        'name': 'Fazer café as 08:00'
        }


def test_get_response(response_json):
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = 'http://127.0.0.1:8000/todo/'

    response = requests.get(url, headers=headers)
    response_dict = response.json()

    status = response_dict[0]

    assert status == response_json
