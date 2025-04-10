import streamlit as st

st.title("Database Connection (mySQL)")
st.text("Pada Page ini kita akan belajar mengenai cara membuat koneksi ke database khususnya ke mySQL\nBerikut adalah caranya :")

st.markdown("### 1.Install Library yang Dibutuhkan")
st.text('Buka terminal dan install library mysql-connector-python')
st.code('pip install mysql-connector-python', language='powershell')

st.markdown("### 2.Buat Directory Baru")
st.markdown('Tambahkan File File Berikut Di Project Kamu\n1. :gray-background[.streamlit/secrets.toml] untuk menyimpan kredensial database\n2. :gray-background[utils/database.py] untuk menyimpan method method untuk CRUD dengan database di directory project kamu')
col1, col2, col3 = st.columns([0.2,0.6,0.2])
with col1:
    pass
with col2:
    st.code('''
    streamlit/ 
        ├── .gitignore 
        ├── .streamlit/ 
        │       └── secrets.toml 
        ├── assets/ 
        ├── Belajar/ 
        ├── pages/ 
        ├── Projects/ 
        ├── utils/ 
        │       └── pychache 
        │       └── __init__.py 
        │       └── function.py 
        │       └── database.py 
        ├── index.html 
        ├── config.py 
        ├── main.py 
        └── pycache/''', language='powershell')
with col2:
    pass

st.markdown("### 3.Buat Kredensial Database")
st.markdown('Tambahkan Kredensial Database seperti nama tabel, username, password, dan lain-lain ke dalam :gray-background[.streamlit/secrets.toml] dan buatlah logika CRUD di dalam method method yang disimpan dalam :gray-background[utils/database.py]')
col1, col2 = st.columns(2)
with col1 :
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
    kol1, kol2, kol3= st.columns(3)
    with kol1:
        pass
    with kol2:
        st.markdown('<p style="width: 100%; background-color: rgb(28, 59, 89); text-align: center; border-radius: 4px; padding: 2px 4px;">.streamlit/secrets.toml</p>', unsafe_allow_html=True)    
    with kol3:
        pass
with col2 :
    st.code('''
    import streamlit as st
    conn = st.connection('internship_RLO', type='sql')

    def get_akun_data():
        akun = conn.query('SELECT email, password FROM akun;', ttl=600)
        return akun

    def get_kontak_data():
        kontak = conn.query('SELECT * FROM kontak;', ttl=600)
        return kontak

    ''', language='python')
    col1, col2, col3= st.columns(3)
    with col1:
        pass
    with col2:
        st.markdown('<p style="width: 100%; background-color: rgb(28, 59, 89); text-align: center; border-radius: 4px; padding: 2px 4px;">utils/database.py</p>', unsafe_allow_html=True)    
    with col3:
        pass

