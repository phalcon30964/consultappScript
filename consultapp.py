from flask import Flask
from collections import OrderedDict
import json

app = Flask(__name__)

@app.route("/cliente/<email>/<password>")
def hello(email,password):
	ret={}
	if email == "john@gmail.com" and password == "123456":
		client=OrderedDict([('estado', "ACTIVO"),('nombres',"john"),('apellidos',"osorio"),('email',"john@gmail.com"),('password',"123456"),('telefono',"3152543235"),('fechaNacimiento',"05/05/95"),('urlFoto',"http://www.icesi.edu.co/imgs/contenido/png/logo_icesi.png"),('identificacion',"13107019"),('tipoIdentificacion',"CEDULA")])	
		ret['ClienteDTO'] =(client)
		return json.dumps(ret)
	elif email == "cdlopezmorcillo@gmail.com" and password == "1234":
		client=OrderedDict([('estado', "ACTIVO"),('nombres',"christian david"),('apellidos',"Lopez morcillo"),('email',"cdlopezmorcillo@gmail.com"),('password',"1234"),('telefono',"3015147161"),('fechaNacimiento',"05/05/95"),('urlFoto',"http://www.icesi.edu.co/imgs/contenido/png/logo_icesi.png"),('identificacion',"1144169711"),('tipoIdentificacion',"TARJETA_DE_IDENTIFICACION")])
		ret['ClienteDTO'] =(client)
		return json.dumps(ret)
	elif email == "munozm@gmail.com" and password == "654321":
		client=OrderedDict([('estado', "ACTIVO"),('nombres',"juan david"),('apellidos',"munoz moreno"),('email',"munozm@gmail.com"),('password',"654321"),('telefono',"3173005973"),('fechaNacimiento',"05/05/95"),('urlFoto',"http://www.icesi.edu.co/imgs/contenido/png/logo_icesi.png"),('identificacion',"123456789"),('tipoIdentificacion',"PASAPORTE")])
		ret['ClienteDTO'] =(client)
		return json.dumps(ret)
	else:
		return "clienteNoExiste"

@app.route("/") 
def hello3():
	return "Consultap V1.0"

if __name__ == "__main__":
	app.run('0.0.0.0', debug=True ,port=5000)
