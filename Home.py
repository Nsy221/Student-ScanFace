import streamlit as st
import face_rec

def show_home():


    st.header('Welcome to the Student Attendance System using Face Recognition')
    st.subheader('A real-time solution for attendance tracking')

    st.markdown("""
        This system utilizes face recognition technology to provide a convenient and secure
        way to track student attendance.
    """)

    st.spinner("Loading Models and Connecting to Redis db ...")
        

    st.success('Model loaded successfully')
    st.success('Redis db successfully connected')

    
if __name__ == "__home__":
    show_home()