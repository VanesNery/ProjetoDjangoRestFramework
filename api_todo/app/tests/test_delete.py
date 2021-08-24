import requests


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
    