#This function will send the feeder block back to it's home position

import sys
import Slush
import time
from Slush import *
from Slush.Boards import *
from Slush.Board import *
from Slush.Base import *
from Slush.Motor import *
from Slush.Temprature import *
from Slush.ExpansionModules import *
  
print('please work')
sys.stdout.flush()

board = Slush.sBoard()
lat_motor = Slush.Motor(0)
lat_motor.run(0,500)
time.sleep(2)
lat_motor.run(1,500)
time.sleep(2)
lat_motor.run(1,0)

