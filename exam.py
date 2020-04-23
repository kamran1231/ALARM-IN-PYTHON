

import time
import winsound
print('Made by Kamran')
def myAlarm():
    try:
        myTime = list(map(int,input('Enter the time in hr and min sec\n').split()))
        if len(myTime)== 3:
            total_seconds = myTime[0]*60*60 + myTime[1]*60+myTime[2]
            time.sleep(total_seconds)
            frequency = 2500  #set frequency to 2500 hertz
            durantion = 1000  #set duration to 1000ms == 1 sec
            winsound.Beep(frequency,durantion)
        else:
            print('please enter time in correct format')
            myAlarm()
    except Exception as e:
        print('this is the exception\n',e,'so')
        myAlarm()
myAlarm()

