# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import bluetooth._bluetooth as bluez

dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print "ble thread started"
except:
    print "error accessing bluetooth device..."
    sys.exit(1)


blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
    returnedList = blescan.parse_events(sock, 10)
    print "----------"
    for beacon in returnedList:
        lt_be = beacon.split(',')
        #print lt_be
        if lt_be[2] == '501':   # major
            print beacon
    

'''
<< LOG >>
ble thread started
----------
54:b1:90:2f:95:7b,0103017b952f90b1540b0aff750077e4,64237,35505,119,-87
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-77
d5:b1:61:f2:eb:d0,24ddf4118cf1440c87cde368daf9c93e,501,20783,-71,-56
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-89
4b:bc:e9:7a:cd:bb,010301bbcd7ae9bc4b0b0aff750077e4,64237,35505,119,-83
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-88
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-77
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-78
f5:bb:54:4a:01:0c,24ddf4118cf1440c87cde368daf9c93e,501,20781,-71,-74
----------
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-77
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-74
d5:b1:61:f2:eb:d0,24ddf4118cf1440c87cde368daf9c93e,501,20783,-71,-55
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-77
4b:bc:e9:7a:cd:bb,010301bbcd7ae9bc4b0b0aff750077e4,64237,35505,119,-85
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-79
54:b1:90:2f:95:7b,0103017b952f90b1540b0aff750077e4,64237,35505,119,-85
d5:99:f7:ad:35:57,24ddf4118cf1440c87cde368daf9c93e,501,20782,-71,-56
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-77
c9:51:05:49:72:d7,030366660319d007020a0509ffee03d7,29257,1361,-55,-89
'''
