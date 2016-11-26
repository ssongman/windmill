# encoding : utf-8
import threading, time

def MyThread(id):
    for i in range(10):
        print('id = {} --> {}'.format(id, i))
        time.sleep(0.01)

threads = []
for x in range(3):
    th = threading.Thread(target = MyThread, args = (x,))
    th.start()
    threads.append(th)

for t in threads:
    t.join()
print('exit')
