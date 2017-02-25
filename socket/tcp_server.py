#!/usr/bin/env python
#import video_dir
#import car_dir
#import motor
from socket import *
from time import ctime          # Import necessary modules   

ctrl_cmd = ['F', 'B', 'L', 'R', 'S', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']
#ctrl_cmd = ['F', 'B', 'L', 'R', 'S', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']


#HOST = socket.gethostname()  # Get local machine name
HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 5001
BUFSIZ = 2       # Size of the buffer, 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     # The parameter of listen() defines the number of connections permitted at one time. Once the 
                         # connections are full, others will be rejected. 

#video_dir.setup()
#car_dir.setup()
#motor.setup()     # Initialize the Raspberry Pi GPIO connected to the DC motor. 
#video_dir.home_x_y()
#car_dir.home()

def loop():
   while True:
      print 'Waiting for connection...'
      # Waiting for connection. Once receiving a connection, the function accept() returns a separate 
      # client socket for the subsequent communication. By default, the function accept() is a blocking 
      # one, which means it is suspended before the connection comes.
      tcpCliSock, addr = tcpSerSock.accept() 
      print '...connected from :', addr     # Print the IP address of the client connected with the server.
      
      while True:
         data = tcpCliSock.recv(BUFSIZ)    # Receive data sent from the client. 
         print 'data :['+data+']'
         # Analyze the command received and control the car accordingly.
         if not data:
            break
         
         if data[0] == 'F':
         	print 'forward...'
         	#motor.ctrl(1, 1)
         elif data[0] == 'B':
         	print 'backward...'
         	#motor.ctrl(1, -1)
         elif data[0] == 'L':
         	print 'left...'
         	#car_dir.turn_left()
         elif data[0] == 'R':
         	print 'right...'
         	#car_dir.turn_right()
         elif data[0] == 'S':
         	print 'stop...'
         	#motor.ctrl(0)
         #elif data == ctrl_cmd[5]:
         #	print 'read cpu temp...'
         #	temp = cpu_temp.read()
         #	tcpCliSock.send('[%s] %0.2f' % (ctime(), temp))
         #elif data == ctrl_cmd[6]:
         #	print 'recv home cmd'
         #	#car_dir.home()
         #elif data == ctrl_cmd[8]:
         #	print 'recv x+ cmd'
         #	video_dir.move_increase_x()
         #elif data == ctrl_cmd[9]:
         #	print 'recv x- cmd'
         #	video_dir.move_decrease_x()
         #elif data == ctrl_cmd[10]:
         #	print 'recv y+ cmd'
         #	video_dir.move_increase_y()
         #elif data == ctrl_cmd[11]:
         #	print 'recv y- cmd'
         #	video_dir.move_decrease_y()
         #elif data == ctrl_cmd[12]:
         #	print 'home_x_y'
         #	video_dir.home_x_y()
         #elif data[0:5] == 'speed':     # Change the speed
         #	print data
         #	numLen = len(data) - len('speed')
         #	if numLen == 1 or numLen == 2 or numLen == 3:
         #		tmp = data[-numLen:]
         #		print 'tmp(str) = %s' % tmp
         #		spd = int(tmp)
         #		print 'spd(int) = %d' % spd
         #		if spd < 24:
         #			spd = 24
         #		motor.setSpeed(spd)
         else:
         	print 'cmd error !'
      # end while
   # end while

   tcpSerSock.close()
   print 'tcpSerSock closed 1'


if __name__ == "__main__":
   try:
      loop()
   except KeyboardInterrupt:
      tcpSerSock.close()
   print 'tcpSerSock closed 2'
