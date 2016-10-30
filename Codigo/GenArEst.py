import datetime
import time
import numpy as np
def Texto(): #Escribe un texto.txt que contiene title,description,Date,Hour,Day,Month
    Datos =np.loadtxt('tzr.csv', dtype = str, delimiter = ';' and ',')
    necesarios = Datos[1:, [4, 5]]
    lista=[]
    pih=[]
    for i in necesarios:
        c=i[0].split(": ")+i[1].split(" ")
        g=c[2].split("-")
        o = datetime.date(int(g[0]),int(g[1]),int(g[2])).strftime("%A")
        m=datetime.date(int(g[0]),int(g[1]),int(g[2])).strftime("%b")
        lista += c+[o]+[m]
    return lista
outfile = open('texto.txt','w')
outfile.write('title'+","+'description'+","+'Date'+","+'Hour'+","+'Day'+","+"Month"+'\n')
ls = Texto()

oj = []
u = 0

while u<=2000000: 
    oj = ls[u]+","+ls[u+1]+","+ls[u+2]+","+ls[u+3]+","+ls[u+4]+","+ls[u+5]+"\n"
    u += 6
    outfile.write(str(oj))
    if u==len(ls):
        break
outfile.close()

def Numday(x):#Genera un archivo semana.txt 
    Datos =np.loadtxt('tzr.csv', dtype = str, delimiter = ';' and ',')
    necesarios = Datos[1:,[5]]
    a=[]
    u=[]
    po=[]
    g=[] 
    k=[]
    p=[]
    for i in necesarios:
        c=i[0].split(" ")
        a+=[c[0]]
    for t in a:
        u+=[t.split("-")]

    for m in u:
        po+=[[int(m[0]),int(m[1]),int(m[2])]]
        if datetime.date(int(m[0]),int(m[1]),int(m[2])).strftime("%A")==x:
            lu=str(m[0]+"-"+m[1]+"-"+m[2]) 
            if lu not in g:
                g+=[str(m[0]+"-"+m[1]+"-"+m[2])]  
    return len(g)
d=["Friday","Monday","Saturday","Sunday","Thursday","Tuesday","Wednesday"]
outfile=open("semanas.txt","w")
outfile.write("Friday,Monday,Saturday,Sunday,Thursday,Tuesday,Wednesday"+"\n")
for i in d:
    k=Numday(i)
    yu=str(k)+","
    outfile.write(str(yu))
outfile.write("\n")
outfile.close()
def Trafico(): #Genera un archivo Trafico.txt
    outfile=open("Trafico.txt","w")
    outfile.write("Trafico,Dia\n")
    i=[]
    Datos =np.loadtxt('texto.txt', dtype = str, delimiter = ';' and ',')
    necesarios = Datos[1:, [0, 4]]
    for r in necesarios:
        if r[0]=="Traffic":
            i=r[0]+","+r[1]+"\n"
            outfile.write(i)
    outfile.close()
            
    return 0
o=Trafico()

def Fall_victim():  #Genera un archivo Fall_victim.txt
    outfile=open("Fall_victim.txt","w")
    outfile.write("Victim,Month\n")
    i=[]
    Datos =np.loadtxt('texto.txt', dtype = str, delimiter = ';' and ',')
    necesarios = Datos[1:, [1, 5]]
    for r in necesarios:
        if r[0]=="FALL VICTIM":
            i=r[0]+","+r[1]+"\n"
            outfile.write(i)
    outfile.close()
            
    return 0
y=Fall_victim()



def Allergic():#Genera un archivo Fall_victim.txt
    outfile=open("Allergic.txt","w")
    outfile.write("Allergic,Month\n")
    i=[]
    Datos =np.loadtxt('texto.txt', dtype = str, delimiter = ';' and ',')
    necesarios = Datos[1:, [1, 5]]
    for r in necesarios:
        if r[0]=="ALLERGIC REACTION":
            i=r[0]+","+r[1]+"\n"
            outfile.write(i)
    outfile.close()
            
    return 0
t = Allergic()

