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


