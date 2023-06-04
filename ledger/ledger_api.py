import json


def get_data():
    return get_data_from_json()


def get_data_from_json():
    f = open('data.json')
    return json.load(f)
