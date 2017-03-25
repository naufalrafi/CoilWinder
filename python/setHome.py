import Slush
import sys

board = Slush.sBoard()
lateral_motor = Slush.Motor(0)
#0,0 is towards LLS, 0,1 is towards ULS

lateral_motor.goUntilPress(0,0,1000000)
lateral_motor.setAsHome()
lateral_motor.goUntilPress(0,1,1000000)
end = lateral_motor.getPosition()
lateral_motor.goTo(0)
