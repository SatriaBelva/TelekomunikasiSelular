import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
import altair as alt

def graphCB_Populasi():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten" : get_Kabupaten_data(),
            "CB"        : get_CB_data(),
            "Populasi"  : get_Populasi_data(),
        }
    )

    dataPendidikan["CB"] = (
        dataPendidikan["CB"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
    dataPendidikan["Populasi"] = (
        dataPendidikan["Populasi"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars=["CB", "Populasi"], var_name="Kategori", value_name="Jumlah")

    chart = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=None),
        y=alt.Y("Jumlah:Q"),
        xOffset="Kategori:N",  # Ini penting untuk grouped bar
        color=alt.Color("Kategori:N", scale=alt.Scale(range=["#FFCDD0", "#F5868D"]), legend=alt.Legend(orient="bottom")),  # 👈 legend di bawah),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ]
    ).properties(height=550)

    st.altair_chart(chart, use_container_width=True)
    
