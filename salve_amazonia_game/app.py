import streamlit as st
from pathlib import Path
from PIL import Image
import time

# ---------- CONFIGURAÇÃO DA PÁGINA ----------
st.set_page_config(page_title="Salve a Amazônia", layout="wide")

# ---------- CAMINHOS DAS PASTAS ----------
BASE = Path(__file__).parent
FUNDOS = BASE / "fundos"
FASES = BASE / "fases"
IMAGENS = BASE / "imagens"
AUDIO = BASE / "audio"
SPRITES = BASE / "sprites"

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

# ---------- FUNÇÃO PARA ANIMAÇÃO DA KAWANA COM SPRITES E LEGENDAS ----------
def animacao_kawana_com_falas():
    sprites = [
        ("Kawane_latex1.png", "🌿 Use sempre instrumentos limpos para respeitar a natureza."),
        ("Kawane_latex2.png", "🌱 Evite ferir profundamente a árvore da seringueira."),
        ("Kawane_latex3.png", "🪣 Coletar com cuidado evita o desperdício e protege a floresta!"),
        ("Kawane_latex4.png", "🌳 Pronto! Agora o látex pode ser armazenado com cuidado.")
    ]
    for img, fala in sprites:
        path = SPRITES / img
        if path.exists():
            fundo = FASES / "fase1.png"
            if fundo.exists():
                fundo_img = Image.open(fundo).convert("RGBA")
                sprite_img = Image.open(path).convert("RGBA").resize((250, 250))
                fundo_img.paste(sprite_img, (300, 150), sprite_img)  # coordenada aproximada
                st.image(fundo_img, use_column_width=True)
            legenda(fala)
            time.sleep(2)

# ---------- ESTADO DA TELA ----------
if "tela" not in st.session_state:
    st.session_state.tela = "inicial"

# ---------- TELA INICIAL ----------
if st.session_state.tela == "inicial":
    fundo_inicial = FUNDOS / "img_inicial.png"
    if fundo_inicial.exists():
        st.image(str(fundo_inicial), use_container_width=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        btn_iniciar = IMAGENS / "btn_iniciar.png"
        if btn_iniciar.exists():
            st.image(btn_iniciar, width=150)
            if st.button("Iniciar 🌱"):
                st.session_state.tela = "fase1"

    with col2:
        btn_audio = IMAGENS / "btn_audio.png"
        if btn_audio.exists():
            st.image(btn_audio, width=150)

    with col3:
        btn_sair = IMAGENS / "btn_sair.png"
        if btn_sair.exists():
            st.image(btn_sair, width=150)
            if st.button("Sair ❌"):
                st.stop()

# ---------- TELA FASE 1 ----------
elif st.session_state.tela == "fase1":
    tocar_musica_automatica()
    st.markdown("## 🎮 Fase 1: Aprendizado com Kawana")

    # Kawana e Caue lado a lado
    col_kawana, col_caue = st.columns(2)
    with col_kawana:
        animacao_kawana_com_falas()

    with col_caue:
        caue = SPRITES / "caue_anotando.png"
        if caue.exists():
            st.image(str(caue), width=300)

    if st.button("Finalizar Fase 🎉"):
        vitoria = AUDIO / "vitoria.wav"
        if vitoria.exists():
            st.audio(str(vitoria), format="audio/wav")
        st.balloons()
        st.success("Parabéns! Você aprendeu com a Kawana e Caue como proteger a Amazônia!")

