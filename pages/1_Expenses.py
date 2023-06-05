import streamlit as st

import components.expenses as ex
import ledger.ledger_api as ledger


st.set_page_config(layout='wide', initial_sidebar_state='expanded',
                   page_title='Finance Dashboard')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


@st.cache_data
def load_data():
    return ledger.get_expense_data()


ex.show(st, load_data())
