import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import os
from matplotlib import pyplot as plt
from utils import clearTerminal, testingCheckbox, pilihanDivisi, organizationSelection, previewUploadedFile, usernameAndPassword, registration

st.set_page_config(layout='wide', menu_items={"Get help": 'mailto:satriabelvanararyan@gmail.com', 'About' : 'Made by Satria Belva Nararya'})

Penampungan     = st.Page("Belajar/0 Penampungan.py", title="Dashboard", icon=":material/dashboard:")
Data            = st.Page("Belajar/1 Data.py", title="Data Component", icon=":material/folder_open:")
Charts          = st.Page("Belajar/2 Charts.py", title="Charts Component", icon=":material/signal_cellular_alt:")
Forms           = st.Page("Belajar/3 Forms.py", title="Form Component", icon=":material/forms_add_on:")
Session_State   = st.Page("Belajar/4 Session State.py", title="Session State", icon=":material/cookie:")
Callback        = st.Page("Belajar/5 Callback.py", title="Callback", icon=":material/function:")
Layout          = st.Page("Belajar/6 Layout.py", title="Layout", icon=":material/dashboard:")
Fragment        = st.Page("Belajar/7 Fragment.py", title="Fragment", icon=":material/segment:")
DB_mySQL_Conn   = st.Page("Belajar/8 Database Connection (mySQL).py", title="Database Connection (mySQL)", icon=":material/database:")
DB_Gsheet_Conn  = st.Page("Belajar/9 Database Connection (Google Sheet).py", title="Database Connection (Google Sheet)", icon=":material/docs:")

Populytics      = st.Page("Projects/Populytics.py", title="Populytics", icon=":material/group:", default=True)
Market_Radar    = st.Page("Projects/Market Radar.py", title="Market Radar", icon=":material/shopping_cart:")
EcoScope        = st.Page("Projects/EcoScope.py", title="EcoScope", icon=":material/show_chart:")

pg = st.navigation({
    "Project Internship RLO": [Populytics, Market_Radar, EcoScope],
    "Belajar": [Penampungan, Data, Charts, Forms, Session_State, Callback, Layout, Fragment, DB_mySQL_Conn, DB_Gsheet_Conn],
})
pg.run()

















# st.markdown("""
#     <style>
#         #MainMenu { visibility: hidden; }
#         @keyframes rgbHeader {
#             0% { background-color: #FE00FE; }
#             25% { background-color: #7F78FF; }
#             50% { background-color: #01A5F8; }
#             75% { background-color: #00E0FF; }
#             100% { background-color: #151719; }
#         }

#         .stAppHeader {
#             animation: rgbHeader 5s infinite;
#         }
#     </style>
# """, unsafe_allow_html=True)