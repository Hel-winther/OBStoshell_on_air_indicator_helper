#!/usr/bin/python
import obspython as obs
import os
import time

#script properties
prefix = ""
start_set = ""
reset_set = ""
ex_start = ""
ex_reset = ""

def script_description():
    a = "Read the instructions on github before using any commands in this script!\n"
    b = "Prefix refers to the path to the program that you want to use as controller, for example OpenRGB. \n"
    c = "Rec and Reset refers to the respective profiles you created within OpenRGB, in these fields write '--profile Rec' or the respective names of the profiles you created.\n"
    description = a + b + c 
    return description 
    
def script_properties():
    props = obs.obs_properties_create()
    
    obs.obs_properties_add_text(props, "Prefix", "Prefix", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "Rec", "Rec", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "Reset", "Reset", obs.OBS_TEXT_DEFAULT)
    
    return props



def script_update(settings):
    global prefix
    global start_set
    global reset_set
    global ex_start
    global ex_reset

    prefix = obs.obs_data_get_string(settings, "Prefix")
    start_set = obs.obs_data_get_string(settings, "Rec")
    reset_set = obs.obs_data_get_string(settings, "Reset")
    ex_start = prefix + " " + start_set
    ex_reset = prefix + " " + reset_set

def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "Prefix", "")
    obs.obs_data_set_default_string(settings, "Rec", "")
    obs.obs_data_set_default_string(settings, "Reset", "")


def script_load(settings):  
    obs.obs_frontend_add_event_callback(on_event)

def on_event(event): #start stop event handlers

    if event == obs.OBS_FRONTEND_EVENT_RECORDING_STARTED:
        os.system(ex_start)
        time.sleep(5)


    elif event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        os.system(ex_reset)
        time.sleep(5)

    elif event == obs.OBS_FRONTEND_EVENT_STREAMING_STARTED:
        os.system(ex_start)
        time.sleep(5)


    elif event == obs.OBS_FRONTEND_EVENT_STREAMING_STOPPED:
        os.system(ex_reset)
        time.sleep(5)

