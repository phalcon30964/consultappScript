1. Cuando la maquina virtual arranque saldra el siguiente mensaje: root@IP's password:, anotar la IP que salga.

Luego ejecutar los siguientes comandos.

cd /myproject/
. ejecutar.sh
. /myproject/venv/bin/activate
 python consultappScript/consultapp.py

Para hacer una peticion remplazar con la ip del punto 1.

---------------Para servicio de inicio de sesion----------------------------:
-Formato de la peticion: 
/cliente/email/password
-Casos de prueba:
IP:5000/cliente/cdlopezmorcillo@gmail.com/1234
IP:5000/cliente/john@gmail.com/123456
IP:5000/cliente/munozm@gmail.com/654321
IP:5000/cliente/cualquierotracosa/cualquierotracosa -> por el mometo si lo enviado no existe se devuelve una error de notfound.

CONSTANTES DE ESTADO:
ACTIVO
DESACTIVO

CONSTANTES DE TIPO IDENTIFICACION:
CEDULA
TARJETA_DE_IDENTIFICACION
PASAPORTE

JHON
TIENE QUE HACER COMPROBACIÓN DE QUE SEA CONTRASEÑA CORRECTA.
MIRAR QUE EL NUMERO DE TELÉFONO SEA NUMERO, Y QUE NO TENGA ESPACIOS.
MIRAR QUE LA IDENTIFICACIÓN NO TENGA PUNTOS.
MIRAR QUE EL CORREO TENGA FORMATO DE CORREO.

---------------Para Categorias----------------------------:


JHON, hay
21474 CATEGORIAS POSIBLES
100000 SUBCATEGORIAS POR CATEGORIA POSIBLES

---------------Para Subcategorias----------------------------:


---------------Para MedioPago----------------------------:
Jhon
TIENE QUE VERIFICAR QUE EL MAIL INTRODUCIDO PARA PAYPAL TENGA EL FORMATO CORRECTO
TIENE QUE VERIFICAR QUE EL NUMERO DE TARJETA DE CREDITO ESTE EN EL RANGO PERMITIDO
TIENE QUE VERIFICAR QUE EL CODIGO DE SEGURIDAD SEGUN LA TARJETA ESTE EN EL RANGO PERMITIDO

Constantes de tipo:
CREDITO_VISA
CREDITO_MASTERCARD
CREDITO_AMEX
BITCOIN
PAYPAL


Jhon
TIENE QUE HACER COMPROBACION DE QUE SEA CONTRASEÑA CONRRECTA.
Mirar que el numero de telefono sea numero, y que no tenga espacios.
Mirar que la idenficacion no tenga puntos.
Mirar que el correo tenga formato de correo.

Christian
Definir como se guarda la imagen del usuario.