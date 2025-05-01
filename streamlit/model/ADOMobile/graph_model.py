import streamlit as st
from model import *

ADOMobileconn = gsheet_ADOMobile_connection()
df = ADOMobileconn.read(ttl=2)

def get_Kabupaten_data(): 
    try:
        return df['KABUPATEN'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_CB_data(): 
    try:
        return df['CB'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Populasi_data(): 
    try:
        return df['POPULASI'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None