import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import constants as const


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title=const.APP_PAGE_TITLE)
st.header(const.APP_HEADER)
input = st.text_input("Question: ", key = "question")
submit = st.button(const.APP_SUBMIT_BUTTON)

# Load Gemini pro model to get responses
model=genai.GenerativeModel(const.GOOGLE_APP_MODEL)
def get_response(query):
    ans = model.generate_content(query)
    return ans.text

if submit:
    resp = get_response(input)
    st.subheader("Response is:")
    st.write(resp)