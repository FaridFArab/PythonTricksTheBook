"""
Python’s decorators allow you to extend and modify the behavior of a callable (functions, methods, and classes)
without permanently modifying the callable itself.
• logging
• enforcing access control and authentication
• instrumentation and timing functions
• rate-limiting
• caching, and more
They “decorate” or “wrap” another function and let you execute code before and after the wrapped function runs.
A decorator is a callable that takes a callable as input and returns another callable.
"""

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return "Hello"

print(greet())

"""
Decorators modify the behavior of a callable through a wrapper closure so you don’t have to permanently 
modify the original. Multiple decorators executed from bottom to top but deep levels of decorator stacking will 
eventually have an effect on performance because they keep adding nested
function calls.
"""

# Decorating Functions That Accept Arguments
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
        f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
        f'returned {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

print(say("Farid", "Hello World"))

"""
functools.wraps decorator included in Python’s standard library
"""

import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper