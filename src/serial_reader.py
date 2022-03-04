#!/usr/bin/env python

import serial

class SerialReader:
	def __init__(self, port, baud, data):
		self.port = port
		self.baud = baud
		self.data = data
		self.ser = serial.Serial(port, baud)

	def readLine(self):
		try:
			line = str(self.ser.readline().strip(), self.data)
			args = line.split(',')
			return int(args[1])
		except:
			return -1
