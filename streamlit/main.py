import streamlit as st
import pandas as pd
import numpy as np
from utils import clearTerminal, testingCheckbox, pilihanDivisi, organizationSelection

st.markdown("""
    <style>
        #MainMenu { visibility: hidden; }
        @keyframes rgbHeader {
            0% { background-color: #FE00FE; }
            25% { background-color: #7F78FF; }
            50% { background-color: #01A5F8; }
            75% { background-color: #00E0FF; }
            100% { background-color: #151719; }
        }

        .stAppHeader {
            animation: rgbHeader 5s infinite;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Ini Adalah Project Telkomsel")
st.header("Selamat Datang di Project Telkomsel")
st.subheader("Ini akan menjadi subheader")
st.text("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eveniet aperiam explicabo quae veritatis sequi illum voluptates adipisci eius vel maxime laudantium cumque molestias odio, obcaecati aut rerum. Quos, at reiciendis.")

st.markdown("1. **Satria Belva Nararya** -> [@satriabelva](https://www.instagram.com/satriabelva/) \n"
            "2. *Safila Elsa Vavilya* -> [@safilael](https://www.instagram.com/safilael/)\n"
            "3. Felisita Dian Puspitasari -> [@_dian1234](https://www.instagram.com/_dian1234/)")
st.markdown("- [x] Write the press release")
st.markdown("---")

json = {
    "nama" : ['Satria Belva Nararya', 'Safila Elsa Vavilya', 'Felisita Dian Puspitasari'],
    'umur' : [22, 20, 20],
    'asal divisi' : ['Kaderisasi', 'Litbang', 'Humas']
}
st.json(json)
code = '''
def functionBejo(tes):
    return f'Halo Nama Saya Adalah {tes}'
'''
st.code(code, language='python')
st.write({
    "nama" : "Satria Belva Nararya",
    "Organisasi" : "Himpunan Mahasiswa Sistem Informasi",
    "Skill" : {
        "Bahasa Pemrograman" : ["Python", "Java", "C++"],
        "Bahasa" : ["Indonesia", "Inggris"],
        "Database" : ["MySQL", "MongoDB"]
    }
})

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data, use_container_width=True, x_label='Random X Label', y_label='Random Y Label') 
st.metric(label="Suhu Ruangan Sekretarian HIMASIF", value="20ᴼ Celcius", delta='-5ᴼ Celcius', delta_color='inverse', border=True)
st.metric(label="Jumlah Uang Kas HIMASIF 2024/2025", value=f'Rp2.000.000', delta='Rp500.000', delta_color='normal', border=False, label_visibility='visible', help='Metric Ini berisi informasi mengenai Jumlah uang kas HIMASIF periode 2024/2025 beserta selisihnya dari bulan lalu') 

himasif = pd.DataFrame({
    'Kaderisasi' : ['Taqiyyah', 'Jeje', 'Shofia', 'Robbi', 'Juki', 'Nadhira', 'Nisa', 'Nabil', 'Edryan'],
    'Litbang'    : ['Bagus', 'Mada', 'Ica', 'Brilli', 'Rendy', 'Jasmin', 'Yesi', 'Jopay', None],
    'Humas'      : ['Ila', 'Rhenata', 'Hilmi', 'Raffy', 'Chelsea', 'Vivi', 'Muttaqin', None, None],
    'Mediatek'   : ['Muza', 'Jo', 'Dini', 'Rahardan', 'Tyo', 'Nabila', 'Almas', 'Rafi', 'Oktavia'],
    'PSDM'       : ['Eva', 'Dewi', 'Nathan', 'Felix', 'Ziza', 'Viola', 'Derrick', 'Iklina', 'Kanina']
})

st.write(himasif)
st.table(himasif)
st.dataframe(himasif)

st.image("assets/tes.png",width=400, caption="Ini Adalah Logo HIMASIF", use_container_width=True)
st.video("assets/VID-20241025-WA0013.mp4")

st.checkbox(label='Ini adalah checkbox 1', help='This Checkbox will do something in your terminal', value=True, on_change=testingCheckbox, key='tes')
st.checkbox(label='Ini adalah checkbox 2', help='This Clear The Terminal', value=False, on_change=clearTerminal, key='clearTerminal')

st.radio(
    label='Silahkan Pilih Salah Satu Divisi Di Bawah Ini', 
    options=('Kaderisasi', 'Litbang', 'Humas', 'PSDM', 'Mediatek'), 
    captions=('Pengkaderan anggota', 'Penelitian & Pengembangan', 'Hubungan Masyarakat', 'Pengembangan Sumber Daya Mahasiswa', 'Media & Teknologi'),
    help='Choose One of This Divisions Below',
    key='divisi',
    on_change=pilihanDivisi,
    index=3
)

st.selectbox(
    label='Silahkan Pilih Salah Satu Organisasi Di Bawah Ini', 
    options=('BEM', 'HIMATIF', 'HMIF', 'HIMASIF', 'BPM'), 
    placeholder='"Choose an option',
    help='Choose One of This Organization Below',
    on_change=organizationSelection,
    key='organisasi',
    label_visibility='visible',
    index=3
)

st.button(
    label='Click This Button To Clear The Terminal',
    on_click=clearTerminal,
    key='clearTerminalButton',
    icon="🗑️",
    help='Click This Button To Automaticly Clear Your Terminal',
    use_container_width=True,
    type='secondary',
)