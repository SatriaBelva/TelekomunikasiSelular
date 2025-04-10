import streamlit as st

st.set_page_config(
    layout='wide',
    menu_items={
        "Get help": 'mailto:satriabelvanararyan@gmail.com',
        'About': 'Made by Satria Belva Nararya'
    }
)

# === Belajar Pages ===
Penampungan     = st.Page("view/belajar/0 Penampungan.py", title="Dashboard", icon=":material/dashboard:")
Data            = st.Page("view/belajar/1 Data.py", title="Data Component", icon=":material/folder_open:")
Charts          = st.Page("view/belajar/2 Charts.py", title="Charts Component", icon=":material/signal_cellular_alt:")
Forms           = st.Page("view/belajar/3 Forms.py", title="Form Component", icon=":material/forms_add_on:")
Session_State   = st.Page("view/belajar/4 Session State.py", title="Session State", icon=":material/cookie:")
Callback        = st.Page("view/belajar/5 Callback.py", title="Callback", icon=":material/function:")
Layout          = st.Page("view/belajar/6 Layout.py", title="Layout", icon=":material/dashboard:")
Fragment        = st.Page("view/belajar/7 Fragment.py", title="Fragment", icon=":material/segment:")
DB_mySQL_Conn   = st.Page("view/belajar/8 Database Connection (mySQL).py", title="Database Connection (mySQL)", icon=":material/database:")
DB_Gsheet_Conn  = st.Page("view/belajar/9 Database Connection (Google Sheet).py", title="Database Connection (Google Sheet)", icon=":material/docs:")

# === Projects Pages ===
Populytics      = st.Page("view/projects/Populytics.py", title="Populytics", icon=":material/group:", default=True)
Market_Radar    = st.Page("view/projects/Market Radar.py", title="Market Radar", icon=":material/shopping_cart:")
EcoScope        = st.Page("view/projects/EcoScope.py", title="EcoScope", icon=":material/show_chart:")

# === Navigation ===
pg = st.navigation({
    "Project Internship RLO": [
        Populytics,
        Market_Radar,
        EcoScope
    ],
    "Belajar": [
        Penampungan,
        Data,
        Charts,
        Forms,
        Session_State,
        Callback,
        Layout,
        Fragment,
        DB_mySQL_Conn,
        DB_Gsheet_Conn
    ],
})

pg.run()
