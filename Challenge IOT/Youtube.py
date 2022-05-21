from pytube import YouTube, streams
import webbrowser as wb
from pathlib import Path


# Método para pesquisar video no Youtube
from Speaker import Speaker


def PesquisarVideo(video):
    count = 0
    # Cortar str para tudo depois de pesquisar
    video = video.lower().split()
    for v in video:
        if v == "pesquisar":
            while count >= 0:
                video.pop(count)
                count -= 1
        count += 1
    search_video = ' '.join(video)

    url = f"https://www.youtube.com/results?search_query={search_video}"
    wb.open(url)


# Método para baixar video no Youtube
def DownloadVideo():
    # downloads_path = str(Path.home() / "Downloads") # Path Relativo para pasta Download
    Speaker('Digite a Url do video que deseja que Nolan baixe')
    url = input('Digite a Url do video:' )
    Speaker('Download em andamento')
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()

    stream.download(output_path='./video/')
    Speaker('Nolan terminou de fazer o download')
