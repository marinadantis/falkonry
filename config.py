import json

with open('config.json') as config_json:
    cfg = json.loads(config_json.read())
    locals().update(cfg)
