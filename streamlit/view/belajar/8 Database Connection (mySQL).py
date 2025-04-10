import streamlit as st

st.title("Database Connection (mySQL)")
st.text("Pada Page ini kita akan belajar mengenai cara membuat koneksi ke database khususnya ke mySQL\nBerikut adalah caranya :")

st.markdown("### 1.Install Library yang Dibutuhkan")
st.text('Buka terminal dan install library mysql-connector-python')
st.code('pip install mysql-connector-python', language='powershell')

st.markdown("### 2.Buat Directory Baru")
st.markdown('Tambahkan File File Berikut Di Project Kamu\n1. :gray-background[.streamlit/secrets.toml] untuk menyimpan kredensial database\n2. :gray-background[model/db_connection] untuk menyimpan method method untuk CRUD dengan database di directory project kamu')
col1, col2, col3 = st.columns([0.2,0.6,0.2])
with col1:
    pass
with col2:
    st.code('''
    streamlit/ 
        ├── __pycache__/ 
        ├── .streamlit/ 
        │       └── secrets.toml 
        ├── assets/ 
        ├── controller/ 
        ├── model/ 
        │       └── pychache 
        │       └── __init__.py 
        │       └── db_connection.py 
        ├── utils/ 
        ├── view/ 
        ├── config.py 
        ├── .gitignore 
        ├── main.py 
        └── pycache/''', language='powershell')
with col2:
    pass

st.markdown("### 3.Buat Kredensial Database")
st.markdown('Tambahkan Kredensial Database seperti nama tabel, username, password, dan lain-lain ke dalam :gray-background[.streamlit/secrets.toml] dan buatlah logika CRUD di dalam method method yang disimpan dalam :gray-background[model/db_connection]')
col1, col2 = st.columns(2)
with col1 :
    kol1, kol2, kol3= st.columns(3)
    with kol1:
        pass
    with kol2:
        st.markdown('<p style="width: 100%; background-color: rgb(28, 59, 89); text-align: center; border-radius: 4px; padding: 2px 4px;">.streamlit/secrets.toml</p>', unsafe_allow_html=True)    
    with kol3:
        pass
    st.code('''
    # .streamlit/secrets.toml
    
    # internship_RLO adalah Nama Koneksi Ke Database
    [connections.internship_RLO]
    dialect = "mysql"
    host = "localhost"
    port = 3306
    database = "pwebpr"
    username = "root"
    password = ""
    ''', language='toml')
    st.caption("File ini berisi identitas database yang akan digunakan, karena menggunakan mySQL + Laragon maka bisa tinggal copas saja kode itu dan tinggal ganti nama database dan nama koneksinya")
with col2 :
    col1, col2, col3= st.columns(3)
    with col1:
        pass
    with col2:
        st.markdown('<p style="width: 100%; background-color: rgb(28, 59, 89); text-align: center; border-radius: 4px; padding: 2px 4px;">model/db_connection.py</p>', unsafe_allow_html=True)    
    with col3:
        pass
    st.code('''
    import streamlit as st
    def get_connection():
        return st.connection('internship_RLO', type='sql')
    ''', language='python')
    st.caption("File ini berisi method yang berisi koneksi ke database di mana argumen pertama yaitu Intership RLO adalah nama koneksi ke database yang diinisialisasi di secret.toml")


st.markdown("### 4. Buat Model-Model Sesuai Dengan Kebutuhan Aplikasi")
st.markdown('Silahkan buat file file model yang akan berisi kode SQL ')
col1, col2, col3 = st.columns([0.2,0.6,0.2])
with col1:
    pass
with col2:
    st.code('''
    model/ 
        ├── model/ 
        │     └── __pychache__
        │     └── __init__.py 
        │     └── db_connection.py 
        │     └── account_model.py 
        │     └── contact_model.py 
        │     └── ....
            ''', language='bash')
with col2:
    pass