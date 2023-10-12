"""
While a regular function produces a single return value, generators produce a sequence of results. You could say they
generate a stream of values over the course of their lifetime.
"""
def integers():
    for i in range(1, 9):
        yield i
chain = integers()

print(chain)
print(list(chain))


def squared(seq):
    for i in seq:
        yield i * i

chain = squared(integers())
print(list(chain))
"""
My favorite thing about chaining generators is that the data processing happens one element at a time. There’s no 
buffering between the processing steps in the chain.
"""
integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)
"""
The only downside to using generator expressions is that they can’t be configured with function arguments, and you can’t
reuse the same generator expression multiple times in the same processing pipeline.

"""