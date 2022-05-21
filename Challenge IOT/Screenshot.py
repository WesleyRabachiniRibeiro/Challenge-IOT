import datetime
import pyautogui
import cv2
import numpy

foto = pyautogui.screenshot()
nomeArquivo = datetime.datetime.now().strftime('%d-%m-%Y_%H%M%S' + '.png')


def Screen():
    foto.save('./img/' + nomeArquivo)


def ShowScreenShot():
    imagem = numpy.array(foto)
    imagem = imagem[:, :, ::-1].copy()
    cv2.imshow(f"{nomeArquivo}", imagem)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
# pip install pyautogui
