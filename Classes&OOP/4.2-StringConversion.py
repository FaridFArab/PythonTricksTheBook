# built-in mechanisms Python uses to handle how objects are represented as strings.
"""
You’ll be better off adding the __str__ and __repr__ “dunder” methods to your class. They are the Pythonic way to
control how objects are converted to strings in different situations
"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f'a {self.color} car with {self.mileage} mileage'

print(Car("Red", 140))

"""
The fact that these methods start and end in double underscores is simply a naming convention to flag them as core
Python features.
"""

# __str__ vs __repr__

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return '__repr__ for Car'
    def __str__(self):
        return '__str__ for Car'

"""
Inspecting an object in a Python interpreter session simply prints the result of the object’s __repr__.
Containers like lists and dicts always use the result of __repr__ to represent the objects they contain. 
Even if you call str on the container itself.
"""
import datetime

print(datetime.date.today())
print(repr(datetime.date.today()))

"""
My rule of thumb is to make my __repr__ strings unambiguous and helpful for developers, but I don’t expect them to 
be able to restore an object’s complete state.
If you don’t add a __str__ method, Python falls back on the result of __repr__ when looking for __str__. Therefore, I 
recommend that you always add at least a __repr__ method to your classes.
"""