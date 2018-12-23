from flask import Flask,jsonify,request,Response,render_template
import sys,os.path
import json
from flask.json import JSONEncoder
sys.path.append("source/")
import cancion
import db

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

@app.route("/aniadir/<nombre>/<artista>/<float:bpm>/<int:n>/<l>", methods=['GET'])
def aniadir(nombre,artista,bpm,n,l):
	db.insertar_cancion(nombre,artista,bpm,n,l)
	return jsonify(status="Cancion insertada correctamente")

@app.route("/eliminar/<nombre>", methods=['GET'])
def eliminar(nombre):
	db.borrar_cancion(nombre)
	return jsonify(status="Cancion eliminada correctamente")
        
@app.route("/mostrar")
def mostrar():
	return jsonify(db.mostrar_canciones())

@app.route("/compararBPMS/<nombre>/<otra>")
def compararBPMS(nombre,otra):
	if(cancion.compararBPMS(nombre,otra)):
		return jsonify(status="Canciones suenan bien")
	else:
		return jsonify(status="Canciones suenan mal")

@app.route("/compararKey/<nombre>/<otra>")
def compararKey(nombre,otra):
	if(cancion.compararKey(nombre,otra)):
		return jsonify(status="Canciones suenan bien")
	else:
		return jsonify(status="Canciones suenan mal")

@app.route("/recomendacion/<nombre>")
def recomendacion(nombre):
	return jsonify(db.buscar_adecuadas(nombre))

@app.route('/status')
def status():
	return jsonify(status="OK")

@app.errorhandler(404)
def page_not_found(error):
  		return "Not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
