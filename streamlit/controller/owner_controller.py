import streamlit as st
from model import *

def akunData() :
    st.header("📋 Data Akun")
    akun = get_akun_data()
    kontak = get_kontak_data()
    owner = get_Owner_data()
    if not akun.empty and not kontak.empty and not owner.empty:
        for row in akun.itertuples():
            st.write(f"📧 {row.email} | 🔑 {row.password}")
        st.header("📞 Data Kontak")
        for i in kontak.itertuples():
            st.write(f"👤 {i.Owner} | 📱 {i.NomorHP}")
        st.header("👑 Owner Only")
        for i in owner.itertuples():
            st.write(f"Nama Owner ke-{i.Index+1}: {i.Owner}")
    else:
        st.warning("Tidak ada data akun ditemukan.")



