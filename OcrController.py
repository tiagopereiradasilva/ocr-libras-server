#coding: utf-8
from datetime import datetime
import pytesseract
import cv2
import re
from PIL import Image

#executando tesseract instalado no servidor a partir de seu caminho absoluto
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Tiago\Desktop\OCR-Libras\Tesseract-OCR\tesseract.exe'

#alfabeto com caracteres a serem filtrados
alfabeto = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
			'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
			',', 'Ç', 'Ã', 'Á', 'Â', 'À', 'É', 'Ê', 'Í', 'Ó', 'Ô', 'Õ', 'Ú'
            , '!', '?', ':', '.', ' '}

def read_image(file):
        
    #converts formData to image
    image = Image.open(file)
    image.save("image.png", "PNG")

    #carregando imagem com cv2 (para orperacoes opencv)
    img = cv2.imread("image.png")

    #convertenco imagem para escala de cinza
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #tirando ruidos da imagem
    rect, thresh = cv2.threshold(imgGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #salvando imagem editada.
    cv2.imwrite("imagemGray.png", thresh)

    #reads text from image
    text = pytesseract.image_to_string(image, config='-l por')
    
    #removendo quebras de linha
    text = text.replace("\n"," ")

    #removendo espaços extras.
    text = re.sub("\s+", " ", text)
    
    #colocando texto em caixa alta
    text = text.upper()
    textFinal = ""

    contador = 0
    #filtrando caracteres que pertencem ao alfabeto definido
    while contador < len(text):
        if text[contador] in alfabeto:
            textFinal+=text[contador]
        contador+=1

    return textFinal

