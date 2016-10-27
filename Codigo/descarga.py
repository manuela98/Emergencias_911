
#--------------------------------------------------------------------
#			Descarga de datos
#--------------------------------------------------------------------


import requests
import bs4
import webbrowser
import os
import time
import urllib



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
		urllib.urlretrieve (lineas_a[1].string, "tzr.csv")
 









