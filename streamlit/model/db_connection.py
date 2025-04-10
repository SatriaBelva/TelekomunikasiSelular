import streamlit as st
def get_connection():
    return st.connection('internship_RLO', type='sql')