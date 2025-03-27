import os
import streamlit as st

def clearTerminal():
    if st.session_state.get("clearTerminal", False) or st.session_state.get("clearTerminalButton", False):
        os.system('cls' if os.name == 'nt' else 'clear')

def testingCheckbox():
    """Fungsi untuk mengecek status checkbox di Streamlit."""
    if st.session_state.get("tes", False):
        print('Anda sudah benar')
    else:
        print('Anda salah')

def pilihanDivisi():
    """Menampilkan divisi yang dipilih oleh pengguna."""
    divisi = st.session_state.get("divisi", "")
    print(f'Anda Memilih Divisi {divisi}')

def organizationSelection():
    """Menampilkan organisasi yang dipilih oleh pengguna."""
    organisasi = st.session_state.get("organisasi", "")
    print(f'Anda Memilih organisasi {organisasi}')
