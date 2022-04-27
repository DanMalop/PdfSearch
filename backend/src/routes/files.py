from flask import Blueprint, request
from os import getcwd
from responses.response_json import response_json

routes_files = Blueprint("routes_files", __name__)

PATH_FILE = f"{getcwd()}/files/"

@routes_files.post("/upload")   # Ruta para subir los archivos
def upload_file():
    try:
        file = request.files["file"]
        file.save(f"{PATH_FILE}{file.filename}")
        response = response_json("succes")
        response.headers.add('Access-Control-Allow-Origin', '*') # se inclulle en el header para las politicas CORS
        return response
    
    except FileNotFoundError:
        response = response_json("folder not found", 404)
        response.headers.add('Access-Control-Allow-Origin', '*') # se inclulle en el header para las politicas CORS
        return response
    
# @routes_files.get("/file/<string:name_file>")
# def get_file():
    