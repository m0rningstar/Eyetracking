# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 19:13:18 2017

@author: m0rningstar
"""


import os
import datetime
import pandas as pd


def process_events(filename, debug=False):
    '''Returns a dictionary contains pandas dataframes for each specific type 
    of event. Dictionary keys are:
    User Event
    Saccade L
    Saccade R
    Fixation L
    Fixation R
    Blink L
    Blink R
    
    arguments
    
    filename  -  name of the file (produced by IDF Event Detector) to be read
    
    keyword arguments
    
    debug  -  Boolean indicating if DEBUG mode is on (default = False)
    
    returns
    
    data_dict  -  a dict with dataframe for each type of event
    '''
    
    ###########################################################################
    #debug mode
    if debug:
        def message(msg):
            print msg
    else:
        def message(msg):
            pass
    
    ###########################################################################
    #read the file to dataframe
    start_time = datetime.datetime.now()
    try:
        raw = pd.read_csv(os.path.abspath(filename), sep='\t', 
                    names=[str(i) for i in range(17)], squeeze=True) # weird 'names' argument is required because of variable column number
    except IOError:
        print "ERROR: file '%s' does not exist" % filename
    message('file "%s" was read to dataframe ' % filename)
    message('time elapsed: ' + str(datetime.datetime.now()- start_time))
    
    #headers for events dataframes
    s_names = {'1':'Trial', '2':'Number', '3':'Start', '4':'End', '5':'Duration',
             '6':'Start Loc.X', '7':'Start Loc.Y', '8':'End Loc.X', '9':'End Loc.Y',
             '10':'Amplitude', '11':'Peak Speed', '12':'Peak Speed At', 
             '13':'Average Speed', '14':'Peak Accel.', '15':'Peak Decel.', 
             '16':'Average Accel.'}
    f_names = {'1':'Trial', '2':'Number', '3':'Start', '4':'End', '5':'Duration',
             '6':'Location X', '7':'Location Y', '8':'Dispersion X', '9':'Dispersion Y',
             '10':'Plane', '11':'Avg. Pupil Size X', '12':'Avg Pupil Size Y'}
    b_names = {'1':'Trial', '2':'Number', '3':'Start', '4':'End', '5':'Duration'}
    ue_names = {'1':'Trial','2':'Number', '3':'Start', '4':'Description'}
    #dictionary of event types
    types_dict={'User Event':['UserEvent', ue_names], 'Saccade L':['Saccade L', s_names],
                 'Saccade R':['Saccade R', s_names], 'Fixation L':['Fixation L', f_names],
                 'Fixation R':['Fixation R', f_names], 'Blink L':['Blink L', b_names],
                 'Blink R':['Blink R', b_names]} #TODO: redo this whole part in a more decent way

    ###########################################################################
    #loop through event types dictionary
    data_dict={}
    start_time = datetime.datetime.now()
    for key in types_dict:
        event=raw[(raw['0']==types_dict[key][0])]
        event=event.ix[:,1:(len(types_dict[key][1])+1)]
        event.rename(columns=types_dict[key][1], inplace=True)
        event.index = range(len(event))
        data_dict[key]=event
    message('data processing complete')
    message('time elapsed: ' + str(datetime.datetime.now()- start_time))
    
    message('\ndata dictionary keys are: ')
    map(message, data_dict.keys())
    
    return data_dict


def main():
    filename=str(raw_input("Enter filename: ")+".txt")
    df=process_events(filename, debug=True)
    
if __name__ == '__main__':
    main()