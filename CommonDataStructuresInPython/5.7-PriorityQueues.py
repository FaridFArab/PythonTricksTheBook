"""
A priority queue is a container data structure that manages a set of records with totally-ordered keys (for example,
a numeric weight value) to provide quick access to the record with the smallest or largest key in the set.
"""

# list – Maintaining a Manually Sorted Queue
"""
While the insertion point can be found in O(log n) time using bisect.insort40 in the standard library, this is always dominated
by the slow insertion step.
Maintaining the order by appending to the list and re-sorting also
takes at least O(n log n) time. Another downside is that you must manually take care of re-sorting the list when new elements are inserted.
It’s easy to introduce bugs by missing this step, and the burden is always on you, the developer.
"""

# heapq – List-Based Binary Heaps
"""
Since heapq technically only provides a min-heap implementation, extra steps must be taken to ensure sort stability 
and other features typically expected from a “practical” priority queue.
"""
import heapq
q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
while q:
    next_item = heapq.heappop(q)
    print(next_item)

# queue.PriorityQueue – Beautiful Priority Queues
"""
The difference is that PriorityQueue is synchronized and provides locking semantics to support multiple concurrent 
producers and consumers.
"""
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))
while not q.empty():
    next_item = q.get()
    print(next_item)