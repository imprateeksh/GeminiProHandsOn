import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import constants as const
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title=const.VISION_PAGE_TITLE)
st.header(const.VISION_HEADER)
input = st.text_input("Question: ", key = "question")
uploaded_file = st.file_uploader("Choose Image...", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded img", use_column_width=True)


submit = st.button(const.VISION_SUBMIT_BUTTON)
# Load Gemini pro model to get responses
model=genai.GenerativeModel(const.GOOGLE_VISION_MODEL)

def get_response(input,image):
    if input:
        ans = model.generate_content([input,image])
    else:
        ans = model.generate_content(image)
    return ans.text

if submit:
    resp = get_response(input, image)
    st.subheader("Response is:")
    st.write(resp)