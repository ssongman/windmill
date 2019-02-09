###################################################
#
# File name   : ex712_bluetooth_basic.py
# Execution   : 
#               cd /home/pi/song/windmill/python
#               python ex712_bluetooth_basic.py
#               python3 ex712_bluetooth_basic.py
#
# Description :
#         v0.5: GUI Setting
#         v0.6: add BLE Setting
#         v1.0: add range alert
#
###################################################

# Dependencies:
# sudo apt-get install python-bluetooth
import bluetooth

print("Searching for Bluetooth devices....")
devices = bluetooth.discover_devices()
for addr in devices:
    print("Found device: {}".format(addr))



