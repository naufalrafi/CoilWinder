# Function to initialize board, motors, and variables for the winder

import Slush

def init_winder():
	# Slush Engine init variables
	global slush_board
	global lateral_motor
	global drive_motor
	slush_board = Slush.sBoard()
	lateral_motor = Slush.Motor(0)
	drive_motor = Slush.Motor(1)
	# Magnetorqer specific winding variables in mm (can be customized later)
	global wire_gauge
	global rod_diameter
	wire_gauge = 0.02
	rod_diameter = 5

