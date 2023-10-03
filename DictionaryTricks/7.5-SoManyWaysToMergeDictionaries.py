"""
sometimes you need a way to merge two or more dictionaries into one, so that the resulting dictionary contains a
combination of the keys and values of the source dicts.
"""
xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}
ts = {'d': 2, 'e':5}
# print(xs + ys) : TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

"""
The classical solution for the “merging multiple dictionaries” problem in Python is to use the built-in dictionary 
update() method.
"""
# Strategy 1
zs = dict()
zs.update(xs)
zs.update(ys)
print(zs)
"""
def update(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = value
"""

# Strategy 2
"""
uses the dict() built-in combined with the **-operator for “unpacking” objects
"""

ws = dict(xs,**ys)
print(ws)

"""
Starting with Python 3.5, the **-operator became more flexible.4 So in Python 3.5+ there’s another—and arguably 
prettier—way to merge an arbitrary number of dictionaries.
"""

fs = {**xs, **ts, **ys}
print(fs)

"""
Using the **-operator is also faster than using chained update() calls.It still remains sufficiently readable.
"""