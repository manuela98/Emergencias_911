#--------------------------------------------------------------------
#			Extraccion de datos
#--------------------------------------------------------------------

import requests
import bs4
import webbrowser

res = requests.get('http://montcoalert.org/gettingdata/')
gh = bs4.BeautifulSoup(res.text, "lxml") # tambien es posible desde un archivo abierto
type(gh)
tabla_archivos = gh.find_all('div',{'class':'blog-entry-body'})
type(tabla_archivos)
len(tabla_archivos)
for content in tabla_archivos:
    lineas_a = content('a')
    if lineas_a:
        webbrowser.open(lineas_a[1].string)
