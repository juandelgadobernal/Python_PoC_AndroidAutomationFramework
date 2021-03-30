#!/usr/bin/python

from subprocess import check_call, check_output
import time
import datetime
import argparse
from uiautomator import Device
import pytz

#---------------------------------------------------------

def readserial():

    output = check_output(['adb', 'devices'])

    lines = output.splitlines()
    firstDev = lines[1].split()[0]
    print ("1st Device on List = {}".format(firstDev))

    return firstDev

def startScript():
    print("Script TV---------")
    start_ts = datetime.datetime.now()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print('test start:  %s ' % start_ts_pst)

    return start_ts_pst

def endScript(start_ts_pst):

    stop_ts = datetime.datetime.now()
    stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    print("-------------RESULTS  -------------------------------------------")
    print('test start:  %s' % start_ts_pst)
    print('test end  :  %s' % stop_ts_pst)

    return

def control_down(androidTV, serial):

    # Wakeup
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
    #print("Android TV  - Wakeup".format())
    time.sleep(2)

    #down
    androidTV.press.down()
    print("Android TV Control - Click Down".format())
    time.sleep(2)

def yourApps(androidTV,serial,tv_app):

    """
    Identify an App in the row "Your Apps and channels"
    param str description: type of the element by description to be clicked to identify
    param str selected: name of the element as selected
    returns: True if onb is found
    """
    long_timeout = 3

    objFound = False

    while objFound == False:
        if androidTV(description=tv_app,selected ='true' ).exists:
            print("Android TV - Obj exist {}".format(tv_app))
            androidTV(description=tv_app,selected ='true' ).click()
            print("Android TV Control- Enter {}".format(tv_app))
            objFound = True
        else:
            androidTV.press.right()
            print("Android TV Control- Move to the Right".format())
    return True

def home_androidTV(androidTV,serial):

    long_timeout = 3

    # Wakeup
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
    print("Android TV  - Wakeup".format())
    time.sleep(3)

    # home
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    print("Android TV Control - Click Home".format())

    if androidTV(text='Home').wait.exists(timeout=long_timeout):
        print("Android TV - Verify Home Displayed".format())
        androidTV(text='Home').click()
        print("Android TV - Click Home".format())


def foundApp_androidTV(androidTV,serial,tv_app):
    #Your Apps and channels
    control_down(androidTV,serial)
    control_down(androidTV,serial)

    #click app
    yourApps(androidTV,serial,tv_app)

    return

def appTest_androidTV(androidTV,serial,tv_app):

    print("Android TV - TV App {}".format(tv_app))

    time.sleep(5)
    androidTV.press.down()
    time.sleep(2)
    androidTV.press.back()
    print("Android TV Control - Click Back to Home menu".format())
    time.sleep(5)
    androidTV.press.up()
    print("Android TV Control - Click Up".format())
    time.sleep(5)
    androidTV.press.enter()
    print("Android TV Control - Click Enter to Search icon".format())
    time.sleep(5)

    print("Android TV Control - Set text for search movie".format())
    androidTV(description='f').click()
    androidTV(description='r').click()
    androidTV(description='o').click()
    androidTV(description='z').click()
    androidTV(description='e').click()
    androidTV(description='n').click()
    time.sleep(5)

    if androidTV(resourceId='com.disney.disneyplus:id/poster', description='Frozen: Una aventura congelada').exists :
        print("Android TV - Movie exist frozen".format())
        androidTV.press.down()
        time.sleep(1)
        androidTV.press.down()
        time.sleep(1)
        androidTV.press.down()
        time.sleep(1)
        androidTV.press.down()
        time.sleep(1)
        androidTV.press.enter()
        time.sleep(5)
        #androidTV(resourceId='com.disney.disneyplus:id/poster', description='Frozen: Una aventura congelada').press.enter()

        if androidTV(text='VER AHORA', selected='true').exists or androidTV(text='REANUDAR', selected='true').exists:
            print("Android TV - Ready to Streaming".format())
            androidTV(selected='true').click()
            print("Android TV Control- Enter ".format())
            time.sleep(5)
            print("Android TV Validation - Movie streaming ".format())

        time.sleep(10)
        androidTV.press.back()



    #androidTV(resourceId='com.disney.disneyplus:id/searchEditText', className='android.widget.EditText').set_text("Frozen")
    #time.sleep(3)
    #androidTV.press.enter()

    #go to your apps


    # App click
    #d(className='android.widget.ImageView', resourceId='com.amazon.tv.launcher:id/main_image', packageName='com.amazon.tv.launcher').click()
    #time.sleep(3)
"""
    # Menu_click
    d(text='Movies', className='android.widget.TextView').click()
    time.sleep(3)
    #d.press.back()
    d.press.left()
    time.sleep(1)
    d.press.home()
    time.sleep(1)

    d.press.down
    time.sleep(5)
    d.press.down()
    time.sleep(5)
    d.press.right()
    time.sleep(1)

    d.press.down()
    time.sleep(0)

    d.press.right()
    time.sleep(1)

    d.press.right()
    time.sleep(1)

    d.press.enter()
    time.sleep(1)

    d.press.home()

    #time.sleep(3)


"""

    # Menu_click
    #d(text='Home', className='android.widget.TextView').click()
    # time.sleep(3)

    # Airplane
    #d.pressDPadLeft()
    #time.sleep(3)


    # home
    #check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    #time.sleep(3)


#---------------------------------------------------------------------------

if __name__ == "__main__":

    time.sleep(10)

    firstserial = readserial()
    serial=firstserial #args.serial
    tv_app = "Disney+"
    #YouTube

    start_ts_pst = startScript()

    try:
        androidTV = Device(serial)
        home_androidTV(androidTV,serial)
        foundApp_androidTV(androidTV,serial,tv_app)
        appTest_androidTV(androidTV, serial, tv_app)

    except Exception as ex:
        print(ex)
    finally:
        endScript(start_ts_pst)
