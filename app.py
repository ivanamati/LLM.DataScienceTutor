import streamlit as st
#from langchain.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
#from langchain_core import prompts
from langchain.chains import LLMChain

OPENAI_API_KEY = "..."

st.title('Data Scientist LLM Tutor')

openai_api_key = st.sidebar.text_input('OPENAI_API_KEY')

def generate_response(input_text):
    """ this function generates response by using the ChatGPT / Openai API key"""
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    
    # PROMPT
    # template is like SystemMessage from LLM, and inside of it we can define the variable for users input (for example)
    template = """
    You are an expert data scientist with an expertise in building deep learning models and overall understanding Data Science and its rules. 
    You are also a great mentor and teacher of the data science concepts and when you get the request from the user you help him like a great teacher to learn those concepts.
    Explain the asked concept of {concept} in a couple of lines later make a new line and give an example usecase in natural language processing and/or Data science where is {concept} often applied.
    """
    prompt = PromptTemplate(
        input_variables=["concept"], # this is users input 
        template=template,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    # running the chain only specifying one input variable (before it was .run, now is used .invoke which gives a dictionary)
    output = chain.invoke(input_text)
    print(output['text'])

    #st.info(chain_one.invoke(input_text))
    st.info(output['text'])


with st.form('my_form'):
  text = st.text_area('Enter text:')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'): 
    generate_response(text)