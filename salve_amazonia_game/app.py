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
