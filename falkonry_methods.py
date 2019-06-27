import json
import requests


def make_request(method, url, payload, headers):
    if method.upper() == 'POST':
        response = requests.post(url, data=payload, headers=headers)
        return response
    elif method.upper() == 'GET':
        response = requests.get(url, headers=headers)
        return response
    else:
        return None


def display_status_code(response, url):
    if response.status_code == 201:
        print(response)
        return json.loads(response.content.decode('utf-8'))
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None


def display_response_json(content):
    if content is not None:
        print("Here's your info: ")
        for k, v in content.items():
            print('{0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')
