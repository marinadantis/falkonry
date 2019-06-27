import json
import config
#import newconfig
import random
import string
import falkonry_methods


def main():

    # api_url of Falkonry project (e.g. 'https://dev.falkonry.ai:30076/api/1.1/accounts/Qqa5uqp4zvq0qv/datastreams')
    api_url = config.api_url_base + "accounts/" + config.account_id + "/datastreams"

    # Unique name creation in payload (e.g.marinads_abc12)
    suffix = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
    name = config.prefix + "_" + suffix
    config.payload['name'] = name
    payload_json = json.dumps(config.payload)

    # Authorization token configuration in headers
    authorization = "Bearer" + " " + config.api_token
    config.headers['Authorization'] = authorization

    # POST request call
    response = falkonry_methods.make_request('POST', api_url, payload_json, config.headers)

    # Display Status code
    content = falkonry_methods.display_status_code(response, api_url)

    # Display response json
    falkonry_methods.display_response_json(content)


if __name__ == "__main__":
    main()
