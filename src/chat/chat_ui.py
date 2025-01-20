import streamlit as st
from src.chat.chat_history import save_message, load_messages

def display_chat_ui():
    st.subheader("Groq Chat Streamlit App", divider="rainbow", anchor=False)

    # Display chat messages from history on app rerun
    messages = load_messages()
    for index, message in messages.iterrows():
        avatar = "🤖" if message['role'] == "assistant" else "👨‍💻"
        with st.chat_message(message['role'], avatar=avatar):
            st.markdown(message['content'])

    if prompt := st.chat_input("Enter your prompt here..."):
        save_message("user", prompt)
        with st.chat_message("user", avatar="👨‍💻"):
            st.markdown(prompt)

        # Fetch response from Groq API
        try:
            # Your Groq API call here
            full_response = "Assistant response"
            save_message("assistant", full_response)
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(full_response)
        except Exception as e:
            st.error(f"An error occurred: {e}", icon="🚨")