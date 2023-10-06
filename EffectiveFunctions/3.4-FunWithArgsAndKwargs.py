import functools


def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo('hello', 1,2,3,)
print('*' * 150)
foo('hello', 1,2,3, key1='bar', key2='zoo')

"""
You can do so by using the argument-unpacking operators * and ** when calling the function you want to forward 
arguments to.
"""

def f1(x, *args, **kwargs):
    """
    This technique can be useful for subclassing and writing wrapper functions.
    :param x:
    :param args:
    :param kwargs:
    :return:
    """
    kwargs['name'] = 'Farid'
    new_args = args + ('extra',)
    # bar(x, *new_args, **kwargs)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

print('*' * 150)
print(AlwaysBlueCar('green', 48932).color)

def trace(f):
    """
    One more scenario where this technique is potentially helpful is writing wrapper functions such as decorators.
    There you typically also want to accept arbitrary arguments to be passed through to the wrapped function.
    :param f:
    :return:
    """
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function

"""
It’s sometimes difficult to balance the idea of making your code explicit enough and yet adhere to the Don’t Repeat 
Yourself (DRY) principle. This will always be a tough choice to make.
"""