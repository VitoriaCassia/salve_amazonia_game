import streamlit as st
from pathlib import Path
import time

# Configuração da Página
st.set_page_config(page_title="Salve a Amazônia", layout="centered")
st.title("🌿 Jogo Educativo: Salve a Amazônia")

# Diretórios esperados
IMG_FUNDOS = Path("fundos")
IMG_FASES = Path("fases")
IMG_SPRITES = Path("sprites")
AUDIO = Path("audio")

# Funções auxiliares
def tocar_audio(caminho_audio):
    if Path(caminho_audio).exists():
        st.audio(str(caminho_audio), format='audio/mp3', autoplay=True)
    else:
        st.warning(f"🎵 Arquivo de áudio não encontrado: {caminho_audio}")

def mostrar_legenda(texto):
    st.markdown(f"<div style='background-color:#e8ffe8;padding:10px;border-radius:10px;color:#004400;font-size:18px;margin-top:10px'>{texto}</div>", unsafe_allow_html=True)

# Estado inicial
if "tela" not in st.session_state:
    st.session_state.tela = "inicio"
if "musica_tocando" not in st.session_state:
    st.session_state.musica_tocando = False

# TELA INICIAL
if st.session_state.tela == "inicio":
    img_path = IMG_FUNDOS / "img_inicial.png"
    if img_path.exists():
        st.image(str(img_path), use_container_width=True)
    else:
        st.warning("Imagem 'img_inicial.png' não encontrada.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Iniciar Jogo"):
            st.session_state.tela = "fase1"
            st.session_state.musica_tocando = False
    with col2:
        st.button("❌ Sair", on_click=st.stop)

# TELA FASE 1
elif st.session_state.tela == "fase1":
    fase_img = IMG_FASES / "fase1.png"
    if fase_img.exists():
        st.image(str(fase_img), use_container_width=True)
    else:
        st.warning("Imagem 'fase1.png' não encontrada.")

    st.markdown("### 🌱 Fase 1: Kawana ensina a extrair o látex")
    st.divider()

    # Música toca automaticamente na entrada
    if not st.session_state.musica_tocando:
        tocar_audio(AUDIO / "musica_fundo.mp3")
        st.session_state.musica_tocando = True

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("👩🏽‍🌾 Ver Kawana Ensinando"):
            st.info("Kawana está explicando como extrair o látex corretamente!")
            for i in range(1, 5):
                sprite_path = IMG_SPRITES / f"Kawane_latex{i}.png"
                if sprite_path.exists():
                    st.image(str(sprite_path), width=400)
                    time.sleep(0.8)
                else:
                    st.warning(f"Imagem {sprite_path} não encontrada.")
            mostrar_legenda("🌿 Use sempre instrumentos limpos e respeite o tempo da árvore.")
            mostrar_legenda("🌿 Evite cortar profundamente para não ferir a seringueira.")
            mostrar_legenda("🌿 Recolha o látex com cuidado e evite desperdício.")

    with col2:
        if st.button("📓 Ver Caue Anotando"):
            img_caue = IMG_SPRITES / "Caue_anotando.png"
            if img_caue.exists():
                st.image(str(img_caue), width=300)
                st.info("Caue está anotando tudo para compartilhar com sua comunidade!")
            else:
                st.warning("Imagem 'Caue_anotando.png' não encontrada.")

    with col3:
        if st.button("🎉 Finalizar Fase"):
            tocar_audio(AUDIO / "vitoria.wav")
            st.success("Parabéns! Você concluiu a Fase 1 com sucesso!")
            st.balloons()
