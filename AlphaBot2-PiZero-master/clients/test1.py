from line_tracker import line_tracker
from motor import motor
from time import sleep

address = "192.168.0.10"
Threshold=400
mot = motor(address)
lt = line_tracker(address)
lt.start()


while True:
    try:
        if type(lt.data)==int:
            sleep(1)
            continue
        if lt.data[0]>0 and lt.data[1]>0:
            print(lt.data[0])
    except KeyboardInterrupt:
        
        break
        
lt.stop()
mot.stop()