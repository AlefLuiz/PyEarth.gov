import tkinter as tk
from tkinter import filedialog

import cv2 as cv
import os
import pathlib
import numpy as np
import imutils

class APIDigital():
    

    def ProcurarDigital(self, userFile):
        digitais = []
        dim = (1000, 1200)
        # userFile = filedialog.askopenfilename()
        # -- Inicio do processamento da imagem -- #
        userImg = cv.resize(cv.Canny(cv.imread(userFile), 125, 175), dim)
        uContours, uHierarchies = cv.findContours(userImg, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        #cv.imshow('Teste', userImg)

        path = str(pathlib.Path(__file__).parent.resolve()) + '\\database'
        
        for files in os.listdir(path):
            f = os.path.join(path, files)
            if os.path.isfile(f):
                baseImg = cv.resize(cv.Canny(cv.imread(f), 125, 175), dim)
                bContours, bHierarchies = cv.findContours(baseImg, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
                if len(uContours) == len(bContours):
                    digitais.append(f.split("\\")[-1])
        return digitais
