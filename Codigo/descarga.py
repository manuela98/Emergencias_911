
#--------------------------------------------------------------------
#			Descarga de datos
#--------------------------------------------------------------------


import requests
import bs4
import webbrowser
import os
import time



def mover_datos():
		#Funcion encargada de mover el archivo de texto descargado a la Carpeta actual
		return os.system('./mv.sh')


try:
    archivo = open("tzr.csv", "r") 
    archivo.close()
except:
    res = requests.get('http://montcoalert.org/gettingdata/')
    gh = bs4.BeautifulSoup(res.text, "lxml") 
    link = gh.find_all('div',{'class':'blog-entry-body'})
    for content in link:
        lineas_a = content('a')
        if lineas_a:
            webbrowser.open(lineas_a[1].string)
	    time.sleep(20)
	    mover_datos()
	






