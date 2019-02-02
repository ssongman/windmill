###################################################
#
# file name  : ex31_queue.py
# executeoin : python3 ex312_queue.py
#
###################################################

import queue

q = queue.Queue()


for i in range(5):
    q.put(i)

print(q.maxsize)

while not q.empty():
    print(q.get(), end = '\n')








