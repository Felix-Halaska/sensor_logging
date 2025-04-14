import serial

sensor_0 = serial.Serial('/dev/ttyUSB0',9600)
sensor_0.write(b'C,1<cr>')
print("Sensor 0 Command Sent")

sensor_1 = serial.Serial('/dev/ttyUSB1',9600)
sensor_1.write(b'C,1<cr>')
print("Sensor 1 Command Sent")

readings_0 = []
data_0 = []

readings_1 = []
data_1 = []

while True:
    character_0 = sensor_0.read(1).decode()
    if character_0 == '\x00':
        pass
    else:
        if character_0 == '\r':
            value_0 = float("".join(readings_0))
            print(f"{value_0=}")
            data_0.append(value_0)
            readings_0 = []
        else:
            readings_0.append(character_0)

    character_1 = sensor_1.read(1).decode()
    if character_1 == '\x00':
        pass
    else:
        if character_1 == '\r':
            value_1 = float("".join(readings_1))
            print(f"{value_1=}")
            data_1.append(value_1)
            readings_1 = []
        else:
            #value = float(character)
            readings_1.append(character_1)