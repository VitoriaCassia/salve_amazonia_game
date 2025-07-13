import streamlit as st
import time

# ----- CONFIG ----- #
st.set_page_config(page_title="Salve a Amazônia - Fase 1", layout="wide")

# ----- FUNÇÕES ----- #
def tocar_audio(audio_path):
    st.audio(audio_path, format='audio/mp3')

def mostrar_legenda(texto):
    st.markdown(f"<div style='background-color:#e0ffe0;padding:10px;border-radius:10px;color:#004400;font-size:18px'>{texto}</div>", unsafe_allow_html=True)

# ----- TELAS ----- #
if "tela" not in st.session_state:
    st.session_state.tela = "inicial"

# ----- TELA INICIAL ----- #
if st.session_state.tela == "inicial":
    st.image("fundos/img_inicial.png", use_container_width=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌱 Iniciar", key="btn_iniciar"):
            st.session_state.tela = "fase1"
    with col2:
        st.markdown("Feito com carinho para salvar a Amazônia 🌿")
    with col3:
        if st.button("❌ Sair", key="btn_sair"):
            st.stop()

# ----- FASE 1 ----- #
elif st.session_state.tela == "fase1":
    st.image("fases/fase1.png", use_column_width=True)

    st.markdown("### 🎮 Fase 1: Extração Sustentável do Látex com Kawana e Caue")
    st.markdown("---")

    # Botão de áudio
    col_audio, col_sair = st.columns([1,1])
    with col_audio:
        if st.button("🔊 Música de Fundo", key="btn_audio"):
            tocar_audio("audio/musica_fundo.mp3")
    with col_sair:
        if st.button("🔙 Voltar", key="btn_voltar_fase1"):
            st.session_state.tela = "inicial"

    # Animação Kawana (Storyboard)
    st.subheader("🌿 Kawana ensina a extrair o látex da seringueira:")
    sprites_kawana = [
        "sprites/Kawane_latex1.png",
        "sprites/Kawane_latex2.png",
        "sprites/Kawane_latex3.png",
        "sprites/Kawane_latex4.png"
    ]
    for sprite in sprites_kawana:
        st.image(sprite, width=400)
        time.sleep(0.8)

    mostrar_legenda("Use sempre instrumentos limpos e respeite o tempo da árvore!")
    mostrar_legenda("Evite cortar profundamente para não ferir a seringueira!")
    mostrar_legenda("Recolha o látex com cuidado e evite desperdício.")

    # Caue anotando
    st.subheader("📝 Caue está anotando tudo com atenção!")
    st.image("sprites/caue_anotando.png", width=300)

    st.success("Você aprendeu com Kawana como proteger a floresta com sabedoria indígena!")
    if st.button("🎉 Finalizar Fase", key="btn_finaliza"):
        tocar_audio("audio/vitoria.wav")
        st.balloons()
        st.markdown("### Parabéns! Você concluiu a fase 1 com sucesso. 🌱")
