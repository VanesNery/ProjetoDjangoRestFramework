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


def test_put():
    headers = {
        'Accept':'*/*',
        'User-Agent': 'request',
    }

    post_json = {
        'done': False,
        'name': 'Fazer o almoço as 13:00'
    }

    url = 'http://127.0.0.1:8000/todo/'
    response = requests.get(url, headers=headers)
    response_dict = response.json()
    status = response_dict[2]['id']

    response = requests.put(url + str(f'{status}/'), data=post_json, headers=headers)
    response_dict = response.json()
    if response == 201:
        assert response_dict == post_json


def test_delete():
    headers = {
        'Accept':'*/*',
        'User-Agent': 'request',
    }

    url = 'http://127.0.0.1:8000/todo/'

    response = requests.get(url, headers=headers)
    response_dict = response.json()
    status = response_dict[2]['id']

    response = requests.delete(url + str(f'{status}/'), headers=headers)
    response_dict = response.__dict__['status_code']

    assert response_dict == 204
    
    
