import threading
import yaml
from sensor_logging import Sensor


with open('Sensor_Info.yml') as f:
    sensor_info = yaml.load(f, Loader=yaml.FullLoader)

sensor_list = list(sensor_info.keys())

threads = []
sensors = []

for sensor in sensor_list:

    name = sensor_info[sensor]["Name"]
    rate = sensor_info[sensor]["Rate"]
    port = sensor_info[sensor]["Port"]
    baud = sensor_info[sensor]["Baud"]
    return_symbol = sensor_info[sensor]["Return_Symbol"]
    extra_char = sensor_info[sensor]["Extra_Char"]
    read_line = sensor_info[sensor]["Read_Line"]

    with open(name+'.csv', 'w') as creating_new_csv_file: 
        pass 
    print("Empty File Created Successfully")

    sensor = Sensor(name,rate,port,baud,return_symbol,extra_char,read_line)
    sensors.append(sensor)
    thread = threading.Thread(target=sensor.read)
    threads.append(thread)

