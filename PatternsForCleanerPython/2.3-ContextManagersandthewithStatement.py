"""
This implementation won’t guarantee the file is closed if there’s an exception
during the f.write() call—and therefore our program might leak a file descriptor.
"""
import threading

f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()

some_lock = threading.Lock()
# Harmful:
some_lock.acquire()
try:
    # Do something...
    some_lock.locked()
finally:
    some_lock.release()

# Better:
"""
Instead of having to write an explicit try...finally statement each time, 
using the with statement takes care of that for us.
"""
with some_lock:
    # Do something...
    some_lock.locked()

"""
What’s a context manager? It’s a simple “protocol” (or interface) that your object needs to follow in 
order to support the with statement. Basically, all you need to do is add __enter__ and __exit__ methods to an object 
if you want it to function as a context manager. Python will call these two methods at the appropriate times 
in the resource management cycle.
"""


class ManagedFile:
    """
    Python calls __enter__ when execution enters the context of the with statement, and it’s time to acquire
    the resource. When execution leaves the context again, Python calls __exit__ to free up the resource.
    """

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')

from contextlib import contextmanager

"""
A downside of the @contextmanager-based implementation might be that it requires some understanding of advanced 
Python concepts like decorators and generators.
"""


@contextmanager
def managed_file(name):
    try:
        file = open(name, 'w')
        yield file
    finally:
        file.close()


with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)


with Indenter() as indent:
    indent.print('hi!')
with indent:
    indent.print('hello')
with indent:
    indent.print('bonjour')
    indent.print('hey')
"""
output:
>>> 
hi!
    hello
        bonjour
hey
"""
