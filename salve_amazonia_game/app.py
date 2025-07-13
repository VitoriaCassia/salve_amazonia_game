import streamlit as st
from pathlib import Path
import time

# ---------- CONFIGURAÇÃO DA PÁGINA ----------
st.set_page_config(page_title="Salve a Amazônia", layout="wide")

# ---------- FUNÇÃO PARA TOCAR MÚSICA AUTOMÁTICA ----------
def tocar_musica_automatica():
    audio_path = AUDIO / "musica_fundo.mp3"
    if audio_path.exists():
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)

# ---------- FUNÇÃO PARA EXIBIR LEGENDAS ----------
def legenda(texto):
    st.markdown(
        f"<div style='background-color:#ffffffcc; padding:10px; border-left: 5px solid green; border-radius:5px; font-size:18px'><strong>{texto}</strong></div>",
        unsafe_allow_html=True
    )

# ---------- FUNÇÃO PARA MOSTRAR SPRITES ----------
def mostrar_animacao_kawana():
    sprites = ["Kawane_latex1.png", "Kawane_latex2.png", "Kawane_latex3.png", "Kawane_latex4.png"]
    for img in sprites:
        path = SPRITES / img
        if path.exists():
            st.image(str(path), width=300)
            time.sleep(1)

# ---------- CAMINHOS DAS PASTAS ----------
BASE = Path(__file__).parent
FUNDOS = BASE / "fundos"
FASES = BASE / "fases"
IMAGENS = BASE / "imagens"
AUDIO = BASE / "audio"
SPRITES = BASE / "sprites"

# ---------- ESTADO DA TELA ----------
if "tela" not in st.session_state:
    st.session_state.tela = "inicial"

# ---------- TELA INICIAL ----------
if st.session_state.tela == "inicial":
    fundo_inicial = FUNDOS / "img_inicial.png"
    if fundo_inicial.exists():
        st.image(str(fundo_inicial), use_column_width=True)
    col1, col2 = st.columns(2)
    with col1:
        btn_iniciar = IMAGENS / "btn_iniciar.png"
        if btn_iniciar.exists() and st.button("Iniciar 🌱"):
            st.session_state.tela = "fase1"
    with col2:
        btn_sair = IMAGENS / "btn_sair.png"
        if btn_sair.exists() and st.button("Sair ❌"):
            st.stop()

# ---------- TELA FASE 1 ----------
elif st.session_state.tela == "fase1":
    tocar_musica_automatica()

    fase1 = FASES / "fase1.png"
    if fase1.exists():
        st.image(str(fase1), use_column_width=True)

    st.markdown("### 🎮 Fase 1: Aprendizado com Kawana")

    col_kawana, col_caue = st.columns(2)
    with col_kawana:
        mostrar_animacao_kawana()
    with col_caue:
        caue = SPRITES / "Caue_anotando.png"
        if caue.exists():
            st.image(str(caue), width=300)

    legenda("🌿 Use sempre instrumentos limpos para respeitar a natureza.")
    legenda("🌱 Evite ferir profundamente a árvore da seringueira.")
    legenda("🪣 Coletar com cuidado evita o desperdício e protege a floresta!")

    if st.button("Finalizar Fase 🎉"):
        vitoria = AUDIO / "vitoria.wav"
        if vitoria.exists():
            st.audio(str(vitoria), format="audio/wav")
        st.balloons()
        st.success("Parabéns! Você aprendeu com a Kawana e Caue como proteger a Amazônia!")

