"""
The lambda keyword in Python provides a shortcut for declaring small anonymous functions. Lambda functions behave just
like regular functions declared with the def keyword.
"""
add = lambda x,y: x + y
print(add(3,4))


"""
Lambda functions are restricted to a single expression. This means a lambda function can’t use statements or 
annotations—not even a return statement, so there’s always an implicit return statement. Because lambdas can be 
anonymous, you don’t even need to assign them to a name first.
"""
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x:x[1]))

print(sorted(range(-5,6), key=lambda x: x * x))
"""
you have more concise implementations in Python using the built-in operator.itemgetter() and abs() functions.
"""

def make_add(n):
    return lambda x: x + n

plus_3 = make_add(3)
plus_5 = make_add(5)

print(plus_5(2))
print(plus_3(2))

"""
Sometimes, using a lambda function instead of a nested function declared with the def keyword can express 
the programmer’s intent more clearly.
"""
# Harmful
class Car:
    rev = lambda self: print("Wroom!")
    crash = lambda self: print("Boom!")

my_car = Car()
my_car.crash()

# Harmful
print(list(filter(lambda x: x % 2 == 0, range(16))))

# Better
print([x for x in range(16) if x % 2 == 0])