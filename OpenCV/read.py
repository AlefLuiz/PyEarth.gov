import tkinter as tk
from tkinter import filedialog

import cv2 as cv
import os

acesso = False
root = tk.Tk()
root.withdraw()

dim = (1000, 1200)

userFile = filedialog.askopenfilename()

# -- Inicio do processamento da imagem -- #
userImg = cv.resize(cv.Canny(cv.imread(userFile), 125, 175), dim)
uContours, uHierarchies = cv.findContours(userImg, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow('Teste', userImg)

for files in os.listdir('database'):
    f = os.path.join('database', files)
    if os.path.isfile(f):
        baseImg = cv.resize(cv.Canny(cv.imread(f), 125, 175), dim)
        bContours, bHierarchies = cv.findContours(baseImg, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        if len(uContours) == len(bContours):
            print('Bem vindo!')
            break
        else:
            print('Digital não encontrada no sistema!')

cv.waitKey(0)





