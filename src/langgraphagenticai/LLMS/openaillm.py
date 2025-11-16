import os 
import streamlit as st

from langchain_openai import OpenAI

class OpenAILLM:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input

    def load_openai_llm(self):
        try:
            openai_api_key=self.user_controls_input.get("openai_api_key")
            selected_openai_model=self.user_controls_input.get("selected_openai_model")

            if openai_api_key=="" and os.environ.get("OPENAI_API_KEY") =='':
                st.error("Please provide a valid OpenAI API key.")
                
            llm=OpenAI(model_name=selected_openai_model,openai_api_key=openai_api_key)

        except Exception as e:
            raise ValueError(f"Failed to load OpenAI LLM due to: {e}")
        return llm
    
    
