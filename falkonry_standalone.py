import json
import requests
import config
import random
import string


def create_datastream():

    # api_url of Falkonry project
    # api_url = 'https://dev.falkonry.ai:30076/api/1.1/accounts/Qqa5uqp4zvq0qv/datastreams'
    # api_url = '{0}accounts/{1}/datastreams'.format(config.api_url_base, config.account_id)
    api_url = config.api_url_base + "accounts/" + config.account_id + "/datastreams"

    # Unique name creation in payload (e.g.marinads_abc12)
    suffix = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
    name = config.prefix + "_" + suffix
    config.payload['name'] = name
    payload_json = json.dumps(config.payload)

    # Authorization token configuration in headers
    Authorization = "Bearer" + " " + config.api_token
    config.headers['Authorization'] = Authorization

    # POST request call
    response = requests.post(api_url, data=payload_json, headers=config.headers)

    if response.status_code == 201:
        print(response)
        return json.loads(response.content.decode('utf-8'))
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
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


def display_response_json(response):
    if response is not None:
        print("Here's your info: ")
        for k, v in response.items():
            print('{0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')


def main():
    repsonse_json = create_datastream()
    display_response_json(repsonse_json)


if __name__ == "__main__":
    main()
