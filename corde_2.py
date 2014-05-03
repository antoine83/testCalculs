# -*- coding: utf-8 -*-

import wx
from wxPython.wx import *
import time
from math import cos,sin

class Fenetre(wxPanel) :
	def __init__(self, parent) :
		wxPanel.__init__(self, parent, -1)
		wx.EVT_PAINT(self, self.OnPaint)
		self.t0=time.time()

	def OnPaint(self, event=None) :
		dc = wxPaintDC(self)
		dc.Clear()
		dc.SetPen(wx.Pen("BLACK", 4))
		angle=0.2*cos(time.time()-self.t0)
		x,y=50+100*sin(angle),100*cos(angle)
		dc.DrawLine(50, 0, x, y)
		dc.DrawCircle(x, y,20)

app=wxPySimpleApp()
cadre = wxFrame(None, -1, "Mon cadre !")
fenetre=Fenetre(cadre)
cadre.Show(True)

#Boucle de "calcul"
for i in xrange(100) :
	print i
	time.sleep(0.05) #Mettre ici le calcul
	wxPostEvent(fenetre,wxPaintEvent()) # Demande un nouvel affichage
	wxYield() # Laisse du temps à l'affichag
