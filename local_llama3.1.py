import streamlit as st
import ollama

st.title("Local Chat App")
st.caption("This app allows you to chat with an AI using local llama3 and RAG all locally run on your machine!")
st.caption("For any questions, contact Sanjay Amirthraj")

context = st.text_area("Enter the context for your question", height=300)
prompt = st.text_input("Enter your message or question")

if prompt:
    def ollama_llm(question, context):
        if not context ==  "":
            context = "Help the user to the most of your abilities"
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': formatted_prompt}])
        return response['message']['content']

    result = ollama_llm(prompt, context)
    st.write(result)


if st.button("Submit"):
    prompt = ""
    context = ""

import datetime
st.write("Chat time: ", datetime.datetime.now())




