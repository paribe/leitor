import streamlit as st
from gtts import gTTS
import os
import pygame

# Criar um dicionário com os idiomas e seus respectivos códigos
languages = {
    "English (Australia)": "en",
    "English (United Kingdom)": "en",
    "English (United States)": "en",
    "English (Canada)": "en",
    "English (India)": "en",
    "English (Ireland)": "en",
    "English (South Africa)": "en",
    "English (Nigeria)": "en",
    "French (Canada)": "fr",
    "French (France)": "fr",
    "Mandarin (China Mainland)": "zh-CN",
    "Mandarin (Taiwan)": "zh-TW",
    "Portuguese (Brazil)": "pt",
    "Portuguese (Portugal)": "pt",
    "Spanish (Mexico)": "es",
    "Spanish (Spain)": "es",
    "Spanish (United States)": "es"
}

# Título da aplicação
st.title('Seleção de Idioma com Reprodução de Áudio')

# Definir o idioma padrão como "Portuguese (Brazil)"
default_language = "Portuguese (Brazil)"
default_index = list(languages.keys()).index(default_language)

# List box para o usuário escolher o idioma com "Portuguese (Brazil)" como padrão
selected_language = st.selectbox("Escolha o idioma:", list(languages.keys()), index=default_index)

# Pegar o código do idioma selecionado
lingua = languages[selected_language]

# Entrada de texto para conversão em áudio
texto = st.text_input("Digite o texto que deseja converter em fala:")

# Botão para gerar o áudio
if st.button("Gerar Áudio"):
    if texto:
        # Conversão de texto para fala
        tts = gTTS(texto, lang=lingua)
        audio_path = "audio.mp3"
        
        # Remover o arquivo de áudio se ele já existir
        if os.path.exists(audio_path):
            os.remove(audio_path)

        tts.save(audio_path)
        
        # Inicializar o mixer do pygame
        pygame.mixer.init()
        
        # Carregar e reproduzir o áudio
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        # Esperar a reprodução terminar antes de tentar excluir o arquivo
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Descarregar o mixer e fechar o pygame
        pygame.mixer.music.unload()
        pygame.mixer.quit()

        # Excluir o arquivo após a reprodução
        if os.path.exists(audio_path):
            os.remove(audio_path)

        st.success("Áudio gerado e reproduzido com sucesso!")
    else:
        st.warning("Por favor, insira um texto para conversão.")
