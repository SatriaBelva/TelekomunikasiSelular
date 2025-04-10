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

def previewUploadedFile():
    file = st.session_state.get("uploadedFile")
    if file:
        for file in file:
            # if file.name
            print(f"""file id : {file.file_id}\n
                      Judul : {file.name}\n
                      Tipe : {file.type}\n
                      Ukuran : {file.size} Byte\n""") 
            
def usernameAndPassword():
    button = st.session_state.get('usernameAndPasswordSubmitButton')
    username = st.session_state.get('username')
    password = st.session_state.get('password')
    tanggalLahir = st.session_state.get('tanggalLahir')
    deskripsi = st.session_state.get('deskripsi')

    if username and password and tanggalLahir and deskripsi:
        day = tanggalLahir.day
        month = tanggalLahir.strftime("%B")  # Nama bulan dalam bahasa Inggris
        year = tanggalLahir.year
        formatted_date = f"{day} {month} {year}"
        print(f"Username : {username}\nPassword : {password}\nTTL : {formatted_date}\nDeskripsi Diri : {deskripsi}\n")

def registration():
    tes = st.session_state.get('registration')
    if tes:
        # st.write(f"Data dari session_state: {tes}")  # Menampilkan di UI Streamlit
        print(tes)  # Untuk debugging di terminal
    else:
        st.warning("Belum ada data registrasi.")

def hide_sidebar():
    css = """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }

    #MainMenu{
        display: none;
    }

    .stAppDeployButton{
        display: none;
    }
    </style>
    """
    return css

def landing_page_style() :
    css = """
    <style>
    /* Gradient background */
    .landing-container {
        background: linear-gradient(135deg, #f3f4f6, #e0f7fa);
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-top: 100px;
    }

    .landing-title {
        font-size: 40px;
        font-weight: 700;
        color: #0d47a1;
    }

    .landing-subtitle {
        font-size: 18px;
        color: #333333;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    .login-button {
        background-color: #4285F4;
        color: white;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0 4px 14px rgba(66, 133, 244, 0.4);
        transition: background-color 0.3s ease;
    }

    .login-button:hover {
        background-color: #3367d6;
    }

    </style>

    <div class="landing-container">
        <div class="landing-title">👋 Selamat Datang di Aplikasi Internship</div>
        <div class="landing-subtitle">
            Eksplorasi data, visualisasi, dan manajemen proyek <br>
            dalam satu dashboard interaktif.
        </div>

    """
    return css