from flask import Flask
from collections import OrderedDict
import json

app = Flask(__name__)

@app.route("/cliente/<email>/<password>")
def inicioSesion(email,password):
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
		
@app.route("/categorias/getAll")
def getcategoria():
	ret={}
	ret['CategoriaDTO']=[]
	category=OrderedDict([('idCategoria',1),('nombreCategoria;',"salud"),('descripcion;',"Consultas de salud")])
	ret['CategoriaDTO'].append(category)
	category=OrderedDict([('idCategoria',2),('nombreCategoria;',"leyes"),('descripcion;',"Consultas de ley")])
	ret['CategoriaDTO'].append(category)
	category=OrderedDict([('idCategoria',3),('nombreCategoria;',"deportes"),('descripcion;',"Consultas de deportes")])
	ret['CategoriaDTO'].append(category)
	category=OrderedDict([('idCategoria',4),('nombreCategoria;',"educacion"),('descripcion;',"Consultas de educacion")])
	ret['CategoriaDTO'].append(category)
	
	return json.dumps(ret)
	
@app.route("/subcategorias/<int:idCategoria>")
def getsubcategoria(idCategoria):
	ret={}
	ret['SubcategoriaDTO']=[]
	if idCategoria==1:
		subcategory=OrderedDict([('nombreSubcategoria;',"Enfermedades"),('descripcion;',"Consultas de enfermedades"),('idSubcategoria;',100001),('idCategoria',1),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Comida saludable"),('descripcion;',"Consultas de comida saludable"),('idSubcategoria;',100002),('idCategoria',1),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Medicina"),('descripcion;',"Consultas de medicina"),('idSubcategoria;',100003),('idCategoria',1),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"EPS"),('descripcion;',"Consultas de EPS"),('idSubcategoria;',100004),('idCategoria',1),])
		ret['SubcategoriaDTO'].append(subcategory)
		return json.dumps(ret)
	if idCategoria==2:
		subcategory=OrderedDict([('nombreSubcategoria;',"Demandas"),('descripcion;',"Consultas de enfermedades"),('idSubcategoria;',200001),('idCategoria',2),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Decretos"),('descripcion;',"Consultas de comida saludable"),('idSubcategoria;',200002),('idCategoria',2),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Denuncias"),('descripcion;',"Consultas de medicina"),('idSubcategoria;',200003),('idCategoria',2),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Estatutos"),('descripcion;',"Consultas de EPS"),('idSubcategoria;',200004),('idCategoria',2),])
		ret['SubcategoriaDTO'].append(subcategory)
		return json.dumps(ret)
	if idCategoria==3:
		subcategory=OrderedDict([('nombreSubcategoria;',"Futbol"),('descripcion;',"Consultas de enfermedades"),('idSubcategoria;',300001),('idCategoria',3),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Basquetball"),('descripcion;',"Consultas de comida saludable"),('idSubcategoria;',300002),('idCategoria',3),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Rutinas"),('descripcion;',"Consultas de medicina"),('idSubcategoria;',300003),('idCategoria',3),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Lesiones"),('descripcion;',"Consultas de EPS"),('idSubcategoria;',300004),('idCategoria',3),])
		ret['SubcategoriaDTO'].append(subcategory)
		return json.dumps(ret)
	if idCategoria==4:
		subcategory=OrderedDict([('nombreSubcategoria;',"Matematicas"),('descripcion;',"Consultas de enfermedades"),('idSubcategoria;',400001),('idCategoria',4),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Ciencias sociales"),('descripcion;',"Consultas de comida saludable"),('idSubcategoria;',400002),('idCategoria',4),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Biologia"),('descripcion;',"Consultas de medicina"),('idSubcategoria;',400003),('idCategoria',4),])
		ret['SubcategoriaDTO'].append(subcategory)
		subcategory=OrderedDict([('nombreSubcategoria;',"Quimica"),('descripcion;',"Consultas de EPS"),('idSubcategoria;',400004),('idCategoria',4),])
		ret['SubcategoriaDTO'].append(subcategory)
		return json.dumps(ret)
	else:
		return "categoriaNoExiste"

@app.route("/") 
def version():
	return "Consultap V1.0"

if __name__ == "__main__":
	app.run('0.0.0.0', debug=True ,port=5000)
