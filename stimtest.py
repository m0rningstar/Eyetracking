# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:33:40 2017

@author: apron
"""
from psychopy.monitors import Monitor
from psychopy.visual import Window, Circle
from psychopy.event import Mouse

SIZE=(1920,1080) # (1680,1050)
CENTER=(0,0)
POS={1:(1.5,0), 2:(3,0), 3:(5,0), 4:(1.06,1.06), 5:(2.12,2.12), 6:(3.54,3.54),
     7:(0,1.5), 8:(0,3), 9:(0,5), 10:(-1.06,1.06), 11:(-2.12,2.12),12:(-3.54,3.54), 
     13:(-1.5,0),14:(-3,0),15:(-5,0), 16:(-1.06,-1.06), 17:(-2.12,-2.12), 18:(-3.54,-3.54), 
     19:(0,-1.5), 20:(0,-3), 21:(0,-5), 22:(1.06,-1.06), 23:(2.12,-2.12), 24:(3.54, -3.54)}
DISTANCE=60
WIDTH=31 #
STIMSIZE= [0.4, 1.0, 2.0]

mon = Monitor('ProBook') #('BlOne')
mon.setWidth(WIDTH) 
mon.setDistance(60)
mon.setSizePix(SIZE)

disp=Window(size=SIZE, monitor=mon, units='deg', color=(-1,-1,-1), fullscr=True)

mouse=Mouse()

fixmark=Circle(disp, radius=0.01,edges=32, pos=CENTER, lineColor=(0,0,0))

stim1=Circle(disp, radius=0.3, edges=32, pos=POS[1], lineColor=(0,0,0), lineWidth=3)
stim2=Circle(disp, radius=0.6, edges=32, pos=POS[2], lineColor=(0,0,0), lineWidth=3)
stim3=Circle(disp, radius=1.0, edges=32, pos=POS[3], lineColor=(0,0,0), lineWidth=3)

stim4=Circle(disp, radius=0.3, edges=32, pos=POS[4], lineColor=(0,0,0), lineWidth=3)
stim5=Circle(disp, radius=0.6, edges=32, pos=POS[5], lineColor=(0,0,0), lineWidth=3)
stim6=Circle(disp, radius=1.0, edges=32, pos=POS[6], lineColor=(0,0,0), lineWidth=3)


stim7=Circle(disp, radius=0.3, edges=32, pos=POS[7], lineColor=(0,0,0), lineWidth=3)
stim8=Circle(disp, radius=0.6, edges=32, pos=POS[8], lineColor=(0,0,0), lineWidth=3)
stim9=Circle(disp, radius=1.0, edges=32, pos=POS[9], lineColor=(0,0,0), lineWidth=3)

stim10=Circle(disp, radius=0.3, edges=32, pos=POS[10], lineColor=(0,0,0), lineWidth=3)
stim11=Circle(disp, radius=0.6, edges=32, pos=POS[11], lineColor=(0,0,0), lineWidth=3)
stim12=Circle(disp, radius=1.0, edges=32, pos=POS[12], lineColor=(0,0,0), lineWidth=3)

stim13=Circle(disp, radius=0.3, edges=32, pos=POS[13], lineColor=(0,0,0), lineWidth=3)
stim14=Circle(disp, radius=0.6, edges=32, pos=POS[14], lineColor=(0,0,0), lineWidth=3)
stim15=Circle(disp, radius=1.0, edges=32, pos=POS[15], lineColor=(0,0,0), lineWidth=3)

stim16=Circle(disp, radius=0.3, edges=32, pos=POS[16], lineColor=(0,0,0), lineWidth=3)
stim17=Circle(disp, radius=0.6, edges=32, pos=POS[17], lineColor=(0,0,0), lineWidth=3)
stim18=Circle(disp, radius=1.0, edges=32, pos=POS[18], lineColor=(0,0,0), lineWidth=3)

stim19=Circle(disp, radius=0.3, edges=32, pos=POS[19], lineColor=(0,0,0), lineWidth=3)
stim20=Circle(disp, radius=0.6, edges=32, pos=POS[20], lineColor=(0,0,0), lineWidth=3)
stim21=Circle(disp, radius=1.0, edges=32, pos=POS[21], lineColor=(0,0,0), lineWidth=3)

stim22=Circle(disp, radius=0.3, edges=32, pos=POS[22], lineColor=(0,0,0), lineWidth=3)
stim23=Circle(disp, radius=0.6, edges=32, pos=POS[23], lineColor=(0,0,0), lineWidth=3)
stim24=Circle(disp, radius=1.0, edges=32, pos=POS[24], lineColor=(0,0,0), lineWidth=3)

fixmark.draw()
stim1.draw()
stim2.draw()
stim3.draw()
stim4.draw()
stim5.draw()
stim6.draw()
stim7.draw()
stim8.draw()
stim9.draw()
stim10.draw()
stim11.draw()
stim12.draw()
stim13.draw()
stim14.draw()
stim15.draw()
stim16.draw()
stim17.draw()
stim18.draw()
stim19.draw()
stim20.draw()
stim21.draw()
stim22.draw()
stim23.draw()
stim24.draw()

disp.flip()

while True:
    button=mouse.getPressed()
    if button[0]:
        break

disp.close()