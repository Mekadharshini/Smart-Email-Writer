import streamlit as st
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("Smart Email Writer")
prompt = st.text_input("Write Email topic or Email content")
if st.button("Submit"):
    res = model.generate_content(
        prompt + """
        You are an email writing expert.
        Generate a professional email with a subject and a quick reply.
        """
    )
    st.write(res.text)
