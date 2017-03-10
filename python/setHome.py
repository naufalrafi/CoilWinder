import Slush
import sys

board = Slush.sBoard()
lateral_motor = Slush.Motor(0)

lateral_motor.goUntilPress(1,0,1000)
lateral_motor.setAsHome()
lateral_motor.goUntilPress(1,1,1000)
end = lateral_motor.getPosition()
lateral_motor.goTo(0)

