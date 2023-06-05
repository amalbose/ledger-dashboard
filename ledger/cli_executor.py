import subprocess
from io import StringIO
import csv
import pandas as pd

#
# ledger bal -p 'this month'  --format  '%(quoted(display_total)),%(quoted(account)),%(quoted(partial_account)),%(depth)\n%/'
# ledger bal Assets -X INR --depth=3 --format  '%(quoted(account)),%(quoted(display_total)),%(depth)\n%/'


def get_leader_bal():
    ledger_bal = subprocess.run(["ledger", "bal", "Assets", "-X", "INR", "--depth", "3", "--format", "%(quoted(account)),%(quoted(display_total)),%(depth)\n"],
                                stdout=subprocess.PIPE,
                                text=True)
    f = StringIO(ledger_bal.stdout)
    reader = csv.reader(f, delimiter=',')
    data = {}
    total = 0
    for row in reader:
        if int(row[2]) > 2:
            type = row[0].split(":")[1].lower()
            name = row[0].split(":")[2]
            if type not in data:
                data[type] = {}
            amount = float(row[1].replace(" INR", ""))
            data[type][name] = amount
            total = total + amount
    data['total'] = total
    return data

# ledger bal Income Expense -p 'this month' --depth=1 --format '%(quoted(account)),%(quoted(display_total))\n'


def get_income_statements():
    ledger_bal = subprocess.run(["ledger", "bal", "Income", "Expense", "-X", "INR", "-p", "this month", "--depth", "1", "--format", "%(quoted(account)),%(quoted(display_total))\n"],
                                stdout=subprocess.PIPE,
                                text=True)
    f = StringIO(ledger_bal.stdout)
    reader = csv.reader(f, delimiter=',')
    cur = {}
    for row in reader:
        if row[0] != "":
            cur[row[0].lower()] = abs(float(row[1].replace(" INR", "")))
    data = {
        'cur': cur
    }
    return data


# hledger balance -M income expense --tree -E -O csv --layout=tidy
def get_expenses_data():
    ledger_bal = subprocess.run(["hledger", "balance", "-M", "expense", "-X", "INR", "--tree", "-E", "-O", "csv", "--layout", "tidy"],
                                stdout=subprocess.PIPE,
                                text=True)
    f = StringIO(ledger_bal.stdout)
    reader = csv.reader(f, delimiter=',')
    data = []
    indx = 0
    for row in reader:
        if indx == 0:   # skip header
            indx = indx + 1
            continue
        splits = row[0].split(":")
        if len(splits) < 2:
            continue
        datarow = [row[0], row[2], row[5]]
        data.append(datarow)
    return data

# hledger balance -M income expense --tree -E -O csv --layout=tidy


def get_expenses_bare_data():
    ledger_bal = subprocess.run(["hledger", "balance", "-M", "expense", "-X", "INR", "--tree", "-E", "-O", "csv", "--layout", "bare", "--depth", "2"],
                                stdout=subprocess.PIPE,
                                text=True)
    f = StringIO(ledger_bal.stdout)
    reader = csv.reader(f, delimiter=',')
    cols = []
    data = {}
    indx = 0
    headers = ['Date']
    for row in reader:
        if indx == 0:   # skip header
            indx = indx + 1
            cols = row[2:]
            j = 2
            for col in cols:
                data[col] = []
            continue
        splits = row[0].split(":")
        if len(splits) < 2:
            continue
        headers.append(row[0].replace("Expenses:", ""))
        for i in range(0, len(cols)):
            idx = i + 2
            data[cols[i]].append(max(0, float(row[idx])))

    full_data = []
    for key, value in data.items():
        rw = []
        rw.append(key)
        rw = rw + value
        full_data.append(rw)
    return {
        'headers': headers,
        'data': full_data
    }


if __name__ == "__main__":
    print(get_expenses_bare_data())
