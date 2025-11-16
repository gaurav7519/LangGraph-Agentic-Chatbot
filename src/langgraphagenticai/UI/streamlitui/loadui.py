import streamlit as st
import os

from src.langgraphagenticai.UI.uiconfigfile import Config 

class loadstreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:

            llm_options = self.config.get_llm_options()
            usercase_options = self.config.get_usecase_options()

            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['selected_llm'] == "OpenAI":

                model_options = self.config.get_openai_model_options()
                self.user_controls['selected_openai_model'] = st.selectbox("Select Model", model_options)
                self.user_controls['openai_api_key'] = st.session_state.get('openai_api_key', st.text_input("Enter OpenAI API Key", type="password"))

                if not self.user_controls['openai_api_key']:
                    st.warning("Please enter your OpenAI API key to proceed.")

            
            self.user_controls['selected_usecase'] = st.selectbox("Select Usecase", usercase_options)

        return self.user_controls




