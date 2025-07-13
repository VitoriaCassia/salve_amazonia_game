
import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Salve a Amazônia", layout="wide")

# Função para exibir imagem centralizada e com largura adaptável
def mostrar_imagem(nome_arquivo):
    imagem = Image.open(nome_arquivo)
    st.image(imagem, use_container_width=True)

# Função para simular animação da Kawana
def animar_kawana():
    sprites = [
        "Kawane_latex1.png",
        "Kawane_latex2.png",
        "Kawane_latex3.png",
        "Kawane_latex4.png",
    ]
    for sprite in sprites:
        mostrar_imagem(sprite)
        time.sleep(1)  # tempo de exibição de cada sprite

# Música de fundo automática na Fase 1
def tocar_musica_de_fundo():
    audio_file = open('fase1_musica.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', start_time=0)

# Música de vitória ao finalizar a fase
def tocar_musica_vitoria():
    audio_file = open('vitoria.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', start_time=0)

# Tela Inicial
if "tela" not in st.session_state:
    st.session_state.tela = "inicio"

if st.session_state.tela == "inicio":
    mostrar_imagem("tela_inicial.png")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🌳 Iniciar", use_container_width=True):
            st.session_state.tela = "fase1"
    with col2:
        if st.button("❌ Sair", use_container_width=True):
            st.stop()

# Fase 1 - Kawana
elif st.session_state.tela == "fase1":
    tocar_musica_de_fundo()
    mostrar_imagem("fase1.png")
    st.markdown("### 🎮 Fase 1: Aprendizado com Kawana")

    if st.button("Ver ação de Kawana 🌿", key="ver_kawana", use_container_width=True):
        animar_kawana()
        st.markdown("<p style='font-weight:bold; color:black;'>🌱 Use sempre instrumentos limpos para respeitar a natureza.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight:bold; color:black;'>🚫 Evite ferir profundamente a árvore da seringueira.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight:bold; color:black;'>🧺 Coletar com cuidado evita o desperdício e protege a floresta!</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight:bold; color:black;'>🌳 Pronto! Agora o látex pode ser armazenado com cuidado.</p>", unsafe_allow_html=True)
        if st.button("Finalizar Fase 🎉", key="fim_fase", use_container_width=True):
            tocar_musica_vitoria()
            st.success("Parabéns! Você aprendeu com a Kawana e o Cauê como proteger a Amazônia!")
            st.balloons()
            st.session_state.tela = "fim"

elif st.session_state.tela == "fim":
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Voltar ao início", use_container_width=True):
            st.session_state.tela = "inicio"
    with col2:
        if st.button("❌ Sair", use_container_width=True):
            st.stop()
