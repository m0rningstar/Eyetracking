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
from psychopy.event import Mouse
from ctypes import *

def trigger_signal():
    Beep(750,800) #frequency, HZ, duration, ms


disp=Window(size=DISPSIZE, units='pix', color=(-1,-1,-1), fullscr=True)
mouse=Mouse()
stim=Rect(disp, pos=RECPOS, width=RECSIZE[0], height=RECSIZE[1], 
          lineColor=(0,0,0), fillColor=(0,0,0), lineWidth=3)

p_output_val=pointer(c_int(0))

def main():
    tracker=Eyetracker(debug = True)
    tracker.connect_to_iView()
    tracker.calibrate()
    tracker.validate()
    
    stim.draw()
    disp.flip()
    
    print 'Stim appeared'
    
    tracker.start_recording()
    
    tracker.define_aoi('block', 111, AOIPOS[0],AOIPOS[1],AOIPOS[2],AOIPOS[3])
    tracker.define_aoi_port(4444)

    while True:
        button=mouse.getPressed()
        if button[0]:
            break
        ret_out=tracker.get_aoi_otput(p_output_val)
        if ret_out==1:
            if p_output_val[0] == 111: #or try: if p.output_val.contents == 1:
                #trigger_signal()
                print 'AOI hit'
            else:
                pass
        else:
            print 'AOI output value could not be retrived'

    tracker.release_aoi_port()
    tracker.stop_recording()
    tracker.disconnect()
    disp.close()
    
main()
