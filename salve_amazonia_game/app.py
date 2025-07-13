import streamlit as st
import time

# CONFIGURAÇÃO DO APP
st.set_page_config(page_title="Salve a Amazônia - Fase 1", layout="wide")

# FUNÇÕES AUXILIARES
def tocar_audio(audio_path):
    st.audio(audio_path, format='audio/mp3')

def mostrar_legenda(texto):
    st.markdown(
        f"<div style='background-color:#e0ffe0;padding:10px;border-radius:10px;"
        f"color:#004400;font-size:18px;margin-bottom:10px'>{texto}</div>",
        unsafe_allow_html=True
    )

# DEFININDO O ESTADO INICIAL
if "tela" not in st.session_state:
    st.session_state.tela = "inicial"

# ---------------- TELA INICIAL ----------------
if st.session_state.tela == "inicial":
    st.image("fundos/img_inicial.png", use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌱 Iniciar", key="btn_iniciar"):
            st.session_state.tela = "fase1"

    with col2:
        if st.button("📜 Créditos", key="btn_creditos"):
            st.markdown("Desenvolvido por Vibe Coding + Você 🌿")

    with col3:
        if st.button("❌ Sair", key="btn_sair"):
            st.stop()

# ---------------- FASE 1 ----------------
elif st.session_state.tela == "fase1":
    st.image("fases/fase1.png", use_container_width=True)
    st.markdown("### 🎮 Fase 1: Extração Sustentável do Látex com Kawana e Caue")
    st.markdown("---")

    # Música de fundo
    col_audio, col_voltar = st.columns([1, 1])
    with col_audio:
        if st.button("🔊 Música de Fundo", key="btn_audio"):
            tocar_audio("audio/musica_fundo.mp3")
    with col_voltar:
        if st.button("🔙 Voltar", key="btn_voltar_inicio"):
            st.session_state.tela = "inicial"

    # Ver Kawana ensinando
    st.markdown("#### 👩🏽‍🏫 Ver Kawana ensinando a extração do látex")
    if st.button("▶️ Ver Kawana", key="btn_ver_Kawana"):
        sprites_kawana = [
            "sprites/Kawane_latex1.png",
            "sprites/Kawane_latex2.png",
            "sprites/Kawane_latex3.png",
            "sprites/Kawane_latex4.png"
        ]
        falas_kawana = [
            "Use sempre instrumentos limpos e respeite o tempo da árvore.",
            "Evite cortar profundamente para não ferir a seringueira.",
            "Recolha o látex com cuidado e evite desperdício.",
            "Proteger a floresta é garantir o nosso futuro."
        ]
        for i, sprite in enumerate(sprites_kawana):
            st.image(sprite, width=400)
            mostrar_legenda(falas_kawana[i])
            time.sleep(1.2)

        st.success("Kawana terminou o ensinamento! Agora é a vez do Caue.")

    # Caue anotando
    st.markdown("#### 📝 Caue está anotando tudo com atenção:")
    st.image("sprites/caue_anotando.png", width=300)

    # Finalizar fase
    if st.button("🎉 Finalizar Fase", key="btn_finaliza"):
        tocar_audio("audio/vitoria.wav")
        st.balloons()
        st.markdown("## 🌟 Parabéns! Você concluiu a Fase 1 com sabedoria indígena!")

