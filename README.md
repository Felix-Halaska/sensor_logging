# A flexible data logging system for the CREST lab

This system is meant to make logging data during experiements easy, letting lab memebers spend time on science or navigation goals. 

## Raspberry Pi Setup

Step 1: Install Ubuntu 22.04 by following this tutorial, but make sure to image version 22.04 Desktop on the microSD card instead of 20.10.

Step 2: Add user to the dialout and tty groups
- Check what groups your user is in
	- $ groups
 - If this list does not contain both dialout and tty they should be added using the following commands, replacing “user” with your username
	- $ sudo usermod -a -G dialout user
	- $ sudo usermod -a -G tty user
 - Then log out and log back in to activate the changes

Step 3: Clone the sensor_logging repo onto the Raspberry Pi
- Navigate into the folder you want to clone the repo into
- Clone the repo using url/ssh(recommended)
	- $ git clone git@github.com:Felix-Halaska/sensor_logging.git

Step 4: Set a static IP address
- Connect to your local network
- Check the Raspberry Pi’s IP address
	- $ ip addr
- Copy the result under wlan (should be in the form of 192.168.XX.XX)
- Open up network settings and click on the IPv4 tab
- Under the IPv4 Method change the selection to Manual
- Under Routes add the IP address you copied earlier to the Address field, and 255.255.255.0 to the Netmask field

## VSCode Setup (Optional)

Step 1: Install the Remotes extension
- Connect your laptop and the Raspberry Pi to the same network
- Navigate to the extensions tab and search “remotes”
- Install the Remote - SSH extension from Microsoft
- Now open the view (View -> Open View…) and click on Remotes (Tunnels/SSH)
- Hit the + on the SSH line and type ssh user@IP (where user is your user on the Raspberry Pi, and IP is the Pi’s IP address)
- Enter your password
- You can now edit files stored on the Raspberry Pi directly from VSCode!

## Data Collection Setup

Step 1: Open Sensor_Info.yml in VSCode

Step 2: For each sensor that will be plugged in create a sensor instance in the YAML file which includes filling in the following fields:
- A header name for the sensor. This should be unique
- Name: The “name” of the sensor. This should be the data name that will be logged in the csv file, so include units if applicable!
- Rate: The rate of the sensor. This is the hz, or data points logged per second. Make sure that this does not exceed your sensor’s capabilities.
- Port: The port that the sensor is plugged into (In the form of ‘/dev/tty/USB0’ or ‘/dev/tty/USB1’). There are instructions to find this below in the appendix.
- Baud: The baud rate that the sensor communicates at. This is usually listed on its datasheet
- Read_Line: If you can read the sensor data line by line this should be set to True, if it can only read one character at a time it should be set to False. The default should be True
- Return_Character: If you only read one character at a time from your sensor, set this to be the newline/return character (the character that signals a new line of data. If you read full lines, leave this field blank
- Extra_Char: If you read only one character at a time and you read multiple newline/return characters, set this number to be the number of newline/return characters -1. If you read full lines from your sensor, leave this field blank
- Send: If you need to initialize your sensor with a serial command, write it here, otherwise leave it blank

## Data Collection Use

Step 1: Power on the Raspberry Pi

Step 2: Connect each sensor in the order in which you numbered them (i.e. the sensor assigned port “/dev/ttyUSB0” should be plugged in first, followed by “/dev/tty/USB1”

Step 3: Connect your laptop to the same network the Raspberry Pi is connected to

Step 4: ssh into the Raspberry Pi using the hostname previously set up

Step 5: Navigate into the /sensor_logging directory

Step 6: Run the logging script with the following command

- $ python3 initialize.py

Step 7: If a number of messages equal to the number of sensors plugged in print in the console saying “Empty File Created Successfully” the script is running correctly

Step 8: If any error messages print, or only one “Empty File Created Successfully” message prints, kill the operation and try until it succeeds

Step 9: The program should run indefinitely until it is stopped

