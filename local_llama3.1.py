import streamlit as st
import ollama

st.title("Local Chat App")
st.caption("This app allows you to chat with an AI using local llama3 and RAG all locally run on your machine!")
st.caption("For any questions, contact Sanjay Amirthraj")

prompt = st.text_input("Enter your message or question")
if prompt:
    def ollama_llm(question, context):
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': formatted_prompt}])
        return response['message']['content']

    result = ollama_llm(prompt, "")
    st.write(result)

if st.button("Submit"):
    prompt = ""
    st.write("Message submitted!")
