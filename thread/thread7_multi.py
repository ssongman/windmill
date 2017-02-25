#from multiprocessing import Process
from threading import Thread
import time

def a():
    global mode
    for idx in range(1,10):
        print('a: ' + str(idx) + ', mode: ' + mode)
        time.sleep(1)
        if idx == 5:
            mode = 'S'
            break
 
def b():
    global mode
    for idx in range(1,10):
        print('b: ' + str(idx) + ', mode: ' + mode)
        time.sleep(1)
        if mode <> 'F' :
            break
 
def c():
    for idx in range(1,10):
        print('c: ' + str(idx) + ', mode: ' + mode)
        time.sleep(1)
 
 
if __name__ == '__main__':
    p1 = Thread(target = a, args=())
    p2 = Thread(target = b, args=())
    p3 = Thread(target = c, args=())
    print("process did")
    time.sleep(2)
    
    mode='F'
    p1.start()
    print("p1 started")
    p2.start()
    print("p2 started")
    p3.start()
    print("p3 started")
    
    print("p1 join start")
    p1.join()
    print("p1 joined")
    p2.join()
    print("p2 joined")
    p3.join()
    print("p3 joined")
    
print("Program END")
