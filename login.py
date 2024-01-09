# login.py
import streamlit as st
import streamlit_authenticator as stauth
from redis_utils import validate_credentials
from Home import show_home
from History import history
from RealTimePrediction import scanFace

def login():
    if "user_key" not in st.session_state:
        st.session_state.user_key = None

    with st.form(key='login', clear_on_submit=True):
        st.subheader(':green[Login]')
        email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
        password = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')

        if email and password:
            user_key = validate_credentials(email, password)
            if user_key:
                st.session_state.user_key = user_key
                st.session_state.authentication_status = True  # Set authentication status to True

            else:
                st.warning('Invalid email or password')

        btn_login = st.form_submit_button('Login')

        
