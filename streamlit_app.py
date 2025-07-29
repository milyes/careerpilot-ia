import streamlit as st
import openai

st.set_page_config(page_title="🛣️ Simulateur de reconversion", page_icon="🔄")

openai.api_key = st.secrets["openai_key"]

st.title("🔁 Simulateur de reconversion pro")

current_job = st.text_input("Quel est ton métier actuel ?")
reason = st.text_area("Pourquoi veux-tu changer de domaine ?")
target_fields = st.multiselect(
    "Vers quels domaines veux-tu te reconvertir ?",
    ["Intelligence Artificielle", "UX Design", "Développement Web", "Marketing Digital", "Freelance", "Cybersecurity", "Gestion de projet"]
)

if st.button("🚀 Lance le simulateur IA") and current_job and reason and target_fields:
    with st.spinner("L’IA explore les trajectoires pour toi..."):
        prompt = f"""
        Métier actuel : {current_job}
        Motivation : {reason}
        Domaines ciblés : {', '.join(target_fields)}
        
        Propose un plan de reconversion réaliste. Inclure :
        - Étapes concrètes de transition
        - Formations ou certifications pertinentes
        - Potentiel salarial et perspectives d’avenir
        - Conseils personnalisés
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        st.success("🧠 Ton plan de reconversion IA :")
        st.write(response.choices[0].message.content)
