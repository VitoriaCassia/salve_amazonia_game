import streamlit as st
from pathlib import Path

# Caminhos das pastas
IMG_FUNDOS = Path("fundos")
IMG_AUDIO = Path("audio")
IMG_BOTOES = Path("imagens")
IMG_FASES = Path("fases")
IMG_SPRITES = Path("sprites")

# Configuração da página
st.set_page_config(page_title="Salve a Amazônia - Fase 1", layout="centered")

# Função de legenda com destaque visual
def mostrar_legenda(texto):
    st.markdown(
        f"<div style='background-color:#e0ffe0;padding:10px;border-radius:10px;color:#004400;font-size:18px'>{texto}</div>",
        unsafe_allow_html=True
    )

# Controle de telas
if "tela" not in st.session_state:
    st.session_state.tela = "inicial"

# Tela Inicial
if st.session_state.tela == "inicial":
    st.image(str(IMG_FUNDOS / "img_inicial.png"), width=900)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌱 Iniciar", key="btn_iniciar"):
            st.session_state.tela = "fase1"
    with col2:
        st.markdown("Feito com carinho para salvar a Amazônia 🌿")
    with col3:
        if st.button("❌ Sair", key="btn_sair"):
            st.stop()

# Fase 1
elif st.session_state.tela == "fase1":
    st.markdown("### 🎮 Fase 1: Extração Sustentável do Látex com Kawana e Caue")
    st.image(str(IMG_FASES / "fase1.png"), use_container_width=True)

    col_audio, col_voltar = st.columns(2)
    with col_audio:
        if st.button("🔊 Música de Fundo", key="btn_audio"):
            st.audio(str(IMG_AUDIO / "musica_fundo.mp3"), format="audio/mp3")
    with col_voltar:
        if st.button("🔙 Voltar", key="btn_voltar_inicio"):
            st.session_state.tela = "inicial"

    st.markdown("---")
    st.subheader("🌿 Kawana ensina com sabedoria:")
    st.image([str(IMG_SPRITES / f"Kawane_latex{i}.png") for i in range(1, 5)], width=250)
    mostrar_legenda("Use sempre instrumentos limpos e respeite o tempo da árvore.")
    mostrar_legenda("Evite cortar profundamente para não ferir a seringueira.")
    mostrar_legenda("Recolha o látex com cuidado e evite desperdício.")

    st.subheader("📝 Caue está anotando tudo com atenção!")
    st.image(str(IMG_SPRITES / "Caue_anotando.png"), width=200)

    if st.button("🎉 Finalizar Fase", key="btn_finaliza"):
        st.audio(str(IMG_AUDIO / "vitoria.wav"), format="audio/wav")
        st.success("Parabéns! Você concluiu a fase 1 com sucesso. 🌱")
        st.balloons()
