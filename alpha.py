import sys
import Slush

pi = 3.14159265

#assuming website acquires input of rod diameter(d) wire diameter(w)
#otherwise input manually
d = 
w = 

i = 0
ratio = pi*d/w

b = Slush.sBoard()
motor_coiler = Slush.motor(0)
motor_driver = Slush.Motor(1)

#CALIBRATION
#motor goes towards the starting position until limit switch is pressed
motor_driver.goUntilPress(1,0,10000)
#sets current position as position '0'
motor_driver.setAsHome()

#motor goes towards the stop position until limit switch is pressed
motor_driver.goUntilPress(1,1,10000)
#assign the stop position to the variable 'stop'
stop = motor_driver.getPosition()

#motor goes to starting position, '0', ready to start winding 
motor_driver.goTo(0)


#WINDING
#awaits input, allowing user to attach the wire to the rod before the motors start
While True:
n = raw_input("Press 'y' when ready to start winding : ")
if n.strip() == 'y':
    break

#winds the wire 
for laps in range(7) #14 layers = 7 times back and forth
    for i in xrange(stop)
        motor_driver.goTo(i+1)
        motor_coiler.goTo((i+1)*ratio)

    for i in reversed(xrange(stop))
        motor_driver.goTo(i+1)
        motor_coiler.goTo((i+1)*ratio)


#profit??
