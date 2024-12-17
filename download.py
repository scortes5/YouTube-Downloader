# YouTube Download videos
import os
from yt_dlp import YoutubeDL

def download_video(url, output_path=None):
    try:
        # Set default output path if none provided
        if output_path is None:
            output_path = f"{os.getcwd()}/Downloads"
        
        # Create Downloads directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        # Download the video using yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'progress_hooks': [lambda d: print(f"Descargando... {d['_percent_str']}") if d['status'] == 'downloading' else None],
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Descarga Completa!")
    
    except Exception as e:
        print(f"A ocurrido un error: {str(e)}")
