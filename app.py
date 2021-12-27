from flask import Flask, request

from OcrController import read_image


app = Flask("OCR-Libras")

@app.route('/teste', methods=['GET'])
def teste():
    return "<p>Conectado ao servidor!</p>"

@app.route('/ocr', methods=['POST'])
def upload():
    file = request.files['upFile']
    return read_image(file)

app.run()