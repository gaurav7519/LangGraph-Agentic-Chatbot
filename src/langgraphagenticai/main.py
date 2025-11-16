import streamlit as st
from src.langgraphagenticai.UI.streamlitui.loadui import loadstreamlitUI

def load_langgraph_agenticai_app():

    ui=loadstreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("faield to load user inputs from the UI.")
        return
    
    user_message = st.chat_input("enter your message here:")

    


