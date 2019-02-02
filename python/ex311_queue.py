###################################################
#
# file name  : ex311_queue.py
# executeoin : python3 ex311_queue.py
#
###################################################

import queue
#import PriorityQueue


def q_put():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()


def Average(lst): 
    return sum(lst) / len(lst) 


#q = queue.PriorityQueue()
q = queue.Queue()

# maxsize default 0 
q.maxsize= 5

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)


print("q :", q.queue)
print("q[3] :", q.queue[3])

## average
average = Average(q.queue)  
# Printing average of the list 
print("Average of the list =", round(average, 2)) 


print("q.empty: ", q.empty())
print("q.qsize: ", q.qsize())

rcv_data = q.get(block=True)
print("block=True: ", rcv_data)

rcv_data = q.get(block=False)
print("block=False: ", rcv_data)

print(q.get())
print(q.get())
print(q.get())

print("q.empty: ", q.empty())
print("q.qsize: ", q.qsize())




'''
<< LOG >>

q : deque([1, 2, 3, 4, 5])
q[3] : 4
Average of the list = 3.0
q.empty:  False
q.qsize:  5
block=True:  1
block=False:  2
3
4
5
q.empty:  True
q.qsize:  0

'''




