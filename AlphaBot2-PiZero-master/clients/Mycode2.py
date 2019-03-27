from line_tracker import line_tracker
from motor import motor
import time

address = "192.168.0.100"
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
            if lt.data[2]<Threshold and lt.data[1]>Threshold:#Detect black line on middle sensor
                mot.command("forward",7,0.5)
                print(lt.data)
                print("forward")
            else:
                if lt.data[0]<300 or lt.data[1]<Threshold:#Detect black line on left sensor
                    mot.command("left",3,0.3)
                    print(lt.data)
                    print("left")
                elif lt.data[3]<Threshold or lt.data[4]<Threshold:#Detect black line on right sesnsor
                    mot.command("right",3,0.3)
                    print(lt.data)
                    print("right")
                elif lt.data[0]<300 and lt.data[1]<Threshold:
                    mot.command("left",25,0.1)
                else:
                    mot.command("right",25,0.1)#U-turn
            inf_t=t
            
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        lt.stop()
        mot.stop()
        break
        
#This code is a modification from test_receiver.py.
        
