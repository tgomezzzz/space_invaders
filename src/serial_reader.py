#!/usr/bin/env python

import serial

ser = serial.Serial('/dev/cu.wchusbserial533C0037561', 115200)

while(True):
  print(str(ser.readline().strip(), 'ascii'))
