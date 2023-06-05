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
    print(bare_data['data'][:2])
    bdf = pd.DataFrame(bare_data['data'], columns=bare_data['headers'])

    st.bar_chart(bdf, x='Date',
                 height=600)
