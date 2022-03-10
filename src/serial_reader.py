import serial

JOYSTICK_REST = 2000

class SerialReader:
	def __init__(self, port, baud, data):
		self.port = port
		self.baud = baud
		self.data = data
		self.ser = serial.Serial(port, baud)
		self.prev_potentiometer = -1

	def readLine(self):
		try:
			line = str(self.ser.readline().strip(), self.data)
			print(line)
			self.ser.reset_input_buffer()
			args = line.split(',')
			p = int(args[0])
			j = int(args[1])
			b = int(args[2])
			return self.potentiometerChange(p), self.getMotion(j), b
		except:
			print("exception")
			return [0, 2000, 1]

	def getMotion(self, joystick):
		return int(((joystick - JOYSTICK_REST) / 200))

	def potentiometerChange(self, potentiometer):
		result = self.prev_potentiometer != -1 and abs(potentiometer - self.prev_potentiometer) > 20
		print(abs(potentiometer - self.prev_potentiometer))
		self.prev_potentiometer = potentiometer
		return result