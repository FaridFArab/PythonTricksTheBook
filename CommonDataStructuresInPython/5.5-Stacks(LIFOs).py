"""
Depth-first search (DFS) on a tree or graph data structure.
"""

# list – Simple, Built-In Stacks
"""
Performance less consistent than the stable O(1) inserts and deletes provided by a linked list based implementation 
(like collections.deque, see below). On the other hand, lists do provide fast O(1) time random access to elements on the
stack, and this can be an added benefit.
To get the amortized O(1) performance for inserts and deletes, new items must be added to the end of the list with the 
append() method and removed again from the end using pop().
Adding and removing from the front is much slower and takes O(n) time, as the existing elements must be shifted around 
to make room for the new element. This is a performance anti pattern that you should avoid as much as possible.
"""
s = []
s.append('eat')
s.append('sleep')
s.append('code')
s.pop()
print(s)

# collections.deque – Fast & Robust Stacks
"""
The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time 
(non amortized). Because deques support adding and removing elements from either end equally well, they can serve both 
as queues and as stacks. Python’s deque objects are implemented as doubly-linked lists which gives them excellent and 
consistent performance for inserting and deleting elements, but poor O(n) performance for randomly accessing elements 
in the middle of a stack.
"""

from collections import deque
s = deque()
s.append('eat')
s.append('sleep')
s.append('code')
print(s)
s.pop()
s.pop()
s.pop()
# s.pop() # IndexError: pop from an empty deque

# queue.LifoQueue – Locking Semantics for Parallel Computing
"""
This stack implementation in the Python standard library is synchronized and provides locking semantics to support 
multiple concurrent producers and consumers.
"""

from queue import LifoQueue
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')
print(s)
s.get()
s.get()
s.get()
s.get_nowait()

# Comparing Stack Implementations in Python
"""
If you’re not looking for parallel processing support (or don’t want to handle locking and unlocking manually), your 
choice comes down to the built-in list type or collections.deque.
Not only is its performance more stable, the deque class is also easier to use because you don’t have to worry about 
adding or removing items from “the wrong end.”
"""