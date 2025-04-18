import streamlit as st

def get_pages() :
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
    Gmail_Auth      = st.Page("view/belajar/10 Gmail Authentication.py", title="Gmail Account Authentication", icon=":material/account_circle:")

    # === Projects Pages ===
    Populytics      = st.Page("view/projects/Populytics.py", title="Populytics", icon=":material/group:", default=True)
    Market_Radar    = st.Page("view/projects/Market Radar.py", title="Market Radar", icon=":material/shopping_cart:")
    EcoScope        = st.Page("view/projects/EcoScope.py", title="EcoScope", icon=":material/show_chart:")
    tes             = st.Page("view/projects/tes.py", title="tes", icon=":material/show_chart:")
    tes_lagi        = st.Page("view/projects/tes_lagi.py", title="tes_lagi", icon=":material/show_chart:")
    map             = st.Page("view/projects/map.py", title="map", icon=":material/show_chart:")

    return {
        "Project Internship RLO": [Populytics,Market_Radar,EcoScope,tes,tes_lagi,map]
        # "Belajar": [Penampungan,Data,Charts,Forms,Session_State,Callback,Layout,Fragment,DB_mySQL_Conn,DB_Gsheet_Conn,Gmail_Auth],
    }