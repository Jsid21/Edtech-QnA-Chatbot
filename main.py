import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title('EdTech QnA Chatbot')

st.write('Welcome to the EdTech QnA Chatbot! Please enter your question below and I will do my best to help you.')

question = st.text_input('Enter your question here:')

btn = st.button("submit")

if(btn):
    st.write("Answer is ....")

    chain = get_qa_chain()
    response = chain.invoke({"query": question})
    st.write(response["result"])