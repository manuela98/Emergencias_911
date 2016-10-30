import numpy as np
def Datos_necesarios(n,c2):
    Datos =np.loadtxt('tzr.csv', dtype = str, delimiter = ';' and ',')
    necesarios = Datos[1:, [4, 5]]
    lista=[]
    for i in necesarios:
        c=i[0].split(": ")+i[1].split(" ")
        lista+=[c]
    h=[]
    for i in lista:
        if n in i[c2]:
            h+=[i]
    return h

def Consulta():
    c=raw_input("Ingrese Tittle,Description,Date o Hour segun el dato que desea buscar: ")
    n = raw_input("Ingrese el dato que desea buscar: ")
    print "Buscando... Por favor espere."
    print "Debido al tipo de dato este proceso puede tardar un par de minutos"
    if c == "Tittle":
        c2= 0
    if c== "Description":
        c2 = 1
    if c== "Date":
        c2 = 2
    if c == "Hour":
        c2 = 3
    h=Datos_necesarios(n,c2)
    return h
def mark(h):
    title=["Tittle","Description","Date","Hour"]  
    p= ""
    for i in title:
        p = p + '|' + i
    p = p + '|  \n'
    izq = '---|'
    p = p +'|' + izq+izq+izq+izq + '  \n'
    for j in h:

        for i in j:
            p = p + '|' + str(i)
        p = p + '|' + '  \n'
    return p