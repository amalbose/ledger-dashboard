import streamlit as st

st.set_page_config(layout='wide', initial_sidebar_state='expanded',
                   page_title='Finance Dashboard')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.write("Hello World")
