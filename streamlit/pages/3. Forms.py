import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from config import DB_CONFIG
from matplotlib import pyplot as plt
from utils import clearTerminal, testingCheckbox, pilihanDivisi, organizationSelection, previewUploadedFile, usernameAndPassword, registration

st.title("Forms Element")
st.text("Pada Page ini kita akan belajar mengenai cara membuat dashboard data menggunakan Components yang ada di streamlit dengan sedikit bantuan dari library pandas")

# Contoh Yang Benar 
st.markdown("<h1 style='text-align : center;'>User Registration</h1>", unsafe_allow_html=True)
with st.form(key='form2', clear_on_submit=False, enter_to_submit=False) : # Harus menggunakan with agar aplikasi tidak rerun setiap ada perubahan di widgetnya dan hanya direrun setelah form disubmit melalui submit button     
    col1, col2, col3 = st.columns(spec=3)
    firstname    = col1.text_input(label='Firstname')
    surname      = col2.text_input(label='Surname')
    lastname     = col3.text_input(label='Lastname')
    username     = st.text_input(label='Username', help='username harus unik')
    birthdate    = st.date_input(label='Silahkan Pilih Tanggal Lahir Anda',help='Silahkan Pilih Tanggal Lahir Anda',format='DD/MM/YYYY',max_value=datetime.date.today(),min_value=datetime.date(1925, 6, 23), value=datetime.date(2002, 8, 31) )
    password1    = st.text_input(label='Password', type='password', help='password boleh berbeda')
    password2    = st.text_input(label='Confirm Password', type='password')
    submitButton = st.form_submit_button(label='Submit', use_container_width=True, type='secondary', on_click=registration )
    if submitButton :
        if firstname == "" or surname == "" or lastname == "" :
            st.warning(body="Please Fill in Your Name", icon='⚠️')
        elif username == "" :
            st.error(body="Goblog", icon='🧠')
        elif password1 == "":
            st.warning(body="Password Tidak Boleh Kosong", icon='⚠️')
        elif password2 == "":
            st.warning(body="Tolong Konfirmasi Password Anda", icon='⚠️')
        elif password1 != password2 :
            st.warning(body="Password Tidak Sama", icon='⚠️')
        else : 
            # Simpan ke session_state sebelum memanggil fungsi
            st.session_state['registration'] = {
                "firstname": firstname,
                "surname": surname,
                "lastname": lastname,
                "username": username,
                "birthdate": birthdate,
                "password": password1
            }
            st.success(body="Akun Berhasil Dibuat!", icon='🔥')
            registration()