import streamlit as st
import pandas as pd
import numpy as np
import json

import components.income_statement as inst
import components.balance_statement as bal

import ledger.ledger_api as ledger


# @st.cache_data
def load_data():
    return ledger.get_home_data()


st.set_page_config(layout='wide', initial_sidebar_state='expanded',
                   page_title='Finance Dashboard')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

data = load_data()
# st.sidebar.header('Finance Dashboard')

inst.show(st, data)
bal.show(st, data)
