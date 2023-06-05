import pandas as pd
import plost
import streamlit as st


def show(parent, data):
    show_budgetsummary(parent, data)
    # show_budgettable(parent, data)
    # show_areachart(parent, data)


def show_budgetsummary(parent, data):
    coll, colm, colr, cole = parent.columns([6, 0.3, 4.5, 0.2])

    with coll:
        table_data = data['summary']
        parent.markdown("##### Budgeted Expenses")
        df = pd.DataFrame(table_data['data'], columns=table_data['headers'])
        parent.dataframe(df, column_config={
            "Index": st.column_config.Column(
                width='small'
            ),
            "Percent": st.column_config.ProgressColumn(
                "Percent",
                format="%d %%",
                width='medium',
                min_value=0,
                max_value=100
            ),
            "Amount": st.column_config.NumberColumn(
                "Amount",
                format="₹ %d",
                width='medium',
                min_value=0,
                max_value=100,
            ),
            "Budget": st.column_config.NumberColumn(
                "Budget",
                format="₹ %d",
                width='medium',
                min_value=0,
                max_value=100,
            ),
        }, height=500)

    with colr:
        parent.markdown("##### Non Budgeted Expenses")
        ndf = pd.DataFrame(table_data['nondata'],
                           columns=table_data['headers'])
        parent.dataframe(ndf, column_config={
            "Index": st.column_config.Column(
                width='small'
            ),
            "Percent": st.column_config.ProgressColumn(
                "Percent of Total Budget",
                format="%d %%",
                width='medium',
                min_value=0,
                max_value=100
            ),
            "Amount": st.column_config.NumberColumn(
                "Amount",
                format="₹ %d",
                width='medium',
                min_value=0,
                max_value=100,
            ),
            "Budget": None,
        }, height=500)


def show_budgettable(parent, data):
    table_data = data['data']
    df = pd.DataFrame(table_data['data'], columns=table_data['headers'])
    parent.dataframe(df, column_config={
        "Index": st.column_config.Column(
            width='small'
        ),
        "AllPercent": st.column_config.ProgressColumn(
            "Non Budget Percent",
            format="%d %%",
            width='medium',
            min_value=0,
            max_value=100,
        ),
        "Percent": st.column_config.ProgressColumn(
            "Percent",
            format="%d %%",
            width='medium',
            min_value=0,
            max_value=100
        ),
        "Amount": st.column_config.NumberColumn(
            "Amount",
            format="₹ %d",
            width='medium',
            min_value=0,
            max_value=100,
        ),
        "Budget": st.column_config.NumberColumn(
            "Budget",
            format="₹ %d",
            width='medium',
            min_value=0,
            max_value=100,
        ),
    }, height=775)
