import pandas as pd
import plost
import streamlit as st


def show(parent, data):
    show_expenseschart(parent, data)
    show_barchart(parent, data)


def show_expenseschart(parent, data):
    parent.markdown("### Expenses")
    expenses = data['expenses']
    df = pd.DataFrame(expenses['data'], columns=expenses['headers'])
    plost.bar_chart(
        data=df,
        color='Name',
        bar='Name',
        legend=None,
        value=expenses['headers'],
        direction='horizontal',
        height=600
    )


def show_barchart(parent, data):
    parent.markdown("### Expense Trends ")

    bare_data = data['expenses-bare']
    bare_data = data['expenses-bare']

    select_list = bare_data['headers'].copy()
    select_list.remove('Date')
    options = st.multiselect(
        'Select Expenses to filter',
        select_list,
        select_list)

    bdf = pd.DataFrame(bare_data['data'], columns=bare_data['headers'])

    coll, colr = parent.columns([.95, 0.05])
    with coll:
        plost.bar_chart(
            title="Expense Categories",
            data=bdf,
            bar='Date',
            pan_zoom='both',
            height=500,
            direction='horizontal',
            value=options,
            use_container_width=True)

    st.dataframe(data=bdf)
