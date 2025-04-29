import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
from controller.popultycs.Popultycsmap_controller import kecamatan_list

dataKecamatan = kecamatan_list()

def table() :
    data = pd.DataFrame(
        {   
            'Kecamatan'     : dataKecamatan,
            'Penduduk'      : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'KartuKeluarga' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
        }
    )

    rows_per_page = 10
    total_pages = len(data) // rows_per_page + (1 if len(data) % rows_per_page > 0 else 0)

    if 'page' not in st.session_state:
        st.session_state.page = 1

    start_idx = (st.session_state.page - 1) * rows_per_page
    end_idx = start_idx + rows_per_page
    current_data = data.iloc[start_idx:end_idx]

    st.dataframe(current_data, use_container_width=True, hide_index=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        if st.button("⬅️ Prev", key="prev_button", use_container_width=True, ) and st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()
    with col3:
        st.markdown(
            f"<div style='text-align: center; font-weight: normal; padding-top:6px;'>Page {st.session_state.page} of {total_pages}</div>",
            unsafe_allow_html=True
        )   
    with col4:
        if st.button("Next ➡️", key="next_button", use_container_width=True) and st.session_state.page < total_pages:
            st.session_state.page += 1
            st.rerun()
    with col5:
        pass

def table2() :
    data = pd.DataFrame(
        {   
            'Kecamatan'     : dataKecamatan,
            'Sekolah Tinggi'      : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'Sekolah Menengah' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'Tidak/Belum Sekolah & Tamat SD' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'Tidak/Belum Bekerja' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'Penghasilan Stabil' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'Penghasilan Tidak Stabil' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'Jumlah Penduduk' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
            'Jumlah KK' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
        }
    )

    st.dataframe(data,use_container_width=True, hide_index=True)