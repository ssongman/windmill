from threading import Thread
import time

a = 0  #global variable

def thread1(threadname):
    while True:
        print('[thread1] a: ' + str(a))
        time.sleep(1)
        if a > 10:
            print 'thread1 end'
            break

def thread2(threadname):
    global a

    while True:
        a += 1
        print('[thread2] a: ' + str(a))
        time.sleep(1)
        if a > 10:
            print 'thread2 end'
            break


thread1 = Thread( target=thread1, args=("Thread-1", ) )
thread2 = Thread( target=thread2, args=("Thread-2", ) )
print("thread constructor")

time.sleep(2)
a=0
print("before start1")
thread1.start()
print("before start2")
thread2.start()

print("before join1")
thread1.join()
print("before join2")
thread2.join()


print("Program END")
