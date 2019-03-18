from line_tracker import line_tracker
from motor import motor
import time

address = "192.168.0.103"
Threshold=400
mot = motor(address)
lt = line_tracker(address)
lt.start()

def leftSensor():
    if (type(lt.data)==int):
        time.sleep(1)
        continue
        
    if (lt.data[0]>Threshold and lt.data[1]>Threshold):
        return True
    elif (lt.data[1]>Threshold):
        return True
    elif (lt.data[0]>Threshold):
        return True
    else:
        return False

def rightSensor():
    if type(lt.data)==int:
        time.sleep(1)
        continue
    if (lt.data[3]>Threshold and lt.data[4]>Threshold):
        return True
    elif (lt.data[3]>Threshold):
        return True
    elif (lt.data[4]>Threshold):
        return True
    else:
        return False
    
    
    
    
    
    
if leftSensor()==True and rightSensor()==True:#Move Forward
    mot.command("forward",1,5)
elif leftSensor()==True and rightSensor()==False:#Turn Right
    mot.command("set_left_speed",1,0.5)
elif leftSensor()==False and rightSensor()==True:#Turn left
    mot.command("set_right_speed",1,0.5)
else:
    lt.stop()
    mot.stop()
