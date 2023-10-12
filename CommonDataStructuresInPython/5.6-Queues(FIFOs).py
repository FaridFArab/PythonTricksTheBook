"""
A queue is a collection of objects that supports fast first-in, first-out (FIFO) semantics for inserts and deletes.
The insert and delete operations are sometimes called enqueue and dequeue. Unlike lists or arrays, queues typically
don’t allow for random access to the objects they contain.
Queues have a wide range of applications in algorithms and often help solve scheduling and parallel programming
problems. A short and beautiful algorithm using a queue is breadth-first search (BFS) on a tree or graph data structure.
"""
# list — Terribly Sloooow Queues
"""
It’s possible to use a regular list as a queue but this is not ideal from a performance perspective.34 Lists are quite 
slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other 
elements by one, requiring O(n) time.
"""

# collections.deque – Fast & Robust Queues
from collections import deque
q = deque()
q.append('eat')
q.append('sleep')
q.append('code')
print(q)
q.pop()
q.popleft()
print(q)

# queue.Queue – Locking Semantics for Parallel Computing

from queue import Queue
q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')
print(q)
print(q.get())

# multiprocessing.Queue – Shared Job Queues
"""
As a specialized queue implementation meant for sharing data between processes, multiprocessing.Queue makes it easy to 
distribute work across multiple processes in order to work around the GIL limitations. This type of queue can store and
transfer any pickle-able object across process boundaries.
"""
from multiprocessing import Queue
q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')
print(q)
q.get()
q.get()
q.get()
# q.get() # Blocks / waits forever...

