import json
from .cli_executor import *


def get_data():
    data = {
        'income_statement': get_income_statements(),
        'balances': get_leader_bal()
    }
    print(data)
    return data


def get_data_from_json():
    f = open('data.json')
    return json.load(f)
