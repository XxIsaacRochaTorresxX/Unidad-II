'''
Tema: Diccionarios, archivos y formato JSON
Fecha: 02 de septiembre del 2022
Autor: Leonardo Martínez González
'''

# 1. Definición. Colección no ordenada de objetos. Está formada por un PAR clave: valor.
#    Las claves pueden ser números, cadenas o cualquier otro tipo inmutable.
#    Los valores pueden ser de cualquier tipo, incluso otros diccionarios.

# 2. Crear diccionarios

# 3. Acceder a sus valores. Se accede igual que las listas pero por su clave en lugar del indice
#    Si no existe la clave se lanza la excepcion KeyError

# 4. Recorrer un diccionario por su clave.

# 5. Recorrer un diccionario por su valor

# 6. Recorrer un diccionario por clave: valor

# 7. Agregar elementos a un diccionario

# 8. Eliminar elementos con del

# 9. Modificar, accesando directo a la posición

# 10. Algunas operaciones comunes
#     Contar elementos

#     Saber si existe un elemento dentro de un diccionario (solo por clave)

#     Para vaciar un diccionario

#     Unir o actualizar dos diccionarios

#     Sacar un elemento del diccionario con pop() muy parecido a get(), pero pop(),
#     regresa el elemento y lo elimina del diccionario

#      Tambien acepta devolver un valor por defecto pop(clave, "valor por defecto)

#      popitem() regresa un elemento (par clave:valor) de forma aleatoria y lo remueve
#      si no existe genera una excepción KeyError

#      generar un diccionario a partir de una lista con el metodo fromkeys() con valores
#      por defecto con valor None o 0 (CERO)

'''
Defina un diccionario Estudiantes, que:
Almacene datos personales y todas las materia que ha cursado con sus promedios.
Las actividades complemetarias que ha tomado.
'''


'''
El directorio de los clientes de una empresa está organizado en una cadena de texto como la de
más abajo, donde cada línea contiene la información: nombre, email, teléfono, nss, y el descuento
que se le aplica. Las líneas se separan con el carácter de cambio de línea \n 
y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

"NSS;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

Escribir un programa que genere un diccionario con la información del directorio, 
donde cada elemento corresponda a un cliente y tenga por clave su NSS y por valor otro diccionario
con el resto de la información del cliente. Los diccionarios con la información de cada cliente
tendrán como claves los nombres de los campos y como valores la información de cada cliente
correspondientes a los campos. Es decir, un diccionario como el siguiente:

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
{'01234567L': {'Nombre': 'Luis González', 'Email': 'luisgonzalez@mail.com', 'Telefono': '656343576', 'Descuento': 12.5}, '71476342J': {'Nombre': 'Macarena Ramírez', 'Email': 'macarena@mail.com', 'Telefono': '692839321', 'Descuento': 8.0}, '63823376M': {'Nombre': 'Juan José Martínez', 'Email': 'juanjo@mail.com', 'Telefono': '664888233', 'Descuento': 5.2}, '98376547F': {'Nombre': 'Carmen Sánchez', 'Email': 'carmen@mail.com', 'Telefono': '667677855', 'Descuento': 15.7}}
considere el método de cadena split() que separa una cadena de acuerdo al caracter que se le pase
'''


'''
Ejercicio: Crear un diccionario con los códigos postales y su localidad del estado de San Luis Potosi,
           para ello descargue la tabla de códigos postales de la siguiente dirección: 
           https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx
           
           el formato del diccionario  tendra la forma:
           {109159: {'CP': '78000', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, 
           109160: {'CP': '78037', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, . . . }
           
           Genere una lista con los VALORES del diccionario anterior.
           Guarde en un archivo con formato JSON los resultados
           
           Consideraciones:
           1. El método split regresa un arreglo al separar una cadena en subcadenas.
           2. El municipio se encuentra en la posición 4.
           3. El estado se llama: "San Luis Potosí"
'''



'''
Formto  JSON
Formato ligero de intercambio de datos
medio de comunicación estadarizado entre lenguajes de programación

en Python se leen facilmente archivos JSON 
import json #libreria que maneja este formato
with open("Nombre_archivo", 'w') as archivo:
        json.dump( Lista_de_diccionario, archivo) # dump es disparar

Las lineas anteriores graban un archivo y su contenido es en formato JSON

'''