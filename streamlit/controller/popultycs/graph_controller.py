import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *

dataKecamatan = kecamatan_list()

def graphPendidikan(kecamatan):
    if kecamatan == "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                "Kecamatan"                                     : get_kecamatan_data()["nama"].tolist(),
                "Tidak/putus sekolah, belum tamat SD, tamat SD" : get_belum_sekolah_data()["Tidak/putus sekolah, belum tamat SD, tamat SD"].tolist(),
                "SLTP/SLTA"                                     : get_SLTPSLTA_data()["SLTP/SLTA"].tolist(),
                "D1/D2, D3, S1, S2, S3"                         : get_kuliah_data()["kuliah"].tolist()
            }
        )
        st.bar_chart(dataPendidikan, x="Kecamatan", y=["Tidak/putus sekolah, belum tamat SD, tamat SD", "SLTP/SLTA", "D1/D2, D3, S1, S2, S3"], horizontal=False, stack=True, color=["#FFCDD0", "#F5868D", "#E30511"], height=550)
    elif kecamatan != "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
f"Kelurahan di {kecamatan.capitalize()}"                        : get_kelurahan_data(kecamatan)["nama"].tolist(),
                "Tidak/putus sekolah, belum tamat SD, tamat SD" : get_belum_sekolah_data_by_kecamatan(kecamatan)["Tidak/putus sekolah, belum tamat SD, tamat SD"].tolist(),
                "SLTP/SLTA"                                     : get_SLTPSLTA_data_by_kecamatan(kecamatan)["SLTP/SLTA"].tolist(),
                "D1/D2, D3, S1, S2, S3"                         : get_kuliah_data_by_kecamatan(kecamatan)["kuliah"].tolist()
            }
        )
        st.bar_chart(dataPendidikan, x=f"Kelurahan di {kecamatan.capitalize()}", y=["Tidak/putus sekolah, belum tamat SD, tamat SD", "SLTP/SLTA", "D1/D2, D3, S1, S2, S3"], horizontal=False, stack=True, color=["#FFCDD0", "#F5868D", "#E30511"], height=550)

def graphPekerjaan(kecamatan):
    dataPekerjaan = pd.DataFrame(
        {
            "Kecamatan"     : dataKecamatan,
            "Tidak Bekerja" : np.random.randint(0, 12, size=len(dataKecamatan)),
            "Wiraswasta"    : np.random.randint(0, 750, size=len(dataKecamatan)),
            "Guru"          : np.random.randint(0, 750, size=len(dataKecamatan))
        }
    )
    st.bar_chart(dataPekerjaan, x="Kecamatan", y=["Tidak Bekerja", "Wiraswasta", "Guru"], horizontal=False, stack=True, color=["#FFCDD0", "#F5868D", "#E30511"], height=550)

def graphJumlahPenduduk(kecamatan):
    dataJumlahPenduduk = pd.DataFrame(
        {
            "Kecamatan"     : dataKecamatan,
            "Tidak Bekerja" : np.random.randint(0, 750, size=len(dataKecamatan)),
            "Wiraswasta"    : np.random.randint(0, 750, size=len(dataKecamatan)),
            "Guru"          : np.random.randint(0, 750, size=len(dataKecamatan))
        }
    )
    st.bar_chart(dataJumlahPenduduk, x="Kecamatan", y=["Tidak Bekerja", "Wiraswasta", "Guru"], horizontal=False, stack=True, color=["#FFCDD0", "#F5868D", "#E30511"], height=550)

def graphJumlahKK(kecamatan):
    dataJumlahKK = pd.DataFrame(
        {
            "Kecamatan"     : dataKecamatan,
            "Tidak Bekerja" : np.random.randint(0, 750, size=len(dataKecamatan)),
            "Wiraswasta"    : np.random.randint(0, 750, size=len(dataKecamatan)),
            "Guru"          : np.random.randint(0, 750, size=len(dataKecamatan))
        }
    )
    st.bar_chart(dataJumlahKK, x="Kecamatan", y=["Tidak Bekerja", "Wiraswasta", "Guru"], horizontal=False, stack=True, color=["#FFCDD0", "#F5868D", "#E30511"], height=550)

