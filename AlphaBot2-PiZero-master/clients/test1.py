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
            
        print(lt.data)
    except KeyboardInterrupt:
        
        break
        
lt.stop()
mot.stop()