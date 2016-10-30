#-----------------------------------------------Descriptiva--------------------------------------------------------------------
datos.csv <- read.csv("texto.txt", header = T)
Semana <- read.csv("semanas.txt", header = T)

t="--------------------------------------------------------------------------------------------";t
x="En este archivo se realiza la Estadistica Descriptiva de los diferentes variables y resumenes";x
y="--------------------------------------------------------------------------------------------";y

#head(datos.csv)
#sapply(datos.csv, class)
j="--Resumen de frecuencia de datos--";j;summary(datos.csv) #Resumen de los datos

table(datos.csv$Day) #Frecuencias de los dias
a<-table(datos.csv$Day) #Variable a con las frecuencias de los días, se usara para calcular la media etc
mean(a) #media de los dias
my_mode<-function(var){ #Esta funcion nos sirve para calcular cual es el valor que mas se repite
frec.var<-table(var) 
valor<-which(frec.var==max(frec.var)) # Elementos con el valor maximo
names(valor)
}
#---------------------------------------------------------------------------------------------------------

j00="Dia en el que mas se presentan las llamadas";j00;my_mode(datos.csv$Day) #llamamos la funcion y nos dice que dia es donde mas se presentan emergencias
j0="A continuacion se muestran algunos datos estadisticas  de las llamadas por mes";j0
m<-table(datos.csv$Month)
jpeg("prom_llamadas_por_mes.jpg")
barplot(m,col=rainbow(12))
e00="Mes con mas numero de emergencias registradas";e00;my_mode(datos.csv$Month)
#promedio de llamadas por mes
j1="Media de las llamadas por mes ";j1;mean(m)
j2="Maximo ";j2;max(m)
j3="Minimo";j3;min(m)
j4="Desviacion estandar";j4;sd(m)
dev.off()

#-----------------------------------------------------------------------------------------------------------------------
a<-table(datos.csv$Day)
rst =c(a[1]/Semana[1,1],a[2]/Semana[1,2],a[3]/Semana[1,3],a[4]/Semana[1,4],a[5]/Semana[1,5],a[6]/Semana[1,6],a[7]/Semana[1,7])
wr="Resumen de llamadas por dia";wr;summary(a)
g=a/Semana[1,1]
jpeg("prom_llamadas_por_dia.jpg")
barplot(rst, main="Promedio de llamadas por dia", col=rainbow(7))
dev.off()

w00="Dia en el que mas se presentan las llamadas";w00;my_mode(datos.csv$Day)
w1="Media de las llamadas por dia";w1;mean(g)
w2="Maximo ";w2;max(g)
w3="Minimo";w3;min(g)
w4="Desviacion estandar";w4;sd(g)


#--------------------------------------------------------------------------------------------------------------------------


b<-table(datos.csv$title)
jpeg("prom_llamadas_semanales.jpg")
b1<-b/Semana[1,1]
tr="Resumen de llamadas semanales";tr;summary(b1)
barplot(b1,main="Promedio de llamadas semanales",col=rainbow(3))
dev.off()
t00="Tipo de emergencia donde se presentan mas llamadas semanales";t00;my_mode(datos.csv$title)
t1="Media de las llamadas semanales ";t1;mean(b1)
t2="Maximo ";t2;max(b1)
t3="Minimo";t3;min(b1)
t4="Desviacion estandar";t4;sd(b1)
 
#-----------------------------------------------------------------------------------------------------------------------------
b2 = b/Semana[1,1]*1/7
sr="Resumen de llamadas al dia";sr;summary(b2)
jpeg("prom_llamadas_al_dia.jpg")
barplot(b2,main="Promedio de llamadas al dia",col=rainbow(4))
dev.off()
s00="Tipo de emergencia donde se presentan mas llamadas al dia";s00;my_mode(datos.csv$title)
s1="Media de las llamadas por dia ";s1;mean(b2)
s2="Maximo ";s2;max(b2)
s3="Minimo";s3;min(b2)
s4="Desviacion estandar";s4;sd(b2)


#-----------------------------------------------------------------------------------------------------------------------------

Trafico <- read.csv("Trafico.txt", header = TRUE)

Traf<-table(Trafico$Dia)
Tra=Traf/Semana[1,1]
pr="Resumen de emergencias de trafico por dia";sr;summary(Trafico)
jpeg("prom_trafico_al_dia.jpg")
barplot(Tra,main="Promedio de emergencias de trafico al dia",col=rainbow(7))
dev.off()
p00="Dia en que se presentan mas emergencias de trafico";p00;my_mode(Trafico$Dia)
p1="Media de las llamadas relacionadas al trafico al dia ";p1;mean(Tra)
p2="Maximo ";p2;max(Tra)
p3="Minimo";p3;min(Tra)
p4="Desviacion estandar";p4;sd(Tra)
      
      
      
#-----------------------------------------------------------------------------------------------------------------------------
Fall_victim <- read.csv("Fall_victim.txt", header = TRUE)
j5="Resumen de llamadas por  victimas(Fall victim)por mes ";j5;summary(Fall_victim)
Vic<-table(Fall_victim$Month)
jpeg("victimas_fatales_mes.jpg")
barplot(Vic,main="Promedio de victimas fatales por mes",col=rainbow(12))
dev.off()
x00="Mes en donde se prensentan mas vitimas fatales";x00;my_mode(Fall_victim$Month)
x1="Media de las llamadas relacionadas a victimas fatales ";x1;mean(Vic)
x2="Maximo ";x2;max(Vic)
x3="Minimo";x3;min(Vic)
x4="Desviacion estandar";x4;sd(Vic)



#------------------------------------------------------------------------------------------------------------------------------
Allergic <- read.csv("Allergic.txt", header = TRUE)
j6="Resumen de llamadas por reacciones alergicas por mes";j6;summary(Allergic)
Al<-table(Allergic$Month)
jpeg("Alergias_mes.jpg")
barplot(Al,main="Promedio de alergias mensuales",col=rainbow(12))
dev.off()
y00="Mes en donde se prensentan mas casos de alergias";y00;my_mode(Allergic$Month)
y1="Media de las llamadas relacionadas a casos de alergias ";y1;mean(Al)
y2="Maximo ";y2;max(Al)
y3="Minimo";y3;min(Al)
y4="Desviacion estandar";y4;sd(Al)

#-----------------------------------------------INFERENCIAL--------------------------------------------------------------------


inf="¿Es Cierto que Diciembre es el mes con mayor numero de Emergencias?";inf
m<-table(datos.csv$Month)

dev<-sd(m)
dec<-m[3]
jan<-m[5]
feb<-m[4]
mar<-m[8]
apr<-m[1]
aug<-m[2]
sept<-m[12]
oct<-m[11]
nov<-m[10]
may<-m[9]
jul<-m[6]
jun<-m[7]


res11=(dec-jan)-dev
res1=(dec-feb)-dev
res2=(dec-mar)-dev
res3=(dec-apr)-dev
res4=(dec-aug)-dev
res5=(dec-sept)-dev
res6=(dec-oct)-dev
res7=(dec-nov)-dev
res8=(dec-may)-dev
res9=(dec-jul)-dev
res10=(dec-jun)-dev

if (res1<0 | res2<0 | res3<0 | res4<0 | res5<0 | res6<0 | res7<0 | res8<0 | res9<0 | res10<0 | res11<0) print ('Falso')