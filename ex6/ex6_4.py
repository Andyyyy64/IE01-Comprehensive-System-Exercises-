import webiopi
import os
import datetime


SAVEDIR = '/home/andy/IE01-Comprehensive-System-Exercises/ex6'

@webiopi.macro
def get_time():
#    print(datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S"))
    return datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S")

@webiopi.macro
def camera(no):
    filename = SAVEDIR + '/camera_' + no + '.jpg'
    command = f"fswebcam -r 320x240 -d /dev/video0 '{filename}'"
    os.system(command)
    os.system('sync')
