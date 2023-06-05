import pandas as pd
import plost
import streamlit as st


def show(parent, data):
    show_barchart(parent, data)
    # show_areachart(parent, data)


def show_areachart(parent, data):
    expenses = data['expenses']
    df = pd.DataFrame(expenses, columns=['Name', 'Date', 'Amount'])
    plost.area_chart(
        data=df,
        x=dict(field='Date', timeUnit='month'),
        y=dict(field='Amount', aggregate='mean'),
        color='Name',
        legend='right',
        height=600
    )


def show_barchart(parent, data):

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
