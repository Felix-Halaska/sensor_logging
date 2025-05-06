import serial

port = 'dev/ttyUSB0'
baud = 9600
read_line = True
return_character = '\r'

sensor = serial.Serial(port,baud)
print("Serial Connection Open")


readings = []

while True:

    if read_line == True:
        readings = sensor.readline().decode()
        print(readings)
    else:
        character = sensor.read(1).decode()
        print(character)
        if character == return_character:
            value = float("".join(readings))
            print(value)
            readings = []
        else:
            readings.append(character)
            print(readings)

    
