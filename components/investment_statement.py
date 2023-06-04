import streamlit as st
import utils


def show(parent, data):
    parent.markdown("##### Investments")

    data_bal = data['balances']
    data_inv = data_bal['investments']
    icols = parent.columns(len(data_inv))
    indx = 0
    for bank, val in data_inv.items():
        icols[indx].metric(bank, utils.format_cur(val))
        indx = indx + 1
