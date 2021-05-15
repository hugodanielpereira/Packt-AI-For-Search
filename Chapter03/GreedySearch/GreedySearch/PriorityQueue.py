'''
@author: Devangini Patel

Reference: https://docs.python.org/2/library/queue.html
'''
from queue import PriorityQueue

pqueue = PriorityQueue()
print(pqueue.qsize())

pqueue.put((5, 'A'))
pqueue.put((10, 'B'))
pqueue.put((1, 'C'))
pqueue.put((5, 'D'))

print(pqueue.qsize())

while not pqueue.empty(): 
    print(pqueue.get())
    
print(pqueue.qsize())
