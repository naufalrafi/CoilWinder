# This script is the hard coded version of the winding algorithm

import sys
import Slush
import time

board = Slush.sBoard()
lateral_motor = Slush.Motor(0)
drive_motor = Slush.Motor(1)

def requiresTurn(number_of_turns):
    number_of_turns_required = rod_length/gauge
    if(number_of_turns == number_of_turns_required):
        return False
    return True

#Define constant that describes the amount of horizontal movement that the feeder block moves for every full turn of motor.
lateral_constant = 0.01

#Define parameters for wire and rod
gauge = 0.02
rod_diameter = 5
rod_length = 100
one_full_turn = #number of steps needed for the stepper to do one full rotation
#Wind time, assume is starting from 0 position which is the location of the first wind.

#Initialize variables for winding algorithm
number_of_layers = 0
number_of_turns = 1

while(number_of_layers < 14):
    #for one full turn of drive_motor, move the lateral_motor one gauge over
    while(requiresTurn(number_of_turns)):
        drive_motor.goTo(number_of_turns * one_full_turn)
        lateral_motor.goTo(NEEDS TO MOVE 0.02 OVER)
        number_of_turns += 1
    # Should have gone all the way to the end now
    number_of_layers += 1
    number_of_turns = 0
    # Reverse Direction now
    while(requiresTurn(number_of_turns)):
        drive_motor.goTo()
