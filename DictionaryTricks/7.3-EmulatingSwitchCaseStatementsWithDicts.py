"""
The syntax for calling this function works as you’d intuitively expect—we simply use an index into the list and then
use the “()” call syntax for calling the function and passing arguments to it.
The core idea here is to define a dictionary that maps lookup keys for the input conditions to functions that will
carry out the intended operations.
"""

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y


print(dispatch_if("add", 1, 2))
print(dispatch_if("mul", 3, 2))

def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

"""
Every time we call dispatch_dict(), it creates a temporary dictionary and a bunch of lambdas for the opcode lookup.
if we really wanted to do some simple arithmetic like x + y, then we’d be better off using Python’s built-in operator 
module instead of the lambda functions used in the example.
"""

print(dispatch_dict("mul", 2, 8))
print(dispatch_dict("unknown", 2, 8))