import streamlit as st
from PIL import Image
import time
from pathlib import Path

# ---------- CONFIGURAÇÃO DA PÁGINA ----------
st.set_page_config(page_title="Salve a Amazônia", layout="wide")

# ---------- CAMINHOS DAS PASTAS ----------
BASE = Path(__file__).parent
FUNDOS = BASE / "fundos"
FASES = BASE / "fases"
SPRITES = BASE / "sprites"
AUDIO = BASE / "audio"

# ---------- FUNÇÃO PARA EXIBIR IMAGEM ----------
def mostrar_imagem(path):
    if path.exists():
        imagem = Image.open(path).resize((1920, 1080))
        st.image(imagem)

# ---------- FUNÇÃO PARA SOBREPOR SPRITE NO FUNDO ----------
def sobrepor_sprite(fundo_path, sprite_path):
    if fundo_path.exists() and sprite_path.exists():
        fundo = Image.open(fundo_path).resize((1920, 1080)).convert("RGBA")
        sprite = Image.open(sprite_path).resize((1920, 1080)).convert("RGBA")
        combinado = Image.alpha_composite(fundo, sprite)
        st.image(combinado)

# ---------- FUNÇÃO PARA TOCAR MÚSICA DE FUNDO ----------
def tocar_musica_de_fundo():
    musica = AUDIO / "musica_fundo.mp3"
    if musica.exists():
        with open(musica, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3', start_time=0)

# ---------- FUNÇÃO PARA TOCAR MÚSICA DE VITÓRIA ----------
def tocar_musica_vitoria():
    musica = AUDIO / "vitoria.wav"
    if musica.exists():
        with open(musica, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav', start_time=0)

# ---------- FUNÇÃO PARA EXIBIR LEGENDA ----------
def legenda(texto):
    st.markdown(
        f"<div style='background-color:#ffffffcc; padding:10px; border-left: 5px solid green; border-radius:5px; font-size:16px; color:black; font-weight:bold'>{texto}</div>",
        unsafe_allow_html=True
    )

# ---------- ESTADO INICIAL ----------
if "tela" not in st.session_state:
    st.session_state.tela = "inicio"
if "sprite_index" not in st.session_state:
    st.session_state.sprite_index = 0

# ---------- SPRITES DA KAWANA ----------
sprites_kawana = [
    "Kawane_latex1.png",
    "Kawane_latex2.png",
    "Kawane_latex3.png",
    "Kawane_latex4.png",
]

# ---------- LEGENDA DE CADA SPRITE ----------
legendas = [
    "🌱 Use sempre instrumentos limpos para respeitar a natureza.",
    "🚫 Evite ferir profundamente a árvore da seringueira.",
    "🧺 Coletar com cuidado evita o desperdício e protege a floresta!",
    "🌳 Pronto! Agora o látex pode ser armazenado com cuidado."
]

# ---------- TELA INICIAL ----------
if st.session_state.tela == "inicio":
    mostrar_imagem(FUNDOS / "img_inicial.png")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌳 Iniciar"):
            st.session_state.tela = "fase1"
            st.session_state.sprite_index = 0
    with col2:
        if st.button("❌ Sair"):
            st.stop()

# ---------- FASE 1 ----------
elif st.session_state.tela == "fase1":
    tocar_musica_de_fundo()
    fase1_path = FASES / "fase1.png"
    sprite_atual = SPRITES / sprites_kawana[st.session_state.sprite_index]
    
    sobrepor_sprite(fase1_path, sprite_atual)
    legenda(legendas[st.session_state.sprite_index])

    if st.button("▶️ Próxima ação da Kawana"):
        if st.session_state.sprite_index < len(sprites_kawana) - 1:
            st.session_state.sprite_index += 1
        else:
            st.session_state.tela = "fim"
            tocar_musica_vitoria()

# ---------- TELA FINAL ----------
elif st.session_state.tela == "fim":
    st.success("Parabéns! Você concluiu a fase com Kawana e protegeu a Amazônia! 🎉")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Voltar ao início"):
            st.session_state.tela = "inicio"
            st.session_state.sprite_index = 0
    with col2:
        if st.button("❌ Sair"):
            st.stop()
