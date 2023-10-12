# Once a generator expression has been consumed, it can’t be restarted or reused.

# Generator Expressions vs List Comprehensions
listcomp = ['Hello' for i in range(3)]
genexpr = ('Hello' for i in range(3))

"""
You can also call the list() function on a generator expression to construct a list object holding all generated value.
"""
genexpr = ("Hello" for i in range(3))
print(list(genexpr))

"""
Please don’t write deeply nested generator expressions. It’s often better to write a generator function or even a 
class-based iterator. If you need to use nested generators and complex filtering conditions, it’s usually better to 
factor out sub-generators (so you can name them) and then to chain them together again at the top level.
"""