import json
from .cli_executor import *


def get_home_data():
    data = {
        'income_statement': get_income_statements(),
        'balances': get_leader_bal()
    }
    return data


def get_expense_data():
    data = {
        'expenses': get_expenses_data(),
        'expenses-bare': get_expenses_bare_data()
    }
    return data


def get_budget_data():
    data = {
        'data': get_budgets_data(),
        'summary': get_budgets_summary()
    }
    return data


def get_data_from_json():
    f = open('data.json')
    return json.load(f)
