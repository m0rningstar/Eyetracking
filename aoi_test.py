# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 16:05:46 2017

@author: apron
"""
DISPSIZE=(1920,1080) # (1680,1050)
RECPOS=(0,0)
RECSIZE=(100,100)
AOIPOS=(DISPSIZE[0]/2-RECSIZE[0]/2,DISPSIZE[0]/2+RECSIZE[0]/2,
        DISPSIZE[1]/2-RECSIZE[1]/2,DISPSIZE[1]/2+RECSIZE[1]/2) #needs revising?

from winsound import Beep
from eyetracker import Eyetracker
from psychopy.visual import Window, Rect
from psychopy.core import wait

def trigger_signal():
    Beep(750,800) #frequency, HZ, duration, ms


disp=Window(size=DISPSIZE, units='pix', color=(0,0,0), fullscr=True)
stim=Rect(disp, pos=RECPOS, width=RECSIZE[0], height=RECSIZE[1], 
          lineColor=(-1,-1,-1), fillColor=(-1,-1,-1), lineWidth=3)

def main():
    #tracker=Eyetracker(debug = True)
    #tracker.connect_to_iView()
    #tracker.calibrate()
    #tracker.validate()
    
    stim.draw()
    disp.flip()
    
    print 'Stim appeared'
    
    tracker.start_recording()
    
    tracker.define_aoi('block',AOIPOS[0],AOIPOS[1],AOIPOS[2],AOIPOS[3])
    tracker.enable_aoi('block')
    
    try:
        while True:
            tracker.aoi_callback(trigger_signal())
    except KeyboardInterrupt:
        pass
    
    tracker.stop_recording()
    tracker.disconnect()
    trigger_signal()
    disp.close()
    
main()
