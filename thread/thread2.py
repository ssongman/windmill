# encoding : utf-8
import threading, time

class myThread(threading.Thread):
    def run(self):
        for i in range(10):
            print('id = {} --> {}'.format(self.getName(), i))
            time.sleep(0)

threads = []
for x in range(3):
    th = myThread()
    th.start()
    threads.append(th)

for t in threads:
    t.join()
print('exit')
