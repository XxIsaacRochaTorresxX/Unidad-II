'''
Tema: conjuntos
Fecha: 05 de septiembre del 2022
Autor: Isaac Rocha Torres
'''
'''
# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).

c1 = {1,2,3,4,5} #no acepta duplicados
c2 = set([i for i in range(0,11,2)])
c3 = set()

print(c1)
print(c2)
print(c3)

#    Usando la función forezenset. es inmutable y su contenido no puede ser modificado
#    una vez que ha sido inicializado

c4 = frozenset([chr(letra) for letra in range(65,90)])
print(c4)
#    Los elementos repetidos se eliminan


# 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
#    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
#    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
#    a través de un índice.

# 4. Añadir elementos: con el método add() ó con el método update()
#    Agregar el numero 8 al conjunto c

c1.add(10)
print(c1)

c1.update({22,30,80}) # solo es para lista
print(c1)
c1.update(["hola", "mundo"]) # solo es para lista
print(c1)
#    Agregar varios elementos al conjunto


# 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
#    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
#    en caso de no existir el elemento

c1.discard(22)
c1.discard(22)

c1.remove(100)
print(c1)

#     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
#     excepcion KeyError.

c1.pop()
print(c1)



#    El método clear() elimina todos los elementos del conjunto

c2.clear()
print(c2)
#    Número de elementos en un conlunto con la función len()
print("Número de elementos del conjunto c1: ", len(c1))

#    Verificar si un elemento esta dentro de un conjunto

print(80 in c1)
'''
# ************************ Operaciones con conjuntos
'''
cP = set([num for num in range (0,20,2)])
cI = set([num for num in range (1,22,1)])


# 1. Union  ( | )
print(cP | cI)

# 2. Intersección ( & )
cI.update([2,4,8,10])
print(cP & cI)

# 3. Diferencia ( - )
print(cP)
print(cI)

print(cP - cI)


# 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
#    que no son comunes.

print(cP ^ cI)

# 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
#    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6,7}

print( s1 <= s2)

# 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
#    es decir, la intersección de A y B es el conjunto vacío.


# 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
#    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
#    del otro.

a1 = {1,2,3}
a2 = {1,2}

print(a1== a2)


Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"",
                "Promedio":
            },
            {
                "Nombre":"",
                "Promedio":
            },
            . . . 
        ],
        "Promedio general": 
   }


'''

def Estudiantes():

    arch = "Estudiantes.txt"
    fh = open(arch, 'r')
    estudent = set()
    for renglon in fh:
        estudent.add((renglon [0:8], renglon[8:-1]))
    return estudent

def Materias():

    arch = "Kardex.txt"
    fk = open(arch, 'r')
    materias = set()
    for renglon in fk:
        mat = renglon.split("|")
        prom = int(str(mat[2]))
        materias.add((renglon [0:8], mat [1], prom))
    return materias

#print(Estudiantes())


def Kardex(ctrl):
    lista1= set()
    lista1.update(Estudiantes())
    lista2 = set()
    lista2.update(Materias())

    no = str(ctrl)
    print(no)
    for ctrl1 in lista1:
        for ctrl2 in lista2:
            if ctrl1[0]== no:
             if  ctrl2[0]== no:
                 kardex={}
                 kardex["Nombre: "] = ctrl1[1]
                 kardex["Materias: "] = ctrl1[1]
                print(ctrl1, ctrl2)


Kardex(int(input()))