import streamlit as st
import os as os

def DisplayYourName(yourName):
    print(f'ini adalah namamu : {yourName}')

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')  

name = st.text_input(
    label="Enter your name",
    help='Masukkan nama'
)

submit = st.button(label='SUBMIT')
if submit :
    option = st.checkbox(label='Want To Display Your Name?', on_change=DisplayYourName, args=(name,))

st.button(
    label='Hapus Terminal',
    key='clearTerminal',
    help='Hapus Terminal',
    on_click=clearTerminal,
    use_container_width=True,
    type='primary'
)

text = '🔥'
if 'click' not in st.session_state : # Creating Session State
    st.session_state.click = False
else : # Check the session state and check any other logic
    if st.session_state.click == False :
        text = "❤️"
        st.session_state.click = True
    else : 
        text = '🔥'
        st.session_state.click = False

st.button(label=text)
