import time
import threading
global run
run = True

def foo():
    global run
    while run:
        print '.',
        time.sleep(0)


t1 = threading.Thread(target=foo)

print 't1 run'
t1.run()
time.sleep(2)

print 'run=False'
run = False

#while True:
#    pass
             
time.sleep(5)


