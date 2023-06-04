import streamlit as st
import utils


def show(parent, data):
    parent.markdown("##### Income Statment")

    data_is = data['income_statement']
    data_cur = data_is['cur']
    income = utils.format_cur(data_cur['income'])
    expense = utils.format_cur(data_cur['expense'])
    net = utils.format_cur(data_cur['income'] - data_cur['expense'])

    income_col, expense_col, net_col = st.columns(3)
    income_col.metric("Income", income)
    expense_col.metric("Expenses", expense)
    net_col.metric("Net", net)
