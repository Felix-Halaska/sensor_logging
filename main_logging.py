import serial
import csv
from datetime import datetime
import time
import multiprocessing


class Sensor:
      
    def __init__(self,name,rate, port,baud,return_symbol,extra_char,read_line,send,date_time):
        """
        Creates empty variables and reads yaml file
        """
        self.value = 0
        self.readings = []
        self.value = 0

        self.threads = []

        self.ready = False

        self.name = name
        self.return_symbol = return_symbol
        self.extra_char = extra_char
        self.read_line = read_line
        self.rate = rate
        self.date_time = date_time
        self.send = send

        #write header row to csv file
        with open('sensor_data/'+self.name+self.date_time+".csv", "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([name, "Date/Time", "Exact Time [ns]"])

        #establish serial connection
        self.ser = serial.Serial(port,baud,timeout=1)
        self.ser.flush()
        
        self.send()


    def new_thread(self):
        thread = multiprocessing.Process(target=self.read)
        thread.start()
    
    def send(self):
        byte_message = self.send.encode('utf-8')
        self.ser.write(byte_message)

    def read(self):
        """
        Read sensor data and prepare it to be logged
        """
        cycle_start = time.perf_counter_ns()
        
        while True:

            #only read data if we don't have a string stored up
            if self.ready == True:
                current_time = time.perf_counter_ns()
            else:
                current_time = time.perf_counter_ns()

                #method for logging if the computer is having trouble logging line by line
                if self.read_line == False:

                    #read one character only
                    character = self.ser.read(1).decode()

                    #filter out any erroneous empty characters
                    if character == '\x00' or character == '':
                        pass
                    else:

                        #look for carriage return, and join characters together if found
                        if character == self.return_symbol:
                            self.value = float("".join(self.readings))
                            #print(f"{value=}")
                            self.ready = True

                            #filter out any extra characters after the carriage return character
                            for i in range(self.extra_char):
                                self.ser.read(1)
                        #add another character to the reading
                        else:
                            self.readings.append(character)
                
                #line by line logging
                else:
                    self.reading = self.ser.readline().decode()
                    print(self.reading)
                    #self.reading = self.reading[0:-2]
                    self.value = self.reading
                    #self.value = list(map(int, self.value))
                    self.ready = True

            #if one second has elapsed and there is a reading ready, log it
            # print(current_time-cycle_start)
            # print((1/self.rate)*1*10**9)
            # print(self.readings)
            # print(self.value)
            if current_time - cycle_start >= (1/self.rate) * 1*10**9 and self.ready == True:
                #print("Logging...")
                self.log()
                self.ready = False
                self.readings = []
                cycle_start = time.perf_counter_ns()
            else:
                pass

    def log(self):
        """ 
        Log a prepared reading, along with the date and time at which it was logged
        """
        print("Logging"+self.name+"...")
        print(self.value)
        with open('sensor_data/'+self.name+self.date_time+".csv", "a",newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([self.value, datetime.now(), time.perf_counter_ns()])
        
        
