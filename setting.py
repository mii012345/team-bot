import json

def get_token():
    with open('setting.json') as f:
        data = json.load(f)

    return data['TOKEN']

def debug():
    with open('setting.json') as f:
        data = json.load(f)

    return bool(data['DEBUG'])