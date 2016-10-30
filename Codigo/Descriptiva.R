datos.csv <- read.csv("texto.txt", header = T)

t="--------------------------------------------------------------------------------------------";t
x="En este archivo se realiza la Estadistica Descriptiva de los diferentes variables y resumenes";x
y="--------------------------------------------------------------------------------------------";y

#head(datos.csv)
#sapply(datos.csv, class)
j="--Resumen de frecuencia de datos--":;j;summary(datos.csv) #Resumen de los datos

table(datos.csv$Day) #Frecuencias de los dias
a<-table(datos.csv$Day) #Variable a con las frecuencias de los días, se usara para calcular la media etc
mean(a) #media de los dias
my_mode<-function(var){ #Esta funcion nos sirve para calcular cual es el valor que mas se repite
frec.var<-table(var) 
valor<-which(frec.var==max(frec.var)) # Elementos con el valor maximo
names(valor)
}
j00="Dia en el que mas se presentan las llamadas";j00;my_mode(datos.csv$Day) #llamamos la funcion y nos dice que dia es donde mas se presentan emergencias
j0="A continuacion se muestran algunos datos estadisticas  de las llamadas por mes";j0
m<-table(datos.csv$Month)
jpeg("promllamadaspormes.jpg")
barplot(m,col=rainbow(12))
my_mode(datos.csv$Month)
#promedio de llamadas por mes
j1="Media de las llamadas por mes ";j1;mean(m)
j2="Maximo ";j2;max(m)
j3="Minimo";j3;min(m)
j4="Desviacion estandar";j4;sd(m)
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
(dec-jan)-dev
dev.off()



Fall_victim <- read.csv("Fall_victim.txt", header = TRUE)
j5="Resumen de llamadas por  victimas(Fall victim)por mes ";j5;summary(Fall_victim)
Vic<-table(Fall_victim$Month)
jpeg("victimasfatalesmes.jpg")
barplot(Vic,col=rainbow(7))
# promedio de victimas fatales al mes
dev.off()
Allergic <- read.csv("Allergic.txt", header = TRUE)
j6="Resumen de llamadas por reacciones alergicas por mes";j6;summary(Allergic)
Al<-table(Allergic$Month)
jpeg("Alergiasmes.jpg")
barplot(Al,col=rainbow(7))
dev.off()

