from line_tracker import line_tracker
from motor import motor
import time

address = "192.168.0.103"
Threshold=400
mot = motor(address)
lt = line_tracker(address)
lt.start()
inf_t = time.time()

while True:
    try:
        t=time.time()
        if type(lt.data)==int: 
            time.sleep(0.5)
            continue
            
        if t-inf_t>1:
            if lt.data[2]<Threshold:#Detect black line on middle sensor
                mot.command("forward",7,0.5)
                print("forward")
            else:
                if lt.data[0]<Threshold or lt.data[1]<Threshold:#Detect black line on left sensor
                    mot.command("left",3,0.2)
                    print("left")
                elif lt.data[3]<Threshold or lt.data[4]<Threshold:#Detect black line on right sesnsor
                    mot.command("right",3,0.2)
                    print("right")
            inf_t=t
            
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        lt.stop()
        mot.stop()
        break
        
#This code is a modification from test_receiver.py.
        
