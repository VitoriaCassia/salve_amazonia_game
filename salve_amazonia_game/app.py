import streamlit as st
from PIL import Image
import time
import streamlit.components.v1 as components
import base64

# Configurações da página
st.set_page_config(layout="centered", page_title="Salve a Amazônia", page_icon="🌳")

# Função para mostrar imagens com tamanho padronizado
def mostrar_imagem(nome_arquivo):
    imagem = Image.open(nome_arquivo)
    st.image(imagem, use_column_width=False, width=600)

# Função para mostrar legenda com estilo padronizado
def legenda(texto):
    st.markdown(
        f"""
        <div style="background-color: rgba(255, 255, 255, 0.7);
                    color: black;
                    padding: 12px;
                    font-size: 12pt;
                    font-weight: bold;
                    border-radius: 10px;
                    text-align: center;
                    width: 600px;
                    margin: 0 auto;">
            {texto}
        </div>
        """, unsafe_allow_html=True)

# Função para tocar áudio automaticamente
def tocar_audio(arquivo_audio):
    with open(arquivo_audio, "rb") as f:
        audio_bytes = f.read()
        b64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Início da execução
if "fase" not in st.session_state:
    st.session_state.fase = 0
if "indice_sprite" not in st.session_state:
    st.session_state.indice_sprite = 0

# Lista dos sprites da Kawana (em cima da fase1.png)
sprites_kawana = [
    "Kawane_latex1.png",
    "Kawane_latex2.png",
    "Kawane_latex3.png",
    "Kawane_latex4.png"
]

# Legendas associadas a cada sprite
legendas = [
    "Use sempre instrumentos limpos para respeitar a natureza.",
    "Evite ferir profundamente a árvore da seringueira.",
    "Coletar com cuidado evita o desperdício e protege a floresta!",
    "Pronto! Agora o látex pode ser armazenado com cuidado."
]

# Tela inicial com música de fundo automática
if st.session_state.fase == 0:
    tocar_audio("musica_fundo.mp3")
    mostrar_imagem("tela_inicial.png")
    
    if st.button("Iniciar 🌱"):
        st.session_state.fase = 1

# Fase 1: Kawana e os ensinamentos
elif st.session_state.fase == 1:
    # Exibe a imagem do fundo (fase1)
    mostrar_imagem("fase1.png")
    
    # Exibe sprite atual da Kawana sobre o fundo
    sprite_atual = sprites_kawana[st.session_state.indice_sprite]
    mostrar_imagem(sprite_atual)

    # Texto "Clique aqui!" acima do botão
    st.markdown(
        '<p style="text-align: center; color: white; font-size: 24px; font-weight: bold;">Clique aqui!</p>',
        unsafe_allow_html=True
    )

    # Botão para avançar sprites
    if st.button("➡️ Ver ação da Kawana"):
        if st.session_state.indice_sprite < len(sprites_kawana) - 1:
            st.session_state.indice_sprite += 1
        else:
            st.session_state.fase = 2  # ir para a próxima fase
            st.session_state.indice_sprite = 0

    # Legenda associada ao sprite
    legenda(legendas[st.session_state.indice_sprite])

# Fase final com imagem parabéns e texto educativo
elif st.session_state.fase == 2:
    mostrar_imagem("parabens.png")
    tocar_audio("musica_vitoria.mp3")

    legenda("Parabéns! Você concluiu a fase com Kawana e protegeu a Amazônia!")

    st.markdown(
        """
        <div style="background-color: rgba(255, 255, 255, 0.7);
                    color: black;
                    padding: 12px;
                    font-size: 12pt;
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
                    font-size: 12pt;
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
