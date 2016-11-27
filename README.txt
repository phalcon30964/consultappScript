login: root
password: 123456

Asegurese de que cuenta con conexion a internet.

1. Cuando la maquina virtual arranque saldra el siguiente mensaje: root@IP's password:, anotar la IP que salga.

Luego ejecutar los siguientes comandos.

Si es la primeara vez: iptables -I INPUT -p tcp --dport 5000 -j ACCEPT

cd /myproject/
. ejecutar.sh
. /myproject/venv/bin/activate
 python consultappScript/consultapp.py

Para hacer una peticion remplazar con la ip del punto 1.

---------------Para servicio de inicio de sesion----------------------------:
-Formato de la peticion: 
/cliente/email/password
-Metodo: 
GET
-Casos de prueba:
IP:5000/cliente/cdlopezmorcillo@gmail.com/1234
IP:5000/cliente/john@gmail.com/123456
IP:5000/cliente/munozm@gmail.com/654321
IP:5000/cliente/cualquierotracosa/cualquierotracosa -> clienteNoExiste

CONSTANTES DE ESTADO:
ACTIVO
INACTIVO

CONSTANTES DE TIPO IDENTIFICACION:
CEDULA
TARJETA_DE_IDENTIFICACION
PASAPORTE

John
TIENE QUE HACER COMPROBACIÓN DE QUE SEA CONTRASEÑA CORRECTA.
MIRAR QUE EL NUMERO DE TELÉFONO SEA NUMERO, Y QUE NO TENGA ESPACIOS.
MIRAR QUE LA IDENTIFICACIÓN NO TENGA PUNTOS.
MIRAR QUE EL CORREO TENGA FORMATO DE CORREO.

---------------Para MedioPago----------------------------:
-Formato de la peticion: 
/mediopago/email/password
-Metodo: 
GET
-Casos de prueba:
IP:5000/mediopago/cdlopezmorcillo@gmail.com/1234 -> clienteSinMedioPago
IP:5000/mediopago/john@gmail.com/123456
IP:5000/mediopago/munozm@gmail.com/654321
IP:5000/mediopago/cualquierotracosa/cualquierotracosa -> clienteNoExiste

John
TIENE QUE VERIFICAR QUE EL MAIL INTRODUCIDO PARA PAYPAL TENGA EL FORMATO CORRECTO
TIENE QUE VERIFICAR QUE EL NUMERO DE TARJETA DE CREDITO ESTE EN EL RANGO PERMITIDO
TIENE QUE VERIFICAR QUE EL CODIGO DE SEGURIDAD SEGUN LA TARJETA ESTE EN EL RANGO PERMITIDO

Constantes de tipo:
CREDITO_VISA
CREDITO_MASTERCARD
CREDITO_AMEX
BITCOIN
PAYPAL

---------------Para Categorias----------------------------:
-Formato de la peticion: 
/categorias/getAll
-Metodo: 
GET
-Casos de prueba:
IP:5000/categorias/getAll

John, hay
21474 CATEGORIAS POSIBLES, MAXIMO
100000 SUBCATEGORIAS POR CATEGORIA POSIBLES, MAXIMO

---------------Para Subcategorias----------------------------:

-Formato de la peticion: 
/subcategorias/idCategoria
-Metodo: 
GET
-Casos de prueba:
IP:5000/subcategorias/1
IP:5000/subcategorias/2-> noHaySubCategorias
IP:5000/subcategorias/3
IP:5000/subcategorias/4
IP:5000/subcategorias/otronumero -> categoriaNoExiste
IP:5000/subcategorias/letras -> not found 

---------------Para registro----------------------------:
ip:5000/mediopago/crear
ip:5000/cliente/crear

-Metodo: 
POST
-Casos de prueba:
ip:5000/mediopago/crear -> con post = ok, con get =error
ip:5000/cliente/crear -> con post = ok, con get =error

Jhon
TIENE QUE HACER COMPROBACION DE QUE SEA CONTRASEÑA CONRRECTA.
Mirar que el numero de telefono sea numero, y que no tenga espacios.
Mirar que la idenficacion no tenga puntos.
Mirar que el correo tenga formato de correo.

Christian
Definir como se guarda la imagen del usuario.
