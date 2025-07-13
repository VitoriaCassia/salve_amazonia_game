import streamlit as st
from pathlib import Path
import time

# ---------------------- CONFIGURAÇÃO ---------------------- #
st.set_page_config(page_title="Salve a Amazônia", layout="wide")
st.title("🌳 Salve a Amazônia - Fase 1")

# ---------------------- CAMINHOS -------------------------- #
IMG_FUNDOS = Path("fundos")
IMG_FASES = Path("fases")
IMG_SPRITES = Path("sprites")
AUDIO = Path("audio")

# ---------------------- FUNÇÕES AUXILIARES ---------------- #
def mostrar_legenda(texto):
    st.markdown(f"<div style='background-color:#e6ffe6;padding:10px;border-radius:10px;margin-top:10px;color:#004d00;font-size:18px'>{texto}</div>", unsafe_allow_html=True)

def tocar_audio(nome_arquivo):
    caminho = AUDIO / nome_arquivo
    if caminho.exists():
        st.audio(str(caminho), format="audio/mp3")
    else:
        st.error(f"⚠️ Áudio '{nome_arquivo}' não encontrado.")

# ---------------------- TELA INICIAL ---------------------- #
if "tela" not in st.session_state:
    st.session_state.tela = "inicio"

if st.session_state.tela == "inicio":
    st.subheader("Bem-vindo ao jogo educativo Salve a Amazônia!")
    imagem_inicial = IMG_FUNDOS / "img_inicial.png"
    if imagem_inicial.exists():
        st.image(str(imagem_inicial), use_container_width=True)
    else:
        st.warning("Imagem 'img_inicial.png' não encontrada.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Iniciar Jogo"):
            st.session_state.tela = "fase1"
    with col2:
        st.markdown("Feito com carinho para salvar a floresta 🌱")

# ---------------------- FASE 1 ---------------------- #
elif st.session_state.tela == "fase1":
    st.subheader("🌿 Fase 1: Extração Sustentável do Látex")
    
    imagem_fase = IMG_FASES / "fase1.png"
    if imagem_fase.exists():
        st.image(str(imagem_fase), use_container_width=True)
    else:
        st.warning("Imagem 'fase1.png' não encontrada.")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔊 Tocar Música"):
            tocar_audio("musica_fundo.mp3")
    with col2:
        if st.button("👩‍🏫 Ver Kawana Ensinando"):
            st.info("Kawana está ensinando como extrair o látex!")
            sprites = [
                "Kawane_latex1.png",
                "Kawane_latex2.png",
                "Kawane_latex3.png",
                "Kawane_latex4.png",
            ]
            for img in sprites:
                path = IMG_SPRITES / img
                if path.exists():
                    st.image(str(path), width=400)
                    time.sleep(0.7)
                else:
                    st.warning(f"Sprite '{img}' não encontrado.")
            mostrar_legenda("Use sempre instrumentos limpos e respeite o tempo da árvore.")
            mostrar_legenda("Evite cortar profundamente para não ferir a seringueira.")
            mostrar_legenda("Recolha o látex com cuidado e evite desperdício.")
    with col3:
        if st.button("✅ Finalizar Fase"):
            tocar_audio("vitoria.wav")
            st.success("Você aprendeu com Kawana como proteger a floresta!")
            st.balloons()

    st.divider()
    st.subheader("📝 Caue está anotando tudo que aprendeu:")
    img_caue = IMG_SPRITES / "Caue_anotando.png"
    if img_caue.exists():
        st.image(str(img_caue), width=300)
    else:
        st.warning("Imagem 'Caue_anotando.png' não encontrada.")
