from flask import Flask,jsonify,request,Response
import sys,os.path
from flask.json import JSONEncoder
sys.path.append("source/")
from cancion import canciones

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True #Activamos el embellecedor de JSON que por defecto está desactivado.

@app.route("/")
def main():
        return jsonify({
    "status": "OK",
    "ejemplo":{
    "Bpms":{
        "ruta":"/bpms",
        "valor": "{Rima: True o False}"
    },
    "Cancion":{
        "ruta":"/song",
        "valor": "{Carga: True o False}"
    },
    "Key":
               { "ruta": "/key",
                 "valor": "{Rima: True o False}"},
    "Internet":
                {"ruta": "/internet",
                "valor": "{Conexion: True o False}"
    }
    }
    })

@app.errorhandler(404)
def page_not_found(error):
  		return "Not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
