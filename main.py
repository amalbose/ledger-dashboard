import streamlit as st
import pandas as pd
import numpy as np
import json

import components.income_statement as inst
import components.balance_statement as bal

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

f = open('data.json')
data = json.load(f)
st.sidebar.header('Finance Dashboard')

inst.show(st, data)
bal.show(st, data)
