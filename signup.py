# signup.py
import streamlit as st
from redis_utils import insert_user
import streamlit_authenticator as stauth

def signup():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
        username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
        password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
        password2 = st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')

        if email and username and password1 and password2:
            if password1 == password2:
                # Hash the password before inserting it into the database
                hashed_password = stauth.Hasher([password1]).generate()[0]
                user_key = insert_user(email, username, hashed_password)
                st.balloons()
                st.success('Account created successfully!')
                
            else:
                st.warning('Passwords do not match')

        btn_signup = st.form_submit_button('Sign Up')
