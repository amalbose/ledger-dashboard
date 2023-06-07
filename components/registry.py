import pandas as pd
import plost
import streamlit as st


def show(parent, data):
    cur = data['cur']
    cur_data = sorted(cur['data'], key=lambda x: x[0], reverse=True)
    df = pd.DataFrame(cur_data, columns=cur['headers'])
    st.dataframe(df, use_container_width=True, column_config={
        "Amount": st.column_config.NumberColumn(
            "Amount",
            format="₹ %0.2f"
        )}, height=700)
