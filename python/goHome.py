#This function will send the feeder block back to it's home position

import sys
import Slush
import time

print('please work')
sys.stdout.flush()

board = Slush.sBoard()
lat_motor = Slush.Motor(0)
lat_motor.run(0,500)
time.sleep(2)
lat_motor.run(1,500)
time.sleep(2)
lat_motor.run(1,0)
