# A function doesn't specify a return value, it returns None by default.

def foo1(value):
    if value:
        return value
    else:
        return None
def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return
def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value

print(type(foo1(0)))
print(type(foo2(0)))
print(type(foo3(0)))

"""
If a function doesn't have a return value (other languages would call this a procedure), then I will leave out the 
return statement.
"""