import streamlit as st
import pandas as pd
from controller import *

col1, col2 = st.columns(2)
with col1 :
    graphCB_Populasi()
with col2 :
    graphCB_Populasi()

dataTable = pd.DataFrame(
    {
        "Nomor" : ['1', "2", "3", "4", "5", "6", "7"],
        "Kabupaten" : ['Lumajang', "Jember", "Banyuwangi", "Bondowoso", "Situbondo", "Probolinggo", "Kota Probolinggo"],
        "Total Household" : [230678, 230678, 230678, 230678, 230678, 230678, 230678],
        "LIS Aktif" : [230678, 230678, 230678, 230678, 230678, 230678, 230678],
        "WiFi Share" : [230678, 230678, 230678, 230678, 230678, 230678, 230678],
        "Total ODP" : [4905, 4905, 4905, 4905, 4905, 4905, 4905],
        "PORT Avail" : [22704, 22704, 22704, 22704, 22704, 22704, 22704],
        "Total PORT" : [44453, 44453, 44453, 44453, 44453, 44453, 44453],
    }
)
get_CB_data()
st.dataframe(dataTable, hide_index=True)