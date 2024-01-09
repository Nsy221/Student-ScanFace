import streamlit as st
import streamlit_authenticator as stauth
from Home import show_home
from History import history
from RealTimePrediction import scanFace
from login import login
from signup import signup

page_bg_img = """
<style>
[data-testid= "stSidebar"] {
background: radial-gradient(circle at 81% 115%,rgba(176, 238, 238, 0.83), rgba(189, 176, 238, 0.89))
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}


</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Center-align the title using HTML
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Welcome to Scan Face</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Display the logo
#st.image("UMPSA.jpg", width=250)
# st.markdown(
#     """
#     <div style="display: flex; justify-content: center; align-items: center;">
#         <img src="UMPSA.jpg" alt="Logo" width="250"/>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
    
# # You can specify the image path here
# image_path = 'UMPSA.jpg'

# # Display the image
# st.image(image_path, caption='Sample Image', use_column_width=200)

# Create a session state to manage user authentication state
session_state = st.session_state

# Check if the user is authenticated
if not session_state.get("authentication_status", False):
    login_form_container = st.subheader(":green[Login]")
    login()

    # Check if the user is authenticated after login form submission
    if session_state.get("authentication_status", False):
        # Remove the login form from display
        login_form_container.empty()

# If authenticated, display welcome message and navigation
if session_state.get("authentication_status", False):
    st.sidebar.subheader('Welcome to ScanFace System')
    
    # Add navigation to other pages in the sidebar
    selected_page = st.sidebar.radio("Navigation", ["Home", "Scan Face", "History"])
    
    if selected_page == "Home":
        show_home()
    elif selected_page == "Scan Face":
        scanFace()
    elif selected_page == "History":
        history()

    # Logout button
    if st.sidebar.button("Log Out"):
        session_state.user_key = None
        session_state.authentication_status = False

# Display signup form
if not session_state.get("authentication_status", False):
    signup_form_container = st.subheader(":green[Sign Up]")
    signup()

    # Check if the user has signed up successfully
    if session_state.get("signup_status", False):
        # Remove the signup form from display
        signup_form_container.empty()
