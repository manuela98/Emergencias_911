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

def plot():
    outfile=open("EMS.txt","w")

    outfile.write("Day Frecuency\n")
    i=[]
    Lunes = 0
    Martes = 0
    Miercoles = 0
    Jueves = 0
    Viernes = 0
    Sabado = 0
    Domingo = 0
    LunesT = 0
    MartesT = 0
    MiercolesT = 0
    JuevesT = 0
    ViernesT = 0
    SabadoT = 0
    DomingoT= 0
    LunesF = 0
    MartesF = 0
    MiercolesF = 0
    JuevesF = 0
    ViernesF = 0
    SabadoF = 0
    DomingoF = 0
    Datos =np.loadtxt('texto.txt', dtype = str, delimiter = ';' and ',')
    necesarios = Datos[1:, [0, 4]]
    i = 0
    count2 = [0,]
    for r in necesarios:
        if r[0]=="EMS":
            if r[1] == "Monday":
                count2 += [1]
                Lunes += 1
                i += 1
            if r[1] == "Tuesday":
                count2 += [2]
                Martes += 1
                i += 1
            if r[1] == "Wednesday":
                count2 += [3]
                Miercoles += 1
                i += 1
            if r[1] == "Thursday":
                Jueves += 1
                count2 += [4]
                i += 1
            if r[1] == "Friday":
                Viernes += 1
                count2 += [5]
                i += 1
            if r[1] == "Saturday":
                Sabado += 1
                count2 += [6]
                i += 1
            if r[1] == "Sunday":
                Domingo += 1
                count2 += [7]
                i += 1
            if count2[i] == 1 and count2[i-1]==7:
                outfile.write('1 '+str(Lunes)+'\n')
                outfile.write('2 '+str(Martes)+'\n')
                outfile.write('3 '+str(Miercoles)+'\n')
                outfile.write('4 '+str(Jueves)+'\n')
                outfile.write('5 '+str(Viernes)+'\n')
                outfile.write('6 '+str(Sabado)+'\n')
                outfile.write('7 '+str(Domingo)+'\n')
                Lunes = 0
                Martes = 0
                Miercoles = 0
                Jueves = 0
                Viernes = 0
                Sabado = 0
                Domingo= 0
          



    outfile=open("Traffic.txt","w")
    outfile.write("Day Frecuency\n")
    j = 0
    count1 = [0,]
    for r in necesarios:
        if r[0]=="Traffic":
            if r[1] == "Monday":
                count1 += [1]
                LunesT += 1
                j += 1
            if r[1] == "Tuesday":
                count1 += [2]
                MartesT += 1
                j += 1
            if r[1] == "Wednesday":
                count1 += [3]
                MiercolesT += 1
                j += 1
            if r[1] == "Thursday":
                JuevesT += 1
                count1 += [4]
                j += 1
            if r[1] == "Friday":
                ViernesT += 1
                count1 += [5]
                j += 1
            if r[1] == "Saturday":
                SabadoT += 1
                count1 += [6]
                j += 1
            if r[1] == "Sunday":
                DomingoT += 1
                count1 += [7]
                j += 1
            if count1[j] == 1 and count1[j-1]==7:
                outfile.write('1 '+str(LunesT)+'\n')
                outfile.write('2 '+str(MartesT)+'\n')
                outfile.write('3 '+str(MiercolesT)+'\n')
                outfile.write('4 '+str(JuevesT)+'\n')
                outfile.write('5 '+str(ViernesT)+'\n')
                outfile.write('6 '+str(SabadoT)+'\n')
                outfile.write('7 '+str(DomingoT)+'\n')
                LunesT = 0
                MartesT = 0
                MiercolesT = 0
                JuevesT = 0
                ViernesT = 0
                SabadoT = 0
                DomingoT= 0
          
    
    
    

    outfile=open("Fire.txt","w")
    outfile.write("Day Frecuency\n")
    i = 0
    count = [0,]
    for r in necesarios:
        if r[0]=="Fire":
            if r[1] == "Monday":
                count += [1]
                LunesF += 1
                i += 1
            if r[1] == "Tuesday":
                count += [2]
                MartesF += 1
                i += 1
            if r[1] == "Wednesday":
                count += [3]
                MiercolesF += 1
                i += 1
            if r[1] == "Thursday":
                JuevesF += 1
                count += [4]
                i += 1
            if r[1] == "Friday":
                ViernesF += 1
                count += [5]
                i += 1
            if r[1] == "Saturday":
                SabadoF += 1
                count += [6]
                i += 1
            if r[1] == "Sunday":
                DomingoF += 1
                count += [7]
                i += 1
            if count[i] == 1 and count[i-1]==7:
                outfile.write('1 '+str(LunesF)+'\n')
                outfile.write('2 '+str(MartesF)+'\n')
                outfile.write('3 '+str(MiercolesF)+'\n')
                outfile.write('4 '+str(JuevesF)+'\n')
                outfile.write('5 '+str(ViernesF)+'\n')
                outfile.write('6 '+str(SabadoF)+'\n')
                outfile.write('7 '+str(DomingoF)+'\n')
                LunesF = 0
                MartesF = 0
                MiercolesF = 0
                JuevesF = 0
                ViernesF = 0
                SabadoF = 0
                DomingoF= 0
          
plot()

