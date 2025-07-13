
import streamlit as st
from PIL import Image
import time
from pathlib import Path

st.set_page_config(page_title="Salve a Amazônia", layout="wide")

# Caminhos base
BASE = Path(__file__).parent
IMAGENS = BASE / "imagens"
FUNDOS = BASE / "fundos"
FASES = BASE / "fases"
SPRITES = BASE / "sprites"
AUDIO = BASE / "audio"

# Função segura para exibir imagem
def mostrar_imagem(pasta, nome_arquivo):
    caminho = pasta / nome_arquivo
    if caminho.exists():
        imagem = Image.open(caminho)
        st.image(imagem, use_container_width=True)
    else:
        st.error(f"Imagem não encontrada: {caminho}")

# Função para animar Kawana
def animar_kawana():
    sprites = [
        "Kawane_latex1.png",
        "Kawane_latex2.png",
        "Kawane_latex3.png",
        "Kawane_latex4.png",
    ]
    ph = st.empty()
    for sprite in sprites:
        sprite_path = SPRITES / sprite
        if sprite_path.exists():
            img = Image.open(sprite_path)
            ph.image(img, use_container_width=True)
            time.sleep(0.6)
        else:
            st.error(f"Sprite não encontrado: {sprite}")

# Tocar música automaticamente
def tocar_musica_de_fundo():
    caminho = AUDIO / "musica_fundo.mp3"
    if caminho.exists():
        with open(caminho, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3", start_time=0)

# Tocar som de vitória
def tocar_musica_vitoria():
    caminho = AUDIO / "vitoria.wav"
    if caminho.exists():
        with open(caminho, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/wav", start_time=0)

# Estados da interface
if "tela" not in st.session_state:
    st.session_state.tela = "inicio"

# TELA INICIAL
if st.session_state.tela == "inicio":
    mostrar_imagem(FUNDOS, "img_inicial.png")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🌳 Iniciar", use_container_width=True):
            st.session_state.tela = "fase1"
    with col2:
        if st.button("❌ Sair", use_container_width=True):
            st.stop()

# TELA FASE 1
elif st.session_state.tela == "fase1":
    tocar_musica_de_fundo()
    mostrar_imagem(FASES, "fase1.png")

    st.markdown("### 🎮 Fase 1: Aprendizado com Kawana")

    if st.button("Ver ação da Kawana 🌿", use_container_width=True):
        animar_kawana()

        st.markdown("<p style='font-weight:bold; color:black;'>🌱 Use sempre instrumentos limpos para respeitar a natureza.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight:bold; color:black;'>🚫 Evite ferir profundamente a árvore da seringueira.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight:bold; color:black;'>🧺 Coletar com cuidado evita o desperdício e protege a floresta!</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight:bold; color:black;'>🌳 Pronto! Agora o látex pode ser armazenado com cuidado.</p>", unsafe_allow_html=True)

        if st.button("Finalizar Fase 🎉", use_container_width=True):
            tocar_musica_vitoria()
            st.success("Parabéns! Você aprendeu com a Kawana como proteger a Amazônia!")
            st.balloons()
            st.session_state.tela = "fim"

# TELA FINAL
elif st.session_state.tela == "fim":
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Voltar ao início", use_container_width=True):
            st.session_state.tela = "inicio"
    with col2:
        if st.button("❌ Sair", use_container_width=True):
            st.stop()
