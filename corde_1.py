# -*- coding: utf-8 -*-

import wx
from wxPython.wx import *
import time
from math import cos, sin

TIMER_ID = wxNewId()

class Fenetre(wxPanel) :
	def __init__(self, parent) :
		wxPanel.__init__(self, parent, -1)
		wx.EVT_PAINT(self, self.OnPaint)
		self.t0=time.time()
		wx.EVT_TIMER(self, TIMER_ID, self.OnPaint)

	def OnPaint(self, event=None) :
		dc = wxPaintDC(self)
		dc.Clear()
		dc.SetPen(wx.Pen("BLACK", 4))
		angle=0.2*cos(time.time()-self.t0)
		dc.DrawLine(50, 0, 50+100*sin(angle), 100*cos(angle))

app=wxPySimpleApp()
cadre = wxFrame(None, -1, "Mon cadre !")
fenetre=Fenetre(cadre)
cadre.Show(True)

t = wxTimer(fenetre, TIMER_ID)
t.Start(200)

for i in xrange(10) :
	print i
	time.sleep(1) # Attend 1 seconde
	wxYield()

app.MainLoop() #Pour laisser la main à l'application plutôt qu'à la ligne de commande
