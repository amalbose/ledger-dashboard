import subprocess
from io import StringIO
import csv

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
    total = 0
    for row in reader:
        if row[0] != "":
            cur[row[0].lower()] = abs(float(row[1].replace(" INR", "")))
    data = {
        'cur': cur
    }
    return data


if __name__ == "__main__":
    print(get_income_statements())
