import streamlit as st
import requests

st.title(":rainbow[Text Translation App Using N8N+streamlit]")
st.subheader(":blue[Translate your English text to Either Telugu or Hindi format.]")

text = st.text_area("Please Enter the Text inside the text area.")
url = "https://sagardesktopn8n.app.n8n.cloud/webhook-test/675207f3-a2e9-4256-9f11-324dc35db046"

if st.button(":green[Telugu]"):
    if text:
        response = requests.post(url , data = {"text" : text, "lang" : "Telugu"})
        if response.status_code == 200:
            st.write(response.json()[0]["output"])
        else:
            st.error("API Error: " + str(response.status_code))

if st.button(":green[Hindi]"):
    if text:
        response = requests.post(url , data = {"text" : text, "lang" : "Hindi"})
        if response.status_code == 200:
            st.write(response.json()[0]["output"])
        else:
            st.error("API Error: " + str(response.status_code))

else:
    pass