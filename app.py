import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="Fiabilité - Démo QR", page_icon="📱", layout="wide")

MACHINES = {
    "THSB001": {"nom": "Thermoformeuse base de douche", "disponibilite": "96,5 %", "mttr": "2,4 h", "mtbf": "145 h"},
    "WARO001": {"nom": "Enrouleuse de mur nº 1", "disponibilite": "94,2 %", "mttr": "3,1 h", "mtbf": "118 h"},
}

st.title("Fiabilité - Démonstration QR")
st.warning("DÉMONSTRATION PUBLIQUE : KPI fictifs. Aucune donnée Navision.")
st.write("Les QR codes existants contenant simplement le code machine sont conservés.")

if "machine" not in st.session_state:
    st.session_state.machine = "THSB001"

with st.expander("📷 Scanner un QR code existant", expanded=True):
    st.write("Autorise la caméra, vise le QR code, puis prends une photo.")
    photo = st.camera_input("Photographier le QR code", key="qr_photo")
    if photo is not None:
        image = np.array(Image.open(photo).convert("RGB"))
        decoded, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        if decoded:
            code = decoded.strip().upper()
            if code in MACHINES:
                st.session_state.machine = code
                st.success(f"QR reconnu : {code}")
            else:
                st.warning(f"QR reconnu : {decoded!r}. Cette machine n'est pas encore incluse dans la démo.")
        else:
            st.error("QR non détecté. Réessaie avec une photo nette et bien éclairée.")

options = list(MACHINES)
selection = st.selectbox("Choisir une machine manuellement", options, index=options.index(st.session_state.machine))
if selection != st.session_state.machine:
    st.session_state.machine = selection

machine = MACHINES[st.session_state.machine]
st.header(f"{st.session_state.machine} - {machine['nom']}")
a, b, c = st.columns(3)
a.metric("Disponibilité", machine["disponibilite"])
b.metric("MTTR", machine["mttr"])
c.metric("MTBF", machine["mtbf"])
st.subheader("Analyse des pannes")
st.info("Classification réelle non publiée. Données fictives.")
st.subheader("Documents et vidéos")
st.write("Bientôt disponible")
