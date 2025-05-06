import yaml
from main_logging import Sensor
from datetime import datetime


with open('Sensor_Info.yml') as f:
    sensor_info = yaml.load(f, Loader=yaml.FullLoader)

sensor_list = list(sensor_info.keys())

#threads = []
sensors = []

for sensor in sensor_list:

    name = sensor_info[sensor]["Name"]
    rate = sensor_info[sensor]["Rate"]
    port = sensor_info[sensor]["Port"]
    baud = sensor_info[sensor]["Baud"]
    return_symbol = sensor_info[sensor]["Return_Symbol"]
    extra_char = sensor_info[sensor]["Extra_Char"]
    read_line = sensor_info[sensor]["Read_Line"]
    send = sensor_info[sensor]["Send"]
    date_time = str(datetime.now())

    with open('sensor_data/'+name+date_time+'.csv', 'w') as creating_new_csv_file: 
        pass 
    print("Empty File Created Successfully")

    sensor = Sensor(name,rate,port,baud,return_symbol,extra_char,read_line,send,date_time)
    sensors.append(sensor)
    Sensor.new_thread(sensor)

