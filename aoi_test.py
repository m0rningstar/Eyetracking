# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 16:05:46 2017

@author: m0rningstar
"""
DISPSIZE= (1680,1050) #(1920,1080)
RECPOS=(0,0)
RECSIZE=(200,200)
APOS=(DISPSIZE[0]/2-RECSIZE[0]/2,DISPSIZE[0]/2+RECSIZE[0]/2,
        DISPSIZE[1]/2-RECSIZE[1]/2,DISPSIZE[1]/2+RECSIZE[1]/2) #area coordinates

from winsound import Beep
from eyetracker import Eyetracker
from psychopy.visual import Window, Rect
from psychopy.event import Mouse
from ctypes import *
from iViewXAPI import *


def trigger_signal():
    Beep(750,800) #frequency, HZ, duration, ms
    print 'SIGNAL WAS TRIGGERED'


disp=Window(size=DISPSIZE, units='pix', color=(-1,-1,-1), fullscr=True, screen = 0)
mouse=Mouse()
stim=Rect(disp, pos=RECPOS, width=RECSIZE[0], height=RECSIZE[1], 
          lineColor=(0,0,0), fillColor=(0,0,0), lineWidth=3)

def main():

    tracker=Eyetracker(debug = True)
    tracker.connect_to_iView()
    tracker.calibrate()
    tracker.validate()

    stim.draw()
    disp.flip()
    print 'Stim appeared'
    print 'Border coordinates: ', APOS

    tracker.set_online_detection(10,5) #10 ms, 5 deg dispersion
    #tracker.start_recording()

    while True: #loop monitorin for events outside defined area
        button=mouse.getPressed()
        if button[2]:
            break
        event=tracker.get_event()
        if event == 1:
            print 'FIXATION DETECTED'
            x=eventData.positionX
            y=eventData.positionY
            print x, y
            if x<APOS[0] or x>APOS[1] or y<APOS[2] or y>APOS[3]:
                trigger_signal()
                #tracker.send_marker_to_iViewX('Signal triggered')
        else:
            #print 'Event data was not retrived'
            #tracker.is_connected()
            pass

    #tracker.stop_recording()
    tracker.disconnect()
    disp.close()


main()
