# rootstack
###Prueba de programación

####Requisitos indispensables
1. Usar Git
2. Consumir API provista en esta prueba. La URL base de la aplicación es
http://coding-test.rootstack.net/ A esto agregue el endpoint a llamar, por ejemplo
http://coding-test.rootstack.net/api/jobs. Todos los endpoints requieren autenticación
por bearer token.
Implementar sistema de autenticación. La pantalla para hacer login y obtener el token
de seguridad está aquí (http://coding-test.rootstack.net/api/auth/login)


####Requerimientos funcionales
1. La autenticación deberá persistir entre cierres de browser
2. Debe mostrar la información del usuario (http://coding-test.rootstack.net/api/auth/me)
3. Listar los trabajos (http://coding-test.rootstack.net/api/jobs)
4. Implementar un mapa para mostrar la localización de los trabajos listados
5. Conectar los elementos de la lista de jobs con los pines del mapa de tal forma que
desde la lista se pueda saber cuál es el pin correspondiente en el mapa.
6. Desde el mapa se pueda saber a qué elemento corresponde el pin (haciendo click,
mouseover, infowindow o combinación de las anteriores, como le parezca que sea
más amigable al usuario)
7. Mostrar la ubicación del usuario y su precisión.
8. La interfaz del usuario puede ser simple.