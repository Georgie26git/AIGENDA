import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key='AIzaSyDL1varc0e5y7JDKCQUHkzxTAL1lRF1v5A')

model= genai.GenerativeModel('gemini-1.5-flash')
 
def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")
    
st.set_page_config(page_title='Georges invoice')
st.sidebar.header("Robobill")
st.sidebar.write("Made by  YDG")
st.sidebar.write("Powdered by GOOGLE GEMINI AI")
st.header("Robobill")
st.subheader("Made by YDG")
st.subheader("Manage your expenses with Robobill")
input = st.text_input("What do you want me to do?",key="input") 
uploaded_file=st.file_uploader("Choose an image",type=['jpg','jpeg','png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

ssubmit = st.button("Namalku Pogam!")

input_prompt = """
You are an expert in reading invoices. We are going to upload an image of an invoice
and you will have to answer any type of questions that the user asks you.
You have to greet the user first. Make aure to keep the fonts uniform and give
the items list ina point-wise format.
At the end, make sure to repeat the name of out app "Robobill" and
ask the user to use it again.
"""
if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Heres what you need to know!")
    st.write(response)
