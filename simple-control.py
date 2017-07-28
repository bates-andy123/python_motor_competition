import time #libraries
import serial
import datetime
import threading

speed = 120

right_motor = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
#arduino.open()

def motor_set(motor, side, direction, speed):
	string = ""
	if(motor == 1 or motor == "Back"):
		if(side == 'Right'):
			if(direction == "Forward"):
				string = "M1R" + chr(speed) + "\r\n"	
				right_motor.write(string.encode())
			if(direction == "Reverse"):
				string = "M1F" + chr(speed) + "\r\n"	
				right_motor.write(string.encode())
		elif(side == 'Left'):
			if(direction == "Forward"):
				string = "M1F" + chr(speed) + "\r\n"	
				left_motor.write(string.encode())
			if(direction == "Reverse"):
				string = "M1R" + chr(speed) + "\r\n"	
				left_motor.write(string.encode())
	elif(motor == 3 or motor == "Depth"):
		if(side == 'Right'):
			if(direction == "Up"):
				string = "M3R" + chr(speed) + "\r\n"	
				right_motor.write(string.encode())
			if(direction == "Down"):
				string = "M3F" + chr(speed) + "\r\n"	
				right_motor.write(string.encode())
		elif(side == 'Left'):
			if(direction == "Up"):
				string = "M3F" + chr(speed) + "\r\n"	
				left_motor.write(string.encode())
			if(direction == "Down"):
				string = "M3R" + chr(speed) + "\r\n"	
				left_motor.write(string.encode())
	elif(motor == 2 or motor == "Front"):
		if(side == 'Right'):
			if(direction == "Forward"):
				string = "M2F" + chr(speed) + "\r\n"
				right_motor.write(string.encode())
			if(direction == "Reverse"):
				string = "M2R" + chr(speed) + "\r\n"	
				right_motor.write(string.encode())
		elif(side == 'Left'):
			if(direction == "Forward"):
				string = "M2R" + chr(speed) + "\r\n"	
				left_motor.write(string.encode())
			if(direction == "Reverse"):
				string = "M2F" + chr(speed) + "\r\n"	
				left_motor.write(string.encode())
	


left_motor = serial.Serial(
	port='/dev/ttyUSB1',
	baudrate=9600,
	#parity=serial.None,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

while True:
	x = raw_input("Enter Command\r\n")
	string = "STP\r\n"
	left_motor.write(string.encode())
	right_motor.write(string.encode())
	
	if x == "F":
	#	motor_set("Depth", 'Right', 'Down', speed)
		motor_set("Front", 'Left', 'Forward', speed)
	elif x == "R":
		motor_set("Front", "Left", "Reverse", speed)
	elif x == "UP":
		motor_set("Depth", "Right", "Up", speed)
		motor_set("Depth", "Left", "Up", speed)
	elif x == "DOWN":
		motor_set("Depth", "Right", "Down", speed)
		motor_set("Depth", "Left", "Down", speed)
	elif x == "FORWARD":
		motor_set("Front", "Right", "Forward", speed)
		motor_set("Front", "Left", "Forward", speed)
		motor_set("Back", "Right", "Forward", speed)
		motor_set("Back", "Left", "Forward", speed)
	elif x == "REVERSE":
		motor_set("Front", "Right", "Reverse", speed)
		motor_set("Front", "Left", "Reverse", speed)
		motor_set("Back", "Right", "Reverse", speed)
		motor_set("Back", "Left", "Reverse", speed)
	#elif x == "custom":
	#	motor_set("Depth", "Left", "Up", speed)
	elif x == "run":
		time.sleep(2)
		motor_set("Depth", "Right", "Down", speed/2)
		motor_set("Depth", "Left", "Down", speed/2)
		time.sleep(5)
		motor_set("Depth", "Right", "Down", speed/4)
		motor_set("Depth", "Left", "Down", speed/4)
		time.sleep(5)
		motor_set("Front", "Right", "Forward", speed)
		motor_set("Front", "Left", "Forward", speed)
		motor_set("Back", "Right", "Forward", speed)
		motor_set("Back", "Left", "Forward", speed)
		time.sleep(20)		
		
