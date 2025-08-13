from openai import OpenAI 
import streamlit as st 

client = OpenAI()
# print(response.output_text)

st.title("GPT-5 Chat")

user_msg = st.text_input("Your message")

if st.button("Send"):
    with st.spinner("Thinking..."):
        response = client.responses.create(
            model= "gpt-5",
            input=user_msg
        )
        st.write("Response: ", response.output_text)
