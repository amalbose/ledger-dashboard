import streamlit as st
import utils
import pandas as pd
import numpy as np
import plost


def show(parent, data):
    parent.markdown("##### Income Statment")

    data_is = data['income_statement']
    data_cur = data_is['cur']

    col_l, col_r = parent.columns(2)
    with col_l:
        data = {
            'Name': ['Income', 'Expense'],
            'Value': [data_cur['income'], data_cur['expenses']]
        }

        plost.bar_chart(
            data=pd.DataFrame(data),
            bar='Name',
            value='Value',
            color='Name',
            legend=None,
            direction='horizontal',
                use_container_width=True)
    with col_r:
        income = utils.format_cur(data_cur['income'])
        expense = utils.format_cur(data_cur['expenses'])
        net = utils.format_cur(data_cur['income'] - data_cur['expenses'])

        income_col, expense_col, net_col = st.columns(3)
        income_col.metric("Income", income)
        expense_col.metric("Expenses", expense)
        net_col.metric("Net", net)
