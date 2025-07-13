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

# ===== FUNÇÕES =====
def carregar_imagem(caminho, largura=None):
    if caminho.exists():
        st.image(str(caminho), width=largura, use_container_width=(largura is None))
    else:
        st.warning(f"⚠️ Imagem '{caminho.name}' não encontrada.")

def tocar_audio(arquivo):
    if arquivo.exists():
        st.audio(str(arquivo), format="audio/mp3", start_time=0)
    else:
        st.warning(f"⚠️ Áudio '{arquivo.name}' não encontrado.")

def mostrar_legenda(texto):
    st.markdown(
        f"""
        <div style='
            background-color:#ffffffcc;
            padding: 12px;
            border-radius: 10px;
            font-size:18px;
            color: #004400;
            font-weight: 500;
            text-align: center;
            border: 1px solid #88cc88;
            margin: 10px 0;'>
            {texto}
        </div>
        """,
        unsafe_allow_html=True
    )

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
    # Música de fundo automática
    tocar_audio(AUDIO / "musica_fundo.mp3")

    # Exibe o cenário da fase
    carregar_imagem(IMG_FASES / "fase1.png")

    st.markdown("### 🧕 Kawana ensina a extrair o látex:")
    sprites_kawana = [
        ("Kawane_latex1.png", "🌿 Use sempre instrumentos limpos!"),
        ("Kawane_latex2.png", "🌿 Evite cortes profundos na seringueira!"),
        ("Kawane_latex3.png", "🌿 Recolha o látex com carinho e evite desperdício."),
        ("Kawane_latex4.png", "🌿 Ensinar é cuidar da floresta para todos!")
    ]

    for sprite_nome, legenda in sprites_kawana:
        st.image(str(IMG_SPRITES / sprite_nome), width=600)
        mostrar_legenda(legenda)
        time.sleep(1.0)

    st.markdown("### ✍️ Caue está aprendendo tudo:")
    carregar_imagem(IMG_SPRITES / "Caue_anotando.png", largura=400)
    mostrar_legenda("📝 Caue está registrando tudo com atenção no caderno.")

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
