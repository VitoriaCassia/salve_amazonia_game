import streamlit as st
import time
from pathlib import Path

# ===== CONFIGURAÇÃO =====
st.set_page_config(page_title="Salve a Amazônia - Fase 1", layout="wide")

# ===== CAMINHOS =====
BASE = Path(__file__).parent
IMG_FUNDOS = BASE / "fundos"
IMG_FASES = BASE / "fases"
IMG_BOTOES = BASE / "imagens"
IMG_SPRITES = BASE / "sprites"
AUDIO = BASE / "audio"

# ===== FUNÇÕES AUXILIARES =====
def carregar_imagem(caminho):
    if caminho.exists():
        st.image(str(caminho), use_container_width=True)
    else:
        st.warning(f"⚠️ Imagem '{caminho.name}' não encontrada.")

def tocar_audio(arquivo):
    if arquivo.exists():
        st.audio(str(arquivo), format="audio/mp3", start_time=0)
    else:
        st.warning(f"⚠️ Áudio '{arquivo.name}' não encontrado.")

def mostrar_legenda(texto):
    st.markdown(f"<div style='background-color:#d4edda;padding:10px;border-radius:8px;color:#155724;font-size:18px'>{texto}</div>", unsafe_allow_html=True)

# ===== TELA ATUAL =====
if "tela" not in st.session_state:
    st.session_state.tela = "inicial"

# ===== TELA INICIAL =====
if st.session_state.tela == "inicial":
    carregar_imagem(IMG_FUNDOS / "img_inicial.png")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🎮 Iniciar Jogo", key="btn_iniciar"):
            st.session_state.tela = "fase1"
    with col2:
        st.markdown("Feito com carinho para salvar a Amazônia 🌳")
    with col3:
        if st.button("❌ Sair", key="btn_sair"):
            st.stop()

# ===== FASE 1 =====
elif st.session_state.tela == "fase1":
    carregar_imagem(IMG_FASES / "fase1.png")
    st.subheader("🌱 Fase 1: Kawana ensina a extrair látex")

    # Música toca automaticamente
    tocar_audio(AUDIO / "musica_fundo.mp3")

    # Kawana em animação
    st.markdown("#### 🧕 Kawana mostra como extrair o látex:")
    sprites_kawana = [
        IMG_SPRITES / "Kawane_latex1.png",
        IMG_SPRITES / "Kawane_latex2.png",
        IMG_SPRITES / "Kawane_latex3.png",
        IMG_SPRITES / "Kawane_latex4.png",
    ]
    for sprite in sprites_kawana:
        carregar_imagem(sprite)
        time.sleep(0.6)

    mostrar_legenda("🌿 Use sempre instrumentos limpos!")
    mostrar_legenda("🌿 Evite cortes profundos na seringueira!")
    mostrar_legenda("🌿 Recolha o látex com carinho e evite desperdício.")

    # Caue anotando
    st.markdown("#### ✍️ Caue está aprendendo e anotando tudo:")
    carregar_imagem(IMG_SPRITES / "Caue_anotando.png")

    # Finalizar
    st.success("Você aprendeu com Kawana como proteger a floresta! 🌳")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Voltar ao início", key="btn_voltar_inicio"):
            st.session_state.tela = "inicial"
    with col2:
        if st.button("✅ Finalizar Fase", key="btn_finalizar"):
            tocar_audio(AUDIO / "vitoria.wav")
            st.balloons()
            st.success("Fase concluída com sucesso! 🎉")

