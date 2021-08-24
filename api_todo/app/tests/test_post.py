import requests

import pytest


@pytest.fixture
def post_json():
    post_json = {
        'done': False,
        'name': 'Fazer o almoço as 12:00'
    }

    return post_json


def test_post(post_json):
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = 'http://127.0.0.1:8000/todo/'


    response = requests.post(url, headers=headers, data=post_json)
    response_dict = response.json()

    if response == 201:
        assert response_dict['id'] is not None


