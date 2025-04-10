import streamlit as st
from model import *
from utils import *

def login():
    user = st.experimental_user
    email = get_email_data()
    authenticated_email = []
    for i in email.itertuples():
            authenticated_email.append(i.email)

    if not user.is_logged_in:
        st.markdown(hide_sidebar(), unsafe_allow_html=True)
        st.markdown(landing_page_style(), unsafe_allow_html=True)
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.button("🔐 Login dengan Google", on_click=lambda: st.login("google"), key="login_button")
        st.markdown("</div></div>", unsafe_allow_html=True)
        return False
    else:
        if user.email not in authenticated_email:
            st.error("⚠️ Maaf, email kamu tidak memiliki akses ke aplikasi ini.")
            st.button("Kembali ke Landing Page", on_click=lambda: st.logout())
            st.markdown(hide_sidebar(), unsafe_allow_html=True)
            return False
        else : 
            st.sidebar.success(f"Hai, {user.name} 👋")
            if st.sidebar.button("Logout"):
                st.logout()
            return True