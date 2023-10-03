"""
In [1]: {True: 'yes', 1: 'no', 1.0: 'maybe'}
Out[1]: {True: 'maybe'}
"""
xs = dict()
xs[True] = 'yes'
xs[1] = 'no'
xs[1.0] = 'maybe'
#  True == 1 == 1.0 --> True
"""
Python Docs:
    “The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respectively, 
    in almost all contexts, the exception being that when converted to a string, the strings ‘False’ or ‘True’ 
    are returned, respectively“.
"""
"""
>>> ['no', 'yes'][True]
'yes'
"""

"""
Python’s dictionaries don’t update the key object itself when a new value is associated with it:
>>> ys = {1.0: 'no'}
>>> ys[True] = 'yes'
>>> ys
{1.0: 'yes'}
"""