import streamlit as st
from PIL import Image
import time
from pathlib import Path
import base64

# ---------- CONFIGURAÇÃO DE PÁGINA ----------
st.set_page_config(layout="centered", page_title="Salve a Amazônia", page_icon="🌳")

# ---------- CAMINHOS DAS PASTAS ----------
BASE = Path(__file__).parent
AUDIO = BASE / "audio"
SPRITES = BASE / "sprites"
FUNDOS = BASE / "fundos"
FASES = BASE / "fases"

# ---------- FUNÇÃO PARA TOCAR ÁUDIO ----------
def tocar_audio(nome_arquivo):
    caminho = AUDIO / nome_arquivo
    if caminho.exists():
        with open(caminho, "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
                <audio autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ Arquivo de áudio não encontrado: {nome_arquivo}")

# ---------- FUNÇÃO PARA MOSTRAR IMAGEM PADRONIZADA ----------
def mostrar_imagem(path):
    if path.exists():
        imagem = Image.open(path).resize((600, 338))
        st.image(imagem)

# ---------- FUNÇÃO PARA LEGENDA FORMATADA ----------
def legenda(texto):
    st.markdown(
        f"""
        <div style="background-color: rgba(255, 255, 255, 0.7);
                    color: black;
                    padding: 12px;
                    font-size: 20px;
                    font-weight: bold;
                    border-radius: 10px;
                    text-align: center;
                    width: 600px;
                    margin: 0 auto;">
            {texto}
        </div>
        """, unsafe_allow_html=True)

# ---------- ESTADO DA APLICAÇÃO ----------
if "fase" not in st.session_state:
    st.session_state.fase = 0
if "indice_sprite" not in st.session_state:
    st.session_state.indice_sprite = 0

# ---------- DADOS DOS SPRITES E LEGENDAS ----------
sprites_kawana = [
    "Kawane_latex1.png",
    "Kawane_latex2.png",
    "Kawane_latex3.png",
    "Kawane_latex4.png"
]
legendas_kawana = [
    "Use sempre instrumentos limpos para respeitar a natureza.",
    "Evite ferir profundamente a árvore da seringueira.",
    "Coletar com cuidado evita o desperdício e protege a floresta!",
    "Pronto! Agora o látex pode ser armazenado com cuidado."
]

# ---------- TELA INICIAL ----------
if st.session_state.fase == 0:
    tocar_audio("musica_fundo.mp3")
    mostrar_imagem(FUNDOS / "tela_inicial.png")
    if st.button("🌱 Iniciar"):
        st.session_state.fase = 1

# ---------- FASE 1 ----------
elif st.session_state.fase == 1:
    mostrar_imagem(FASES / "fase1.png")

    sprite = SPRITES / sprites_kawana[st.session_state.indice_sprite]
    mostrar_imagem(sprite)

    # Texto “Clique aqui!”
    st.markdown(
        '<p style="text-align: center; color: white; font-size: 24px; font-weight: bold;">Clique aqui!</p>',
        unsafe_allow_html=True
    )

    if st.button("➡️ Ver ação da Kawana"):
        if st.session_state.indice_sprite < len(sprites_kawana) - 1:
            st.session_state.indice_sprite += 1
        else:
            st.session_state.fase = 2  # Passa para a fase final
            st.session_state.indice_sprite = 0

    legenda(legendas_kawana[st.session_state.indice_sprite])

# ---------- TELA FINAL ----------
elif st.session_state.fase == 2:
    mostrar_imagem(BASE / "parabens.png")
    tocar_audio("musica_vitoria.mp3")

    legenda("Parabéns! Você concluiu a fase com Kawana e protegeu a Amazônia!")

    st.markdown(
        """
        <div style="background-color: rgba(255, 255, 255, 0.7);
                    color: black;
                    padding: 12px;
                    font-size: 20px;
                    font-weight: bold;
                    border-radius: 10px;
                    text-align: center;
                    width: 600px;
                    margin: 10px auto;">
            A preservação da seringueira é fundamental para a economia local, a sustentabilidade ambiental e a manutenção da cultura da Amazônia.
        </div>
        <div style="background-color: rgba(255, 255, 255, 0.7);
                    color: black;
                    padding: 12px;
                    font-size: 20px;
                    font-weight: bold;
                    border-radius: 10px;
                    text-align: center;
                    width: 600px;
                    margin: 10px auto;">
            O projeto “Encauchados de Vegetais da Amazônia” vem proporcionando o desenvolvimento social de forma sustentável, em comunidades de índios, ribeirinhos, quilombolas e de assentados da reforma agrária, na Amazônia.
            <br><br>
            <a href="https://alavoura.com.br/mulheres-da-amazonia-fabricam-produtos-a-partir-do-latex-nativo/" target="_blank">🌿 Mulheres da Amazônia fabricam produtos a partir do látex nativo - A Lavoura</a>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🔄 Voltar ao Início"):
        st.session_state.fase = 0
        st.session_state.indice_sprite = 0
