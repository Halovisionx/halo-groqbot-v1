import streamlit as st
from src.models.user import User
from src.database.db import get_db

def register_user(username, password):
    db = get_db()
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

def login_user(username, password):
    db = get_db()
    user = db.session.query(User).filter_by(username=username, password=password).first()
    return user

def display_auth_ui():
    st.subheader("User Authentication", divider="rainbow", anchor=False)

    if 'user' not in st.session_state:
        st.session_state.user = None

    if st.session_state.user is None:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Register"):
            register_user(username, password)
            st.success("User registered successfully!")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state.user = user
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")
    else:
        st.write(f"Welcome, {st.session_state.user.username}!")
        if st.button("Logout"):
            st.session_state.user = None