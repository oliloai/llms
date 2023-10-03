import streamlit as st
from PIL import Image
import os

def init_styles():

    favicon = Image.open("favicoblue.png")

    st.set_page_config(page_title="Olilo Multi-LLM Querying System", page_icon=favicon, layout="wide")
    
    current_directory = os.getcwd()
    css_file_path = os.path.join(current_directory, "design", "style.css")


    with open(css_file_path) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    st.sidebar.image("logo.png", width=100)

def olilo_info():
    
    st.title("Olilo Multi-LLM Querying System")

    st.caption('This is  :violet[Olilo LLMS] _Beta_. Enter your promot and see the AI response from different LLMs :sunglasses:')

    st.caption("Olio helps businsses to find the best LLM suitable for their needs. We are building a platform to help you find the best LLM for your needs. \n\nThis is a beta version of our platform. We are working hard to improve it.")

    st.write("Developed by [Olilo AI](https://olilo.ai)")