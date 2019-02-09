###################################################
#
# File name   : ex711_bluetooth_basic.py
# Execution   : 
#               cd /home/pi/song/windmill/python
#               python ex711_bluetooth_basic.py
#               python3 ex711_bluetooth_basic.py
#
# Description :
#         v0.5: GUI Setting
#         v0.6: add BLE Setting
#         v1.0: add range alert
#
###################################################

import bluetooth

print ("looking for nearby devices...")
try:
    nearby_devices = bluetooth.discover_devices(lookup_names = True, flush_cache = True, duration = 20)
    #nearby_devices = bluetooth.discover_devices(lookup_names = True)
    print ("found %d devices" % len(nearby_devices))
    print ("nearby_devices : ", nearby_devices)
except:
    print ("exception occured")
    print ("error accessing bluetooth device...")
    sys.exit(1)



for addr, name in nearby_devices:
    print ("addr[%s], name[%s]" % (addr, name))

if (len(nearby_devices) == 0):
    print("no devices")
else:
    for services in bluetooth.find_service(address = addr):
        print (" Name: %s" % (services["name"])               )
        print (" Description: %s" % (services["description"]) )
        print (" Protocol: %s" % (services["protocol"])       )
        print (" Provider: %s" % (services["provider"])       )
        print (" Port: %s" % (services["port"])               )
        print (" Service id: %s" % (services["service-id"])   )
        print (""                                             )
        print (""                                             )
    # end for
# end if

