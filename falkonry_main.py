import json
import config
import random
import string
import falkonry_methods


def main():

    data = config.data
    for api in data:
        method = api['method']
        if method.upper() == 'POST':
            # api_url of Falkonry project (e.g. 'https://dev.falkonry.ai:30076/api/1.1/accounts/Qqa5uqp4zvq0qv/datastreams')
            api_url = api['api_url_base'] + "accounts/" + api['account_id'] + "/datastreams"

            # Unique name creation in payload (e.g.marinads_abc12)
            suffix = ''.join(
                random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
            name = api['prefix'] + "_" + suffix
            (api['payload'])['name'] = name
            payload_json = json.dumps(api['payload'])

            # Authorization token configuration in headers
            authorization = "Bearer" + " " + api['api_token']
            (api['headers'])['Authorization'] = authorization

            # POST request call
            response = falkonry_methods.make_request('POST', api_url, payload_json, api['headers'])

            # Display Status code
            content = falkonry_methods.display_status_code(response, api_url)

            # Display response json
            falkonry_methods.display_response_json(content)

        elif method.upper() == 'GET':
            print("Code for GET method.")

        else:
            print("Method is not present, please update config file.")


if __name__ == "__main__":
    main()
