# -*- coding:iso-8859-1 -*-
from scipy import *
import numpy as np
import matplotlib.pyplot as gplt


data=np.loadtxt('tgdata.dat', comments='!')

print (data)
#data=io.array_import.read_array('tgdata.dat')
plotfile='tgdata.png'

gplt.plot(data[:,0],data[:,1])
#gplt.plot(data[:,0],data[:,1],'title "Poids en fonction du temps" with points')
gplt.title("Poids en fonction du temps")
gplt.xlabel('temps (h)')
#xtitle('temps (h)')
gplt.ylabel("Echappement d'hydrogene")
#ytitle("Echappement d'hydrogene")
gplt.grid(b=None)
#grid("off")
gplt.show()
gplt.savefig(plotfile)
#output(plotfile,'png medium transparent picsize 600 400')  
