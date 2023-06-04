import streamlit as st
import utils
import utils
import plost
import pandas as pd


def show(parent, data):

    full_data = {
        'Type': [],
        'Balance': []
    }
    data_b = data['balances']
    data_total = data_b['total']
    data_savings = data_b['savings']
    data_savings = dict(sorted(data_savings.items(),
                        key=lambda item: item[1], reverse=True))
    data_deposits = data_b['deposit']
    data_deposits = dict(sorted(data_deposits.items(),
                                key=lambda item: item[1], reverse=True))
    parent.markdown(
        "##### Current Assets [" + utils.format_cur(data_total) + "]")

    savings_col, deposits_col = st.columns([0.7, 0.3], gap="large")

    savings_col.markdown("###### Savings Accounts")
    scols = savings_col.columns(len(data_savings))
    indx = 0
    for bank, val in data_savings.items():
        full_data['Type'].append('Savings:' + bank)
        full_data['Balance'].append(val)
        scols[indx].metric(bank, utils.format_cur(val))
        indx = indx + 1

    indx = 0
    deposits_col.markdown("###### Deposits")
    dcols = deposits_col.columns(len(data_deposits))
    for bank, val in data_deposits.items():
        full_data['Type'].append('Deposits:' + bank)
        full_data['Balance'].append(val)
        dcols[indx].metric(bank, utils.format_cur(val))
        indx = indx + 1

    leftc, rightc = parent.columns([.99, 0.01])
    leftc.markdown("###### Investments")
    with leftc:
        data_bal = data['balances']
        data_inv = data_bal['investments']
        data_inv = dict(sorted(data_inv.items(),
                               key=lambda item: item[1], reverse=True))
        icols = parent.columns(len(data_inv))
        indx = 0
        for type, val in data_inv.items():
            full_data['Type'].append('Investments:' + type)
            full_data['Balance'].append(val)
            icols[indx].metric(type, utils.format_cur(val))
            indx = indx + 1

    col_l, col_r = parent.columns([5.5, 4.5])
    with col_r:
        plost.pie_chart(
            title="Asset Balances",
            data=pd.DataFrame(full_data),
            theta='Balance',
            height=300,
            color='Type')
    with col_l:
        plost.bar_chart(
            data=pd.DataFrame(full_data),
            bar='Type',
            value='Balance',
            height=300,
            color='Type',
            legend=None,
            direction='horizontal',
                use_container_width=True)
