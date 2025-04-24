import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)
with col1 :
    source = pd.DataFrame(
        {
            "Kabupaten" : ['Lumajang', "Jember", "Banyuwangi", "Bondowoso", "Situbondo", "Probolinggo", "Kota Probolinggo"],
            "cb"        : [50, 85, 120, 160, 210, 150, 150],
            "populasi"  : [70, 105, 140, 180, 230, 170, 170]
        }
    )
    st.bar_chart(source, x="Kabupaten", y=["cb", "populasi"], horizontal=False, stack=True, color=["#F5868D", "#E30511"])
with col2 :
    source = pd.DataFrame(
        {
            "Kabupaten" : ['Lumajang', "Jember", "Banyuwangi", "Bondowoso", "Situbondo", "Probolinggo", "Kota Probolinggo"],
            "FB Share REG"        : [50, 85, 120, 160, 210, 150, 150],
            "FB Share YOUTH"           : [70, 105, 140, 180, 230, 170, 170]
        }
    )
    st.bar_chart(source, x="Kabupaten", y=["FB Share REG", "FB Share YOUTH"], horizontal=False, stack=False, color=["#F5868D", "#E30511"])

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