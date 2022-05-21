from FaceRecognize import FaceDetection
from Screenshot import Screen, ShowScreenShot
from Speaker import Speaker
from TocarMusica import TocarMusicaAleatoriaBaixada
from VoiceCommand import Voice
from Youtube import PesquisarVideo, DownloadVideo

while True:
    try:
        if Voice().lower() == "ok nolan":
            Speaker("Nolan ao seu Dispor! Mestre, O que quer que Nolan faça?")
            comando = Voice().lower()
            print(comando)
            if comando == 'tirar print da tela':
                Screen()
                Speaker("Nolan tirou a print com Sucesso! meu senhor")
                ShowScreenShot()
            if comando == 'pesquisar vídeo no youtube':
                Speaker('Qual video você quer que Nolan pesquise?')
                PesquisarVideo(Voice().lower())
            if comando == 'baixar vídeo':
                DownloadVideo()
            if comando == 'tocar música':
                TocarMusicaAleatoriaBaixada()
            if comando == 'abrir câmera':
                Speaker('Ok, aperte Esc quando quiser sair')
                FaceDetection()
        else:
            Speaker("Você não é o meu mestre! Nolan irá te enfrentar! AVADA KEDAVRA")
    except Exception as erro:
        Speaker("Você não é o meu mestre! Nolan irá te enfrentar! SPECTRO PATRONO")
