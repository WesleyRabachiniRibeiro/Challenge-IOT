import datetime
import pyautogui
import cv2
import numpy

# Tira print da tela e escreve o nome do arquivo
foto = pyautogui.screenshot()
nomeArquivo = datetime.datetime.now().strftime('%d-%m-%Y_%H%M%S' + '.png')


# Salva Screen
def Screen():
    foto.save('./img/' + nomeArquivo)

# Mostra Screen
def ShowScreenShot():
    imagem = numpy.array(foto)
    imagem = imagem[:, :, ::-1].copy()
    cv2.imshow(f"{nomeArquivo}", imagem)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
# pip install pyautogui
