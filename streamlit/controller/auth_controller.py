import streamlit as st
from model import *
from utils import *

# Fungsi untuk ambil data user dari session login
def get_current_user():
    return st.experimental_user

# Fungsi untuk ambil daftar email yang diizinkan dari database
def get_allowed_emails():
    email_data = get_email_data()
    return [row.email for row in email_data.itertuples()]

# Fungsi untuk mengecek apakah email user termasuk dalam daftar yang diizinkan
def is_email_allowed(email: str) -> bool:
    allowed_emails = get_allowed_emails()
    return email in allowed_emails

# Komponen UI untuk login
def render_login_page():
    # st.markdown(landing_page_style(), unsafe_allow_html=True)
    # st.markdown(landing_page(), unsafe_allow_html=True)
    tes_landing()
    st.markdown(hide_tools(), unsafe_allow_html=True)
    st.button("🔐 Login dengan Google",use_container_width=True, on_click=lambda: st.login("google"), key="login_button")
    st.markdown("</div></div>", unsafe_allow_html=True)

# Komponen UI untuk user yang tidak diizinkan
def render_unauthorized_page():
    st.error("⚠️ Maaf, email kamu tidak memiliki akses ke aplikasi ini.")
    st.button("Kembali ke Landing Page", on_click=lambda: st.logout())
    st.markdown(hide_sidebar(), unsafe_allow_html=True)

# Komponen greeting dan logout sidebar
def render_sidebar_greeting(user):
    st.sidebar.success(f"Hai, {user.name} 👋")
    if st.sidebar.button("Logout"):
        st.logout()



























# def login():
#     user = st.experimental_user
#     email = get_email_data()
#     authenticated_email = []
#     for i in email.itertuples():
#             authenticated_email.append(i.email)

#     if not user.is_logged_in:
#         st.markdown(landing_page_style(), unsafe_allow_html=True)
#         st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
#         st.button("🔐 Login dengan Google", on_click=lambda: st.login("google"), key="login_button")
#         st.markdown("</div></div>", unsafe_allow_html=True)
#         return False
#     else:
#         if user.email not in authenticated_email:
#             st.error("⚠️ Maaf, email kamu tidak memiliki akses ke aplikasi ini.")
#             st.button("Kembali ke Landing Page", on_click=lambda: st.logout())
#             st.markdown(hide_sidebar(), unsafe_allow_html=True)
#             return False
#         else : 
#             st.sidebar.success(f"Hai, {user.name} 👋")
#             if st.sidebar.button("Logout"):
#                 st.logout()
#             return True