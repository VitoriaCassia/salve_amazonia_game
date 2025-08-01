import streamlit as st
from PIL import Image
from pathlib import Path

# ---------- CONFIGURAÇÃO DA PÁGINA ----------
st.set_page_config(page_title="Salve a Amazônia", layout="wide")

# ---------- CAMINHOS DAS PASTAS ----------
BASE = Path(__file__).parent
FUNDOS = BASE / "fundos"
FASES = BASE / "fases"
SPRITES = BASE / "sprites"
AUDIO = BASE / "audio"

# ---------- ESTADOS ----------
if "tela" not in st.session_state:
    st.session_state.tela = "inicio"
if "sprite_index" not in st.session_state:
    st.session_state.sprite_index = 0
if "musica_tocando" not in st.session_state:
    st.session_state.musica_tocando = False

# ---------- MAPA DE ÁUDIOS POR SPRITE ----------
sprite_audio_map = {
    "inicio": "salve.mp3",
    "Kawane_latex1.png": "fala1.mp3",
    "Kawane_latex2.png": "fala2.mp3",
    "Kawane_latex3.png": "fala3.mp3",
    "Kawane_latex4.png": "fala4.mp3",
    "parabens": ["fala5.mp3", "fala6.mp3", "fala7.mp3"]
}

# ---------- SPRITES E LEGENDAS ----------
sprites_kawana = [
    "Kawane_latex1.png",
    "Kawane_latex2.png",
    "Kawane_latex3.png",
    "Kawane_latex4.png",
]
legendas = [
    "🌱 Use sempre instrumentos limpos para respeitar a natureza.",
    "🚫 Evite ferir profundamente a árvore da seringueira.",
    "🧺 Coletar com cuidado evita o desperdício e protege a floresta!",
    "🌳 Pronto! Agora o látex pode ser armazenado com cuidado."
]

# ---------- FUNÇÕES DE UTILIDADE ----------
def mostrar_imagem(path):
    if path.exists():
        imagem = Image.open(path).resize((800, 451))
        st.image(imagem)

def sobrepor_sprite(fundo_path, sprite_path):
    if fundo_path.exists() and sprite_path.exists():
        fundo = Image.open(fundo_path).resize((800, 451)).convert("RGBA")
        sprite = Image.open(sprite_path).resize((800, 451)).convert("RGBA")
        combinado = Image.alpha_composite(fundo, sprite)
        st.image(combinado)

def tocar_audio(nome_arquivo):
    caminho = AUDIO / nome_arquivo
    if caminho.exists():
        with open(caminho, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

def legenda(texto):
    st.markdown(
        f"<div style='background-color:#ffffffcc; padding:10px; border-left: 5px solid green; border-radius:5px; "
        f"font-size:24px; color:black; font-weight:bold; width:1200px; margin:0 auto;'>{texto}</div>",
        unsafe_allow_html=True
    )

# ---------- TELA INICIAL ----------
if st.session_state.tela == "inicio":
    mostrar_imagem(FUNDOS / "img_inicial.png")
    tocar_audio(sprite_audio_map["inicio"])  # Toca salve.mp3

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌳 Iniciar"):
            st.session_state.tela = "fase1"
            st.session_state.sprite_index = 0
   # with col2:
    #    if st.button("❌ Sair"):
         #   st.stop()

# ---------- TELA FASE 1 ----------
elif st.session_state.tela == "fase1":
    fase1_path = FASES / "fase1.png"
    sprite_atual = sprites_kawana[st.session_state.sprite_index]
    sprite_path = SPRITES / sprite_atual

    sobrepor_sprite(fase1_path, sprite_path)
    legenda(legendas[st.session_state.sprite_index])

    # Toca o áudio correspondente ao sprite
    if sprite_atual in sprite_audio_map:
        tocar_audio(sprite_audio_map[sprite_atual])

    if st.button("▶️ Próxima ação da Kawana"):
        if st.session_state.sprite_index < len(sprites_kawana) - 1:
            st.session_state.sprite_index += 1
        else:
            st.session_state.tela = "fim"

# ---------- TELA FINAL ----------
elif st.session_state.tela == "fim":
    st.markdown("## 🎉 Fase concluída!")
    col1, col2 = st.columns([1, 1])

    with col1:
        parabens_path = SPRITES / "parabens.png"
        if parabens_path.exists():
            imagem = Image.open(parabens_path).resize((600, 338))
            st.image(imagem)

    with col2:
        st.markdown(
            """
            <div style='background-color:#ffffffcc; padding:15px; border-left: 5px solid green; border-radius:5px; 
            font-size:20px; color:black; font-weight:bold;'>
                🎉 Parabéns! Você concluiu a fase com Kawana e protegeu a Amazônia!<br><br>
                🌱 A preservação da seringueira é fundamental para a economia local, a sustentabilidade ambiental e a manutenção da cultura da Amazônia.<br><br>
                📘 O projeto “Encauchados de Vegetais da Amazônia” vem proporcionando o desenvolvimento social de forma sustentável, 
                em comunidades de índios, ribeirinhos, quilombolas e de assentados da reforma agrária, na Amazônia.
            </div>
            """, unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style='background-color:#ffffffcc; padding:10px; border-left: 5px solid green; border-radius:5px; 
            font-size:18px; color:black; font-weight:bold; text-align: center;'>
                🔗 <a href="https://alavoura.com.br/colunas/organicos/sustentabilidade-organicos/mulheres-da-amazonia-fabricam-produtos-a-partir-do-latex-nativo/?utm_source=chatgpt.com" target="_blank">
                Mulheres da Amazônia fabricam produtos a partir do látex nativo - A Lavoura
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    # Toca os áudios da tela final (fala5, fala6, fala7)
    for audio in sprite_audio_map["parabens"]:
        tocar_audio(audio)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Voltar ao início"):
            st.session_state.tela = "inicio"
            st.session_state.sprite_index = 0
            st.session_state.musica_tocando = False
   # with col2:
     #   if st.button("❌ Sair"):
         #   st.stop()
