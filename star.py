# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:16:10 2017

@author: apron
"""

from psychopy.monitors import Monitor
from psychopy.visual import Window, Circle, ImageStim
from psychopy.event import Mouse
import os

DIR = os.getcwd()

SIZE=(1920,1080) # (1680,1050)
CENTER=(0,0)
DISTANCE=60
WIDTH=31 # 47.4
STIMSIZE= [0.4, 1.0, 2.0]
LETTERSIZE= [0.9, 1.8, 2.6] # SIZE ADJASTMENT NEEDED!

CIRCLE1={'Q':[(0, 1.5), (DIR+r'\Stimuli\17-0.png')], 
              'K':[(1.06, 1.06), (DIR+r'\Stimuli\11-0.png')], 
              'J':[(1.5, 0), (DIR+r'\Stimuli\10-0.png')], 
              'V':[(1.06, -1.06), (DIR+r'\Stimuli\22-0.png')], 
              'P':[(0, -1.5), (DIR+r'\Stimuli\16-0.png')], 
              'U':[(-1.06, -1.06), (DIR+r'\Stimuli\21-0.png')], 
              'G':[(-1.5, 0), (DIR+r'\Stimuli\7-0.png')], 
              'Y':[(-1.06, 1.06), (DIR+r'\Stimuli\25-0.png')]}

CIRCLE2={'L':[(0, 3), (DIR+r'\Stimuli\12-0.png')], 
              'F':[(2.12, 2.12), (DIR+r'\Stimuli\6-0.png')], 
              'B':[(3, 0), (DIR+r'\Stimuli\2-0.png')], 
              'N':[(2.12, -2.12), (DIR+r'\Stimuli\14-0.png')], 
              'M':[(0, -3), (DIR+r'\Stimuli\13-0.png')], 
              'R':[(-2.12, -2.12), (DIR+r'\Stimuli\18-0.png')], 
              'H':[(-3, 0), (DIR+r'\Stimuli\8-0.png')], 
              'W':[(-2.12, 2.12), (DIR+r'\Stimuli\23-0.png')]}

CIRCLE3={'I':[(0, 5), (DIR+r'\Stimuli\9-0.png')], 
              'C':[(3.54, 3.54), (DIR+r'\Stimuli\3-0.png')], 
              'D':[(5, 0), (DIR+r'\Stimuli\4-0.png')], 
              'E':[(3.54, -3.54), (DIR+r'\Stimuli\5-0.png')], 
              'S':[(0, -5), (DIR+r'\Stimuli\19-0.png')], 
              'O':[(-3.54, -3.54), (DIR+r'\Stimuli\15-0.png')], 
              'A':[(-5, 0), (DIR+r'\Stimuli\1-0.png')], 
              'T':[(-3.54, 3.54), (DIR+r'\Stimuli\20-0.png')]}

mon = Monitor('ProBook') #('BlOne')
mon.setWidth(WIDTH) 
mon.setDistance(DISTANCE)
mon.setSizePix(SIZE)

disp=Window(size=SIZE, monitor=mon, units='deg', color=(-1,-1,-1), fullscr=True)

mouse=Mouse()

fixmark=Circle(disp, radius=0.05 ,edges=32, pos=CENTER, lineColor=(0,0,0))

images = []

for item in CIRCLE1.keys():
    image=ImageStim(disp, image=CIRCLE1[item][1], pos=CIRCLE1[item][0], size=LETTERSIZE[0])
    images.append(image)

for item in CIRCLE2.keys():
    image=ImageStim(disp, image=CIRCLE2[item][1], pos=CIRCLE2[item][0], size=LETTERSIZE[1])
    images.append(image)

for item in CIRCLE3.keys():
    image=ImageStim(disp, image=CIRCLE3[item][1], pos=CIRCLE3[item][0], size=LETTERSIZE[2])
    images.append(image)

fixmark.draw()
for image in images:
    image.draw()

disp.flip()

while True:
    button=mouse.getPressed()
    if button[0]:
        break

disp.close()