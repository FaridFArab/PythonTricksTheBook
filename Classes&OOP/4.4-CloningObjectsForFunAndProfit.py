"""
Assignment statements in Python do not create copies of objects, they only bind names to an object.
For immutable objects, that usually doesn't make a difference.
"""


xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
"""
when you modify one of the child objects in xs, this modification will be reflected in ys as well—that’s 
because both lists share the same child objects. The copy is only a shallow.
"""
xs.append(['new sublist'])
print(xs is ys, xs == ys)

import copy
zs = copy.deepcopy(xs)
xs[1][0] = 'X'
print(xs is zs, xs == zs)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

a = Point(23, 42)
b = Point(23, 42)
"""
Because our point object uses primitive types (ints) for its coordinates, there’s no difference between a shallow and 
a deep copy in this case.
"""
print(a is b)

"""
Objects can control how they’re copied by defining the special methods __copy__() and __deepcopy__() on them.
"""