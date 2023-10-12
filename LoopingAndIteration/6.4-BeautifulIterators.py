# Objects that support the __iter__ and __next__ dunder methods automatically work with for-in loops.


class RepeaterIterator:
    def __init__(self, source):
        self.source = source #5
    def __next__(self):
        return self.source.value #7

class Repeater:
    def __init__(self, value):
        self.value = value #2
    def __iter__(self):
        return RepeaterIterator(self) #4

"""
We first initialize the cursor and prepare it for reading, and then we can fetch data from it into local variables as 
needed, one element at a time. Because there’s never more than one element “in flight,” this approach is highly 
memory-efficient.
Iterators provide a common interface that allows you to process every element of a container while being completely 
isolated from the container’s internal structure.
I took the opportunity here to replace the calls to __iter__ and __next__ with calls to Python’s built-in functions, 
iter() and next().
"""

if __name__ == '__main__':
    repeater = Repeater('Hello') #1
    for item in repeater: #3
        print(item) #6

"""
Python iterators normally can’t be “reset”—once they’re exhausted they’re supposed to raise StopIteration every time 
next() is called on them. To iterate anew you’ll need to request a fresh iterator object with the iter() function.
Being able to write a three-line for-in loop instead of an eight-line while loop is quite a nice improvement. It makes 
the code easier to read and more maintainable. And this is another reason why iterators in Python are such a powerful 
tool.
"""