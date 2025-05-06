import serial

port = '/dev/ttyUSB0'
baud = 9600
message = 'C,1<cr>'
byte_message = message.encode('utf-8')

ser = serial.Serial(port,baud,timeout=1)
ser.write(byte_message)