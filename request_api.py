import requests
from .bearer_auth import BearerAuth


def requests_by_get(url, token):
    headers = {'Content-Type': 'application/json'}
    auth = BearerAuth(token)
    try:
        response = requests.get(url, auth=auth, headers=headers)
        return response.json()
    except Exception as err:
        error_message = "Error en la conexión con el servidor."
        print(error_message, err)


def requests_by_post(url, body, token):
    headers = {'Content-Type': 'application/json'}
    auth = BearerAuth(token) if token else False
    try:
        response = requests.post(url,  auth=auth, json=body, headers=headers)
        return response.json()
    except Exception as err:
        error_message = "Error en la conexión con el servidor."
        print(error_message, err)
