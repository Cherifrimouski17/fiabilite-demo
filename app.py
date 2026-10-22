
import streamlit as st

st.set_page_config(page_title="Fiabilité - Démonstration", layout="wide")

st.title("Tableau de bord - Fiabilité")
st.success("Application de démonstration en ligne !")

machine = st.selectbox("Choisir une machine", ["WARO001", "THSB001"])

st.subheader(f"Fiche machine : {machine}")
st.info("Données fictives - démonstration uniquement")

col1, col2, col3 = st.columns(3)
col1.metric("Disponibilité", "96,5 %")
col2.metric("MTTR", "2,4 h")
col3.metric("MTBF", "145 h")

st.subheader("Documents et vidéos")
st.write("Bientôt disponible")
