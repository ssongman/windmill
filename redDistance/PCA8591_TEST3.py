#
# PCA8591_TEST2.py
# Read a value from analogue input 0
#

import smbus  # i2c 
import time   # sleep 

bus = smbus.SMBus(1) #i2c  setting   set control register to read channel 0

PCA8591_ADD = 0x48   # PCA8591 address

# PCA8591 analog pin
PCA8591_AIN0 = 0x00  # AIN0
PCA8591_AIN1 = 0x01  # AIN1
PCA8591_AIN2 = 0x02  # AIN2  -- OK
PCA8591_AIN3 = 0x03  # AIN3



def get_distance_f():
    bus.write_byte(PCA8591_ADD, PCA8591_AIN0)    # pin
    volts = bus.read_byte(PCA8591_ADD)           # destroy garbage 
    volts = bus.read_byte(PCA8591_ADD)           # 
    
    # conversion [sharp 4-30] SennsorValue range 80-530
    if volts >= 0 and volts <= 530:
        distance = 2076 / (volts - 11)
    else:
        distance = 0
    #print "[sharp 4-30] volts[%3d] [%3d] cm"  % (volts, distance)  # 
    
    return distance


def get_distance_b():
    bus.write_byte(PCA8591_ADD, PCA8591_AIN1)    # pin
    volts = bus.read_byte(PCA8591_ADD)           # destroy garbage 
    volts = bus.read_byte(PCA8591_ADD)           # 
    
    # conversion [sharp 4-30] SennsorValue range 80-530
    if volts >= 0 and volts <= 530:
        distance = 2076 / (volts - 11)
    else:
        distance = 0
    #print "[sharp 4-30] volts[%3d] [%3d] cm"  % (volts, distance)  # 
    
    return distance


while(1) : # 
    distance_f = get_distance_f()
    distance_b = get_distance_b()
    print "[distance] f[%3d] cm,  b[%3d] cm"  % (distance_f, distance_b)  # 
    time.sleep(1)
  

