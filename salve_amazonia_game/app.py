import streamlit as st
from pathlib import Path
from PIL import Image
import time

# ---------- CONFIG PÁGINA ----------
st.set_page_config(page_title="Salve a Amazônia", layout="wide")

# ---------- CAMINHOS ----------
BASE = Path(__file__).parent
FUNDOS = BASE / "fundos"
FASES = BASE / "fases"
IMAGENS = BASE / "imagens"
AUDIO = BASE / "audio"
SPRITES = BASE / "sprites"

# ---------- TOCAR MÚSICA FUNDO ----------
def tocar_musica_automatica():
    audio_path = AUDIO / "musica_fundo.mp3"
    if audio_path.exists():
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)

# ---------- LEGENDAS COM ESTILO ----------
def legenda(texto):
    st.markdown(
        f"<div style='background-color:#ffffffcc; padding:10px; border-radius:8px; font-size:18px; color:black; font-weight:bold; text-align:center'>{texto}</div>",
        unsafe_allow_html=True
    )

# ---------- MOSTRAR CENA COM SPRITE DA KAWANA E CAUE ----------
def mostrar_cena_com_sprite(sprite_kawana):
    fundo = FASES / "fase1.png"
    sprite_path = SPRITES / sprite_kawana
    caue_path = SPRITES / "caue_anotando.png"

    if fundo.exists() and sprite_path.exists() and caue_path.exists():
        fundo_img = Image.open(fundo).convert("RGBA")
        kawana_img = Image.open(sprite_path).convert("RGBA").resize((250, 250))
        caue_img = Image.open(caue_path).convert("RGBA").resize((250, 250))

        # Kawana à esquerda da árvore
        fundo_img.paste(kawana_img, (240, 270), kawana_img)
        # Caue à direita da árvore
        fundo_img.paste(caue_img, (520, 270), caue_img)

        st.image(fundo_img, use_container_width=True)

# ---------- ESTADO INICIAL ----------
if "tela" not in st.session_state:
    st.session_state.tela = "inicial"
if "etapa_kawana" not in st.session_state:
    st.session_state.etapa_kawana = 0

# ---------- TELA INICIAL ----------
if st.session_state.tela == "inicial":
    fundo_inicial = FUNDOS / "img_inicial.png"
    if fundo_inicial.exists():
        st.image(str(fundo_inicial), use_container_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        btn_iniciar = IMAGENS / "btn_iniciar.png"
        if btn_iniciar.exists():
            st.image(str(btn_iniciar), width=180)
        if st.button("Iniciar 🌱"):
            st.session_state.tela = "fase1"
            tocar_musica_automatica()

    with col2:
        btn_sair = IMAGENS / "btn_sair.png"
        if btn_sair.exists():
            st.image(str(btn_sair), width=180)
        if st.button("Sair ❌"):
            st.stop()

# ---------- FASE 1 ----------
elif st.session_state.tela == "fase1":
    st.markdown("## 🎮 Fase 1: Aprendizado com Kawana")

    falas = [
        "🌿 Use sempre instrumentos limpos para respeitar a natureza.",
        "🌱 Evite ferir profundamente a árvore da seringueira.",
        "🪣 Coletar com cuidado evita o desperdício e protege a floresta!",
        "🌳 Pronto! Agora o látex pode ser armazenado com cuidado."
    ]

    sprites_kawana = [
        "Kawane_latex1.png",
        "Kawane_latex2.png",
        "Kawane_latex3.png",
        "Kawane_latex4.png"
    ]

    etapa = st.session_state.etapa_kawana
    if etapa < len(sprites_kawana):
        mostrar_cena_com_sprite(sprites_kawana[etapa])
        legenda(falas[etapa])
        if st.button("➡️ Próxima ação da Kawana"):
            st.session_state.etapa_kawana += 1
            st.experimental_rerun()
    else:
        # CENA FINAL DA FASE
        mostrar_cena_com_sprite(sprites_kawana[-1])
        legenda("🌳 Pronto! Agora o látex pode ser armazenado com cuidado.")
        vitoria = AUDIO / "vitoria.wav"
        if vitoria.exists():
            with open(vitoria, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/wav", start_time=0)
        st.balloons()
        st.markdown(
            "<div style='background-color:#008000aa; color:white; font-size:22px; padding:20px; border-radius:8px; text-align:center'><strong>Parabéns! Você aprendeu com a Kawana e Caue como proteger a Amazônia!</strong></div>",
            unsafe_allow_html=True
        )
