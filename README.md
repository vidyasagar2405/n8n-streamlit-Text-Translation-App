# n8n-streamlit-Text-Translation-App

# 🌈 Text Translation App — Using n8n + Streamlit

A simple and powerful **English → Telugu / Hindi** translation app built with **Streamlit** as the frontend and **n8n AI Agent (Gemini)** as the backend processor. The app sends user input to an n8n webhook, which triggers an AI Agent to generate translated text and returns it back to the UI in real-time.

---

## 📸 Screenshots

**App UI:**
<img width="1470" height="956" alt="Text Translation snapshot" src="https://github.com/user-attachments/assets/9c322dd1-0a08-4602-b23f-cc2f00657a42" />


**n8n Workflow:**
<img width="1116" height="529" alt="n8n workflow of text translation" src="https://github.com/user-attachments/assets/c5dee910-3294-4cc6-9f68-56b6357eeaf2" />

---

## 🚀 Features

* Translate English text into **Telugu** or **Hindi**
* **Two-button UI** (Telugu / Hindi)
* **Streamlit frontend UI** with a gradient header
* Backend powered by **n8n Webhook + AI Agent**
* Uses **Google Gemini Chat Model** to generate translations
* Clean UI with fast response

---

## 🧩 How It Works

1. User enters English text in Streamlit
2. User clicks **Telugu** or **Hindi**
3. Streamlit sends the request to **n8n Webhook**
4. n8n → AI Agent → Gemini translates the text
5. n8n returns translated text back to Streamlit
6. Streamlit displays the final output

---

## 📁 Project Structure

```
.
├── app.py                    # Streamlit Frontend
├── requirements.txt          # Python dependencies
├── Text Translation N8N file.json   # n8n Workflow Export
└── Text Translation snapshot.png    # App Screenshot
```

---

## ⚙️ Installation

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Run the App

```
streamlit run app.py
```

### 3. Configure n8n

* Import the workflow
* Set up the **Webhook URL**
* Add your **Gemini API Key**
* Update the **Webhook URL in app.py**

---

## 🧠 Technologies Used

* **Streamlit**
* **n8n**
* **Webhook Trigger**
* **AI Agent (Gemini Chat Model)**

---

## **demo video**
[Youtube](https://youtu.be/3Yqg091DSRY)

## ⭐ Contribute

Feel free to fork and enhance the UI, add more languages, or integrate speech-to-text.
