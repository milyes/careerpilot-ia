import streamlit as st
import openai

# Configuration Streamlit
st.set_page_config(page_title="CareerPilot IA", layout="centered")
st.title("🚀 CareerPilot IA")
st.markdown("Une application IA interactive pour explorer les carrières et poser des questions.")

# Clé API OpenAI (à remplacer par ta propre clé ou via secrets Streamlit)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Sidebar
st.sidebar.header("📁 Menu")
option = st.sidebar.radio("Navigation :", ["Accueil", "Chatbot IA", "À propos"])

# Accueil
if option == "Accueil":
    st.subheader("📌 Bienvenue")
    st.write("Utilise le menu pour démarrer le chatbot ou en savoir plus sur l’app.")

# Chatbot IA
elif option == "Chatbot IA":
    st.subheader("💬 Interagis avec le chatbot")
    user_input = st.text_input("Pose ta question ici :")

    if user_input:
        with st.spinner("Réponse en cours..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un assistant de carrière amical et compétent."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success("Réponse reçue ✅")
            st.markdown(f"**🤖 CareerBot :** {response['choices'][0]['message']['content']}")

# À propos
else:
    st.subheader("ℹ️ À propos")
    st.write("Développé avec ❤️ par Ilyes et Copilot. Powered by OpenAI & Streamlit.")
