"""
Namedtuples can be a great alternative to defining a class manually, and they have some other interesting features.
Python’s tuples are a simple data structure for grouping arbitrary objects. Tuples are also immutable—they cannot
be modified once they’ve been created.
Namedtuples aim to solve these two problems. First of all, namedtuples are immutable containers, just like regular
tuples. Once you store data in top-level attribute on a namedtuple, you can’t modify it by updating the attribute.
All attributes on a namedtuple object follow the “write once, read many” principle. Besides that, namedtuples are,
well…named tuples. Each object stored in them can be accessed through a unique (human-readable) identifier. This frees
you from having to remember integer indexes, or resorting to workarounds like defining integer constants as
mnemonics for your indexes.
"""
import json
from collections import namedtuple
Car = namedtuple('Car' , 'color mileage')
"""
Since namedtuple has no way of knowing what the name of the variable is we’re assigning the resulting class to, 
we need to explicitly tell it which class name we want to use. The class name is used in the docstring and the __repr__ 
implementation that namedtuple automatically generates for us.
"""

Car2 = namedtuple('Car', ['color', 'mileage'])
my_car = Car2('Red', 3812.4)
print(my_car.color)

color, mileage = my_car

"""
Like tuples, namedtuples are immutable. When it comes to memory usage, they are also “better” than regular classes and 
just as memory efficient as regular tuples. Namedtuples are a memory efficient shortcut to defining an immutable class 
in Python manually.
"""

class MyCarWithMethods(Car):
    """
    It might be worth doing if you want a class with immutable properties, but it’s also easy to shoot yourself in the
    foot here. For example, adding a new immutable field is tricky because of how namedtuples are structured internally.
    The easiest way to create hierarchies of namedtuples is to use the base tuple’s _fields property:
    """
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

"""
_asdict() helper method returns the contents of a namedtuple as a dictionary.
The _make() classmethod can be used to create new instances of a namedtuple from a sequence or iterable.
"""

print(json.dumps(my_car._asdict()))

"""
Using namedtuples over unstructured tuples and dicts can also make my coworkers’ lives easier because they make the 
data being passed around “self-documenting” (to a degree).
"""