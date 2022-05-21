import os
from random import randint
import pygame
from moviepy.editor import VideoFileClip

from Speaker import Speaker


def TocarMusicaAleatoriaBaixada():
    arq = []
    music = []

    for _, _, arquivo in os.walk('./video'):
        for name in arquivo:
            arq.append(name)
    for _, _, arquivo in os.walk('./music'):
        for name in arquivo:
            music.append(name)
    while True:
        video_name = arq[randint(0, len(arq) - 1)]
        if os.path.exists("./music/" + video_name[:-4] + ".mp3"):
            break
        if len(music) == len(arq):
            break
        else:
            video = VideoFileClip(os.path.join("./video/" + video_name))
            video.audio.write_audiofile(os.path.join("./music/" + video_name[:-4] + ".mp3"))
            break
    pygame.init()
    pygame.mixer.music.load("./music/" + video_name[:-4] + ".mp3")
    Speaker("Aperte Enter para parar a música")
    pygame.mixer.music.play()
    input("Press Enter:")
