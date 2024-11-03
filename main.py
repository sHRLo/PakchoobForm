import streamlit as st
from Pages.Operator import operator_screen
from Pages.Technisian import technisian_screen

# # Database connection
# conn = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'SERVER=10.0.1.7\\bi;'
#     'DATABASE=PM;'
#     'UID=Reza;'
#     'PWD=Re@123456'
# )
# cursor = conn.cursor()

# Function to authenticate user
# def authenticate(username, password):
#     cursor.execute('SELECT username, password, role FROM dbo.Login WHERE username = ? AND password = ?',
#     (username, password))
#     user = cursor.fetchone()
#     if user:
#         return user[2]  # Return the role of the user
#     return None

def login_page():
    st.markdown("<h1 style='text-align: center; color: white;'>Login Page</h1>", unsafe_allow_html=True)
    # Login form
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login',key='login_btn')
    if login_button:
        role = authenticate(username, password)
        if role:
            st.success(f'Welcome {username}!')
            st.session_state.role = role
            st.rerun()
        else:
            st.error('Invalid username or password')

# Define the pages
def admin_page():
    st.title('Admin Page')
    st.write('This is the admin page.')
    if st.button('Logout',key='logout_btn_admin'):
        st.session_state.role = None
        st.rerun()

def operator_page():
    st.title('Operator Page')
    operator_screen()
    if st.button('Logout',key='logout_btn_operator'):
        st.session_state.role = None
        st.rerun()

def technician_page():
    st.title('Technician Page')
    technisian_screen()
    if st.button('Logout',key='logout_btn_technician'):
        st.session_state.role = None
        st.rerun()


# Initialize session state
if 'role' not in st.session_state:
    login_page()
    st.session_state.role = None

# Streamlit app
if st.session_state.role is None:

    if st.session_state.role == 'admin':
        admin_page()
    elif st.session_state.role == 'operator':
        operator_page()
    elif st.session_state.role == 'technician':
        technician_page()
