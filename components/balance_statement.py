import streamlit as st
import utils


def show(parent, data):
    parent.markdown("##### Current Balance")

    data_is = data['balances']
    data_savings = data_is['savings']
    data_deposits = data_is['deposits']

    savings_col, deposits_col = st.columns([0.7, 0.3], gap="large")

    savings_col.markdown("###### Savings Accounts")
    scols = savings_col.columns(len(data_savings))
    indx = 0
    for bank, val in data_savings.items():
        scols[indx].metric(bank, utils.format_cur(val))
        indx = indx + 1

    indx = 0
    deposits_col.markdown("###### Deposits")
    dcols = deposits_col.columns(len(data_deposits))
    for bank, val in data_deposits.items():
        dcols[indx].metric(bank, utils.format_cur(val))
        indx = indx + 1
