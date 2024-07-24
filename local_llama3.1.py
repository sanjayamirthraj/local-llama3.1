import streamlit as st
import ollama

st.title("Local Chat App")
st.caption("This app allows you to chat with an AI using local llama3 and RAG all locally run on your machine!")
st.caption("For any questions, contact Sanjay Amirthraj")

# Prompt the user for their message or question and context
context = st.text_area("Enter the context for your question", height=300)
prompt = st.text_input("Enter your message or question")

if prompt and context:
    # Call Ollama Llama3 model
    def ollama_llm(question, context):
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': formatted_prompt}])
        return response['message']['content']

    # Chat with the AI
    result = ollama_llm(prompt, context)
    st.write(result)

# Add a button to clear the input

if st.button("Submit"):
    prompt = ""
    context = ""
