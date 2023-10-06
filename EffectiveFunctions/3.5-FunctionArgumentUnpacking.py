# Function Argument Unpacking using the * operator

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]


print_vector(*tuple_vec)
print_vector(*list_vec)
"""
Putting a * before an iterable in a function call will unpack it and pass its elements as separate positional arguments 
to the called function.
"""

genexpr = (x * x for x in range(3))
print_vector(*genexpr)

"""
There’s also the ** operator for unpacking keyword arguments from dictionaries.
"""
dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)
"""
If you were to use the single asterisk (*) operator to unpack the dictionary, keys would be passed to the function 
in random order instead.
"""
print_vector(*dict_vec)