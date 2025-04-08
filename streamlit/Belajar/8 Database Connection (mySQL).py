import streamlit as st
# st.set_page_config(page_title='Data', page_icon='🔥', layout='wide', menu_items={"Get help": 'mailto:satriabelvanararyan@gmail.com', 'About' : 'Made by Satria Belva Nararya'})

st.title("Database Connection (mySQL)")
st.text("Pada Page ini kita akan belajar mengenai cara membuat koneksi ke database khususnya ke mySQL\nBerikut adalah caranya :")

st.markdown("### 1.Install Library yang Dibutuhkan")
st.text('Buka terminal dan install library mysql-connector-python')
st.code('pip install mysql-connector-python', language='powershell')

st.markdown("### 2.Buat Directory Baru")
st.markdown('Tambahkan :gray-background[.streamlit/secrets.toml], :gray-background[utils/database.py], :gray-background[.gitignore] di directory project kamu')
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

st.markdown("### 3.Buat Kredensial Database")
st.markdown('Tambahkan Kredensial Database seperti nama tabel, username, password, dan lain-lain ke dalam :gray-background[.streamlit/secrets.toml]')
col1, col2 = st.columns(2)
with col1 :
    st.markdown(':blue-background[.streamlit/secrets.toml]')
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
with col2 :
    st.markdown(':blue-background[.]')
    st.code('''
    # .streamlit/secrets.toml
            
    [connections.internship_RLO] 
    dialect = "mysql"
    host = "localhost"
    port = 3306
    database = "pwebpr"
    username = "root"
    password = ""
    ''', language='toml')

