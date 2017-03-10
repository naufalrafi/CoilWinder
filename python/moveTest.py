import sys
import Slush
import time

board = Slush.sBoard()
lateral_motor = Slush.Motor(0);

lateral_motor.run(0,1000)
time.sleep(4)
lateral_motor.run(1,1000)
time.sleep(4)
lateral_motor.run(0,0)

