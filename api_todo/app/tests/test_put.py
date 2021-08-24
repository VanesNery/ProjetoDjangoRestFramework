import requests

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

