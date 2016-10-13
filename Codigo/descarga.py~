#--------------------------------------------------------------------
#			Descarga de datos
#--------------------------------------------------------------------


import requests
import bs4
import webbrowser
import numpy as np
import shutil 

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





#--------------------------------------------------------------------
#			Extraccion de datos
#--------------------------------------------------------------------



B=np.loadtxt('tzr.csv', dtype = str, delimiter = ';' and ',')
print B[0,0]

