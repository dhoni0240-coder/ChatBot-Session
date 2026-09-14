import streamlit as st
from ollama import chat

st.title("AI ChatBot")

#creating chat
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#Get new messages
user_message = st.chat_input("Type your message here...")

if user_message:
    #Add user message to history
    st.session_state.messages.append({
        "role" : "user",
        "content" : user_message
    })

    #Display user message
    with st.chat_message("user"):
        st.write(user_message)

        #Temporary AI response
        response = chat(
            model = "llama3.2:1b",
            messages = st.session_state.messages
        )
        ai_response = response.message.content

        #Add AI response to history
        st.session_state.messages.append({
            "role" : "assistant",
            "content" : ai_response
        })

        #Display AI response
        with st.chat_message("assistant"):
            st.write(ai_response)