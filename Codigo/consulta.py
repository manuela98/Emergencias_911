#--------------------------------------------------------------------
#			Extraccion de datos
#--------------------------------------------------------------------

import numpy as np
import os

try:
	B=np.loadtxt('tzr.csv', dtype = str, delimiter = ';' and ',')

except:
 	os.system('./mv.sh')



print B[0,0]
