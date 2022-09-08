import json

archivo = open("CPdescarga.txt")
lineas = archivo.readlines()
lista = {}
for lin in lineas[2:]:
    codigos = {}
    cod = lin.split("|")
    if cod[4] == "San Luis Potosí":
        codigos["Codigo Postal"] = cod[6]
        codigos["Municipio"] = cod[3]
        codigos["Estado"] = cod[4]
        lista[cod[0]] = codigos
print(lista)

with open("listap.json", "w") as file:
    json.dump(lista, file, indent=4)