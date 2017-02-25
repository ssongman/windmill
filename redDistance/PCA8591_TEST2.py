#
# PCA8591_TEST2.py
#
#

import smbus  # i2c 
import time   # sleep 

bus = smbus.SMBus(1) #i2c  setting

add = 0x48   # PCA8591 address

# analog pin
#0x00  # AIN0
#0x01  # AIN1
#0x02  # AIN2
#0x03  # AIN3



while(1) : # 
  bus.write_byte(add, 0x03) # 0 
  #time.sleep(0.1)          # 
  bus.read_byte(add)                 # destroy garbage 
  an = bus.read_byte(add)           # 


  # conversion [sharp 4-30]
  cm = 2076 / (an - 11)
  print "[sharp 4-30] an[%3d] [%3d] cm"  % (an, cm)  # 
  time.sleep(1)
  

