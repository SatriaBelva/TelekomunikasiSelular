import streamlit as st
conn = st.connection('internship_RLO', type='sql')

def get_akun_data():
    akun = conn.query('SELECT email, password FROM akun;', ttl=600)
    return akun

def get_kontak_data():
    kontak = conn.query('SELECT * FROM kontak;', ttl=600)
    return kontak
