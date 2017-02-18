#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# Name:       eyetracker.py
# Purpose:    Communication with SMI RED 500 device
# Author: Rafael Grigoryan, kriattiffer at gmail.com
# Date: December 20, 2016
# ----------------------------------------------------------------------------

from iViewXAPI import  *  #iViewX library
from ctypes import *
import time, sys
from pylsl import StreamInlet, resolve_stream



def create_stream(stream_name_markers = 'CycleStart', recursion_meter = 0, max_recursion_depth = 3):
        ''' Opens LSL stream for markers, If error, tries to reconnect several times'''
        if recursion_meter == 0:
            recursion_meter +=1
        elif 0<recursion_meter <max_recursion_depth:
            print 'Trying to reconnect for the %i time \n' % (recursion_meter+1)
            recursion_meter +=1
        else:
            print ("Error: Eyetracker cannot conect to markers stream\n")
            return None
            
        print ("Eyetracker connecting to markers stream...")
        # inlet for markers
        if stream_name_markers in [stream.name() for stream in resolve_stream()]:
            sterams_markers = resolve_stream('name', stream_name_markers)
            inlet_markers = StreamInlet(sterams_markers[0])   
            try:
                inlet_markers
                print '...done \n'
            except NameError:
                print ("Error: Eyetracker cannot conect to markers stream\n")
                return None
        else:
            print 'Error: markers stream is not available\n'
            return create_stream(stream_name_markers,recursion_meter)
        return inlet_markers


class Eyetracker():
    """ Class for interaction with iViewXAPI and experiment in present.py """
    
    def __init__(self, debug = False, number_of_points = 9, screen = 0, 
                 hostip='192.168.0.2', serverip='192.168.0.3'):
#        self.namespace = namespace
        self.number_of_points = number_of_points
        self.screen = screen
#        self.im  = create_stream()
        self.host_ip = hostip
        self.server_ip = serverip
#        if not self.im:
#            if debug != True:
#                self.exit_()

    def  calibrate(self):
        '''configure and start calibration'''

        numberofPoints = self.number_of_points # can be 2, 5 and 9
        displayDevice = self.screen # 0 - primary, 1- secondary (?)
        pointBrightness = 250
        backgroundBrightnress = 50
        targetFile = b""
        calibrationSpeed = 0 # slow
        autoAccept  = 1 # 0 = auto, 1 = semi-auto, 2 = auto 
        targetShape = 1 # 0 = image, 1 = circle1, 2 = circle2, 3 = cross
        targetSize = 20
        WTF = 1 #do not touch -- preset?

        calibrationData = CCalibration(numberofPoints, WTF, displayDevice, 
                                        calibrationSpeed, autoAccept, pointBrightness,
                                        backgroundBrightnress, targetShape, targetSize, targetFile)

        self.res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
        print "iV_SetupCalibration " + str(self.res)
        self.res = iViewXAPI.iV_Calibrate()
        print   "iV_Calibrate " + str(self.res)

    
    def validate(self):
        ''' Present 4 points to validate last calibration.
            Results are displayed in iViewX'''
        self.res = iViewXAPI.iV_Validate()
        print "iV_Validate " + str(self.res)
        self.res = iViewXAPI.iV_ShowAccuracyMonitor()
        # self.res = iViewXAPI.iV_ShowEyeImageMonitor()
        # raw_input('press any key to continue')

    def connect_to_iView(self):
        ''' Connect to iViewX using predeficed host and server IPs'''
        self.res = iViewXAPI.iV_Connect(c_char_p(self.host_ip), c_int(4444), 
                                        c_char_p(self.server_ip), c_int(5555))
        print "iV_sysinfo " + str(self.res)

    def send_marker_to_iViewX(self, marker):
        ''' Sends marker to the eyetracker. Marker becomes iViewX event. '''
        res = iViewXAPI.iV_SendImageMessage(marker)
        # if str(self.res) !='1':
            # print "iV_SendImageMessage " + str(self.res)
    
#    def experiment_loop(self):
#        self.res = iViewXAPI.iV_StartRecording ()
        # print "iV_record " + str(self.res)
        # if not self.im:
        #     print 'LSL socket is Nonetype, exiting'
        #     self.exit_()
        # print 'server running...'
        # while 1:
        #     marker, timestamp_mark = self.im.pull_sample()
        #     IDF_marker =  str([marker, timestamp_mark])
        #     self.send_marker_to_iViewX(IDF_marker)
        #     if marker == [999]:
        #         self.exit_()

    def main(self):
        self.connect_to_iView()
        self.calibrate()
        self.validate()
        self.namespace.EYETRACK_CALIB_SUCCESS = True
        self.experiment_loop()


    def start_recording(self):
        self.res=iViewXAPI.iV_StartRecording ()


    def stop_recording(self):
        self.res=iViewXAPI.iV_StopRecording()


    def disconnect(self):
        self.res=iViewXAPI.iV_Disconnect()

    def exit_(self):
        ''' Close all streams, save data and exit.'''
        #self.im.close_stream()
        time.sleep(1)
        self.res = iViewXAPI.iV_StopRecording()

        user = '1'
        filename = r'C:\Users\iView X\Documents\SMI_BCI_Experiments/' + user + str(time.time())
        self.res = iViewXAPI.iV_SaveData(filename, 'description', user, 1) # filename, description, user, owerwrite
        if self.res == 1:
            print 'Eyatracking data saved fo %s.idf' % filename
        else:
            print "iV_SaveData " + str(self.res)
        self.res = iViewXAPI.iV_Disconnect()
        
        sys.exit()


    def define_aoi(self, name, value, x1, x2, y1, y2):
        '''Configure an AOI rectangle'''
        
        aoigroup='Group1' # name of AOI group
        aoiname=str(name) # AOI name
        enabled=1 # 1 - trigger functionality enabled, 0 - disabled
        eye='r' # 'r' - right eye, 'l' - left eye
        fixhit=1 # 1 - fixation as hit trigger, 0 - raw data as trigger
        message='AOI hit' # message to sent to idf data stream
        outputvalue=int(value) # TTL output value
        aoi=CAOIRectangleStruct(x1,x2,y1,y2) #position of AOI
        
        aoi_struct=CAOIStruct(aoigroup, aoiname, enabled, eye, fixhit, message, outputvalue, aoi)
        self.res=iViewXAPI.iV_DefineAOI(byref(aoi_struct))
        print "AOI defined " + str(self.res)


    def define_aoi_port(self, port):
        '''Difine a port for sending TTL triggers'''
        self.res=iViewXAPI.iV_DefineAOIPort(c_int(port)) #4444 or 5555?


    def release_aoi_port(self):
        '''Release a port'''
        self.res=iVeiwXAPI.iV_ReleaseAOIPort()


    def enable_aoi(self, name):
        '''Enable AOI'''
        self.res=iViewXAPI.iV_EnableAOI(c_char_p(name))
        print 'AOI enabled'+ str(self.res)


    def get_aoi_otput(self, value):
        '''???'''
        self.res=iViewXAPI.iV_GetAOIOutputValue(value)
        return self.res


    def get_sample(self):
        '''Updates "sampleData" structure with current eye tracking data'''
        self.res=iViewXAPI.iV_GetSample(byref(sampleData))
        print 'Sample data updated'+ str(self.res)
        return self.res


    def get_event(self):
        '''Updates "eventData" structure with current event data'''
        self.res=iViewXAPI.iV_GetEvent(byref(eventData))
        print 'Event data updated'+ str(self.res)
        return self.res



if __name__ == '__main__':
            
    RED = Eyetracker(namespace = type('test', (object,), {})(), debug = True)
    RED.main()

