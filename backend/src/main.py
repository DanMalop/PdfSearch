#!/usr/bin/env python3  

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pdfSearch import search
from routes.files import routes_files
import os
import platform

opSystem = platform.system()
port = 5000

app = Flask(__name__, template_folder='./')
CORS(app)    # Necesario para seguir las politicas CORS de coneccion entre servidores

app.register_blueprint(routes_files)
app.config['UPLOAD_FOLDER'] = "Files"
ALLOWED_EXTENSIONS = set(["pdf"])

@app.route('/generate_inform', methods=['POST'])
def generateInform():
    clientRequest = request.json
    print(f"la peticion => {clientRequest}")
    keyword = clientRequest['keyword']
    scope = int(clientRequest['scope'])
    #folder = f"{os.getcwd()}/../bacteriaFiles/LDPE" if opSystem != 'Windows' else f"{os.getcwd()}\..\\bacteriaFiles\\LDPE"
    folder = f"{os.getcwd()}/files" if opSystem != 'Windows' else f"{os.getcwd()}\\files"
    ignoreSpaces = clientRequest['ignoreSpaces']
        
    response = jsonify(search(folder, keyword, scope, ignoreSpaces))
    response.headers.add('Access-Control-Allow-Origin', '*') # se inclulle en el header para las politicas CORS
    return response

# @app.route('/document/<string:document_name>')
# def getDocument(document_name):
#     print(document_name)
#     documentsFound = [document for document in inform if document == document_name]
#     if len(documentsFound) > 0:        
#         return jsonify({"document": inform[documentsFound[0]]})
#     else:        
#         return jsonify({"message": "document not found"})

if __name__ == '__main__':
    app.run(debug=True, port=port, host="0.0.0.0")