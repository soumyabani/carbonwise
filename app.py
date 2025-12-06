import streamlit as st
import requests
import tempfile
from PIL import Image
import sys
import os


from ocr import extract_text_from_image, extract_text_from_pdf

API_URL = "https://ufrukgny9j.execute-api.us-east-1.amazonaws.com/default/carbonwise"

st.title("CarbonWise – AI Carbon Footprint Analyzer")

uploaded = st.file_uploader("Upload Bill or Receipt", type=["pdf", "png", "jpg", "jpeg"])

if uploaded:
    if uploaded.type == "application/pdf":
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        temp.write(uploaded.read())
        text = extract_text_from_pdf(temp.name)

    else:
        img = Image.open(uploaded)
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        img.save(temp.name)
        text = extract_text_from_image(temp.name)

    st.subheader("Extracted Text")
    st.code(text)

    # Send to Lambda
    response = requests.post(API_URL, json={"text": text})
    result = response.json()

    st.subheader("Carbon Results")
    st.json(result)

