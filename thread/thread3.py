#!/usr/bin/python 
import thread, time

exit_var = 0

# thread Function
def counter(id):
    global exit_var
    for i in range(100):
        if exit_var == 1 :
            print 'exit'
            break
        print 'id %s --> %s' % (id, i)
        time.sleep(0.1)

# thread 5
for i in range(100):
    thread.start_new_thread(counter, (i,))

# wait
time.sleep(2)
exit_var = 1
time.sleep(5)
print 'Exiting'