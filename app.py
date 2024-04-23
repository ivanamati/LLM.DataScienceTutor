import streamlit as st
#from langchain.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
#from langchain_core import prompts
from langchain.chains import LLMChain
import langchain_chains
OPENAI_API_KEY = "..."

st.title('Data Scientist LLM Tutor')

openai_api_key = st.sidebar.text_input('OPENAI_API_KEY')

with st.form('my_form'):
  text = st.text_area('Enter text:')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'): 
    response = langchain_chains.generate_response(text, openai_api_key)
    st.info(response)
