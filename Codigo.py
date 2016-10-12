#--------------------------------------------------------------------
#			Extraccion de datos
#--------------------------------------------------------------------

import requests
import bs4
import webbrowser

def extraccion():
	res = requests.get('http://montcoalert.org/gettingdata/')
	gh = bs4.BeautifulSoup(res.text, "lxml") # tambien es posible desde un archivo abierto
	link = gh.find_all('div',{'class':'blog-entry-body'})
	for content in link:
    		lineas_a = content('a')
    		if lineas_a:
        		webbrowser.open(lineas_a[1].string)

extraccion()
