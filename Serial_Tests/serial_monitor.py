import serial

#sensor = serial.Serial('/dev/ttyACM0',9600)
sensor = serial.Serial('/dev/ttyUSB0',9600)
sensor.write(b'C,1<cr>')
print("Sensor 0 Command Sent")


readings = []
data = []

while True:
    
    character = sensor.read(1).decode()
    print(character)
    if character == '\r':
        value = float("".join(readings))
        print(f"{value=}")
        data.append(value)
        readings = []
        sensor.read(1).decode()
    else:
        #value = float(character)
        readings.append(character)
        print(readings)

    
