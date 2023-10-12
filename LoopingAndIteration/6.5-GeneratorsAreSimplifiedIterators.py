# Infinite Generators
class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value

def repeater(value):
    """
    use yield to pass data back to the caller
    :param value:
    :return:
    """
    while True:
        yield value

"""
When a return statement is invoked inside a function, it permanently passes control back to the caller of the function. 
When a yield is invoked, it also passes control back to the caller of the function—but it only does so temporarily.
Whereas a return statement disposes of a function’s local state, a yield statement suspends the function and retains 
its local state. In practical terms, this means local variables and the execution state of the generator function are 
only stashed away temporarily and not thrown out completely. Execution can be resumed at any time by calling next() 
on the generator.
"""
iterator = repeater('Hi')
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generators That Stop Generating
"""
Generators stop generating values as soon as control flow returns from the generator function by any means other than a
yield statement. This means you no longer have to worry about raising StopIteration at all!

"""