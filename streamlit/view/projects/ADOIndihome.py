import streamlit as st
import pandas as pd
from vega_datasets import data

col1, col2 = st.columns(2)
with col1 :
    source = pd.DataFrame(
        {
            "Kabupaten" : ['Lumajang', "Jember", "Banyuwangi", "Bondowoso", "Situbondo", "Probolinggo", "Kota Probolinggo"],
            "cd"        : [50, 85, 120, 160, 210, 150, 150],
            "populasi"  : [70, 105, 140, 180, 230, 170, 170]
        }
    )
    st.bar_chart(source, x="Kabupaten", y=["cd", "populasi"], horizontal=False, stack=True, color=["#F5868D", "#E30511"])
    st.bar_chart(source, x="variety", y="yield", color="site", horizontal=False)
with col2 :
    source = pd.DataFrame(
        {
            "Kabupaten" : ['Lumajang', "Jember", "Banyuwangi", "Bondowoso", "Situbondo", "Probolinggo", "Kota Probolinggo"],
            "cd"        : [50, 85, 120, 160, 210, 150, 150],
            "populasi"  : [70, 105, 140, 180, 230, 170, 170]
        }
    )
    st.bar_chart(source, x="Kabupaten", y=["cd", "populasi"], horizontal=False, stack=True, color=["#F5868D", "#E30511"])
    st.bar_chart(source, x="variety", y="yield", color="site", horizontal=False)

st.write(source)

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

st.dataframe(dataTable, hide_index=True)