#
# PCA8591_TEST.py
#
#

import smbus  # i2c 
import time   # sleep 

bus = smbus.SMBus(1) #i2c  setting

add = 0x48   # PCF8591T address

def readAD() :  # 
  analog = bus.read_byte(add) #analog  
  return analog               #analog  

while(1) : # 
  bus.write_byte(add, 0x00) # 0 
  time.sleep(0.1)           # 
  readAD()                  # destroy garbage 
  an0 = readAD()            # 

  bus.write_byte(add, 0x01) # 1
  time.sleep(0.1)
  readAD()
  an1 = readAD()

  bus.write_byte(add, 0x02)
  time.sleep(0.1)
  readAD()
  an2 = readAD()

  bus.write_byte(add, 0x03)
  time.sleep(0.1)
  readAD()
  an3 = readAD()

  print "value = %3d, %3d, %3d, %3d" % (an0, an1, an2, an3) # 
  
  # conversion1
  cm = pow(3027.4 / an0, 1.2134) # conversion cm
  print "an[%3d] [%3d] cm"  % (an0, cm)  # 
  
  # conversion2 [sharp 10-80]
  cm = 4800 / (an0 - 20)
  print "[sharp 10-80] an[%3d] [%3d] cm"  % (an0, cm)  # 
  

  # conversion3 [sharp 20-150]
  cm = 9642 / (an0 - 16.92)
  print "[sharp 20-150] an[%3d] [%3d] cm"  % (an0, cm)  # 
  

  # conversion [sharp 4-30]
  cm = 2076 / (an0 - 11)
  print "[sharp 4-30] an[%3d] [%3d] cm"  % (an0, cm)  # 
  print "==========================================================="
  time.sleep(1)
  

