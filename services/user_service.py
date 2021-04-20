
from request_api import requests_by_get, requests_by_post


def get_access_token(username, password):
    url = "https://coding-test.rootstack.net/api/auth/login"
    body = {
        "email": username,
        "password": password
    }
    response = requests_by_post(url, body, token=False)
    if response:
        return response.get('access_token', False)
    return False


def get_profile(user, token):
    url = "https://coding-test.rootstack.net/api/auth/me"
    response = requests_by_get(url, token)

    if response and not response.get('message'):
        user.load_by_json(response)
    return user
