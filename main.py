import os
import streamlit as st
from pytube import YouTube
from pathlib import Path

# Récupérer le chemin du dossier de téléchargement par défaut
def get_default_download_path():
    download_path = str(Path.home() / "Downloads")  # Dossier de téléchargement par défaut sur la plupart des systèmes
    if os.name == "nt":  # Si le système d'exploitation est Windows
        download_path = str(Path.home() / "Desktop")  # Téléchargement sur le bureau
    return download_path

# Fonction de téléchargement de vidéo
def download_video(url, output_path):
    try:
        st.write("Téléchargement en cours...")
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(output_path)
        st.success("Téléchargement terminé !")
    except Exception as e:
        st.error(f"Une erreur s'est produite : {str(e)}")

# Interface Streamlit
def main():
    st.title("Téléchargeur de vidéos YouTube")
    url = st.text_input("Entrez le lien de la vidéo YouTube")
    output_path = st.text_input("Entrez le chemin de sortie pour la vidéo", get_default_download_path())
    if st.button("Télécharger"):
        if not url or not output_path:
            st.warning("Veuillez fournir le lien de la vidéo et le chemin de sortie.")
        else:
            download_video(url, output_path)

if __name__ == "__main__":
    main()
