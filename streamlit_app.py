import streamlit as st
from academic_assistant import ask_bot

# Initialize session state to store conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

st.title("Academic Assistant Chatbot")
st.write("Ask me anything about academic topics!")

# User input
user_input = st.text_input("Your question:", "")

if st.button("Submit"):
    if user_input:
        # Get bot response
        bot_response = ask_bot(user_input)
        
        # Add user input and bot response to conversation history
        st.session_state.conversation.append({"user": user_input, "bot": bot_response})

# Display conversation history
for i, msg in enumerate(st.session_state.conversation):
    st.write(f"You: {msg['user']}")
    st.write(f"Bot: {msg['bot']}")
