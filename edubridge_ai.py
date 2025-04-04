import streamlit as st
from googletrans import Translator
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Initialize translator and LLM
translator = Translator()
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Supported local languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Bengali": "bn",
    "Tamil": "ta"
}

# Simulated offline mode
OFFLINE_MODE = False  # Set True to disable live AI response

# UI
st.title("📚 EduBridge AI - Learn Smart in Your Language")
lang_choice = st.selectbox("Choose your language:", list(languages.keys()))
user_language = languages[lang_choice]

st.markdown("### Select a Topic to Learn:")
topic = st.selectbox("Choose topic:", ["Digital Literacy", "Cyber Safety", "Internet Basics", "Email Usage"])

question = st.text_input("❓ Ask your AI tutor a question:")

if question:
    # Translate to English if needed
    translated_question = translator.translate(question, src=user_language, dest="en").text

    if OFFLINE_MODE:
        # Offline fallback (static response)
        response = "This is an offline response. Please connect to the internet for full features."
    else:
        # Use AI tutor (LangChain + OpenAI)
        messages = [
            SystemMessage(content=f"You are an AI tutor helping users learn '{topic}' in simple language."),
            HumanMessage(content=translated_question)
        ]
        ai_response = llm(messages)
        response = ai_response.content

    # Translate back to user's language
    translated_response = translator.translate(response, src="en", dest=user_language).text
    st.markdown(f"### 🧠 Tutor's Answer:\n{translated_response}")
