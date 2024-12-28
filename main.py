import streamlit as st
from langchain_core.prompts import ChatPromptTemplate

st.title("PlayGround")


with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key", key="chatbot_api_key", type="password"
    )
    