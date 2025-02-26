import yt_dlp
import requests
from transformers import pipeline
import torch
torch.cuda.empty_cache()
def obter_transcricao(url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["pt", "en"],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if "automatic_captions" in info:
            captions = info["automatic_captions"].get("pt", []) or info["automatic_captions"].get("en", [])
            if captions:
                response = requests.get(captions[0]["url"])
                return response.text
    return None

def resumir_texto(texto):
    resumo_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=0)
    resumo = resumo_pipeline(texto, max_length=150, min_length=50, do_sample=False, batch_size=1)
    return resumo[0]["summary_text"]

if __name__ == "__main__":
    url_video = input("Digite a URL do vídeo do YouTube: ")
    transcricao = obter_transcricao(url_video)
    if transcricao:
        print("\nResumo do vídeo:")
        print(resumir_texto(transcricao))
    else:
        print("Nenhuma transcrição encontrada para este vídeo.")