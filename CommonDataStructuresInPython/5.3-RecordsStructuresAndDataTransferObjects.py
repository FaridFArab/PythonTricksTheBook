# dict – Simple Data Objects
"""
Dictionaries are also often called maps or associative arrays and allow for the efficient lookup, insertion, and
deletion of any object associated with a given key. Data objects created using dictionaries are mutable.
"""
dict_car1 = {
'color': 'red',
'mileage': 3812.4,
'automatic': True,
}
dict_car2 = {
'color': 'blue',
'mileage': 40231,
'automatic': False,
}

# tuple – Immutable Groups of Objects
"""
Python’s tuples are simple data structures for grouping arbitrary objects. Tuples are immutable—they cannot be modified 
once they’ve been created. Performance-wise, tuples take up slightly less memory than lists in
CPython, and they’re also faster to construct.
"""
import dis
dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval'))
print('*' * 150)
dis.dis(compile("[23, 'a', 'b', 'c']", '', 'eval'))

"""
a tuple is always an ad-hoc structure: It’s difficult to ensure that two tuples have the same number of fields and the 
same properties stored on them.
"""

tuple_car1 = ('red', 3812.4, True)
tuple_car2 = ('blue', 40231.0, False)


# Writing a Custom Class – More Work, More Control
"""
Classes allow you to define reusable “blueprints” for data objects to ensure each object provides the same set of 
fields. Fields stored on classes are mutable, and new fields can be added freely, which you may or may not like.
"""

class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic
class_car1 = Car('red', 3812.4, True)
class_car2 = Car('blue', 40231.0, False)

# collections.namedtuple – Convenient Data Objects
"""
Namedtuple allows you to define reusable “blueprints” for your records that ensure the correct field names are used.
Namedtuples are immutable, just like regular tuples.
"""

from collections import namedtuple

p1 = namedtuple('Point', 'x y z')(1, 2, 3)

# typing.NamedTuple – Improved Namedtuples
"""
It is very similar to namedtuple, the main difference being an updated syntax for defining new record types and 
added support for type hints.
"""
from typing import NamedTuple
class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car1 = Car('red', 3812.4, True)

# struct.Struct – Serialized C Structs
"""
The struct.Struct class23 converts between Python values and C structs serialized into Python bytes objects.
Serialized structs are seldom used to represent data objects meant to be handled purely inside Python code. They’re 
intended primarily as a data exchange format, rather than as a way of holding data in memory that’s only used by 
Python code.
"""

from struct import Struct
MyStruct = Struct('i?f')

data = MyStruct.pack(23, False, 42.0)
print(data)
print(MyStruct.unpack(data))

# types.SimpleNamespace – Fancy Attribute Access
"""
This means SimpleNamespace instances expose all of their keys as class attributes. This means you can use obj.key 
“dotted” attribute access instead of the obj['key'] square-brackets indexing syntax that’s used by regular dicts. All 
instances also include a meaningful __repr__ by default.
"""

from types import SimpleNamespace
car3 = SimpleNamespace(color='red', mileage=3812.4, automatic=True)
print(car3)

"""
You only have a few (2-3) fields: Using a plain tuple object may be okay if the field order is easy to remember or field
names are superfluous. For example, think of an (x, y, z) point in 3D space.
You need immutable fields: In this case, plain tuples, collections.namedtuple, and typing.NamedTuple would all make good
options for implementing this type of data object.
You need to lock down field names to avoid typos: collections.namedtuple and typing.NamedTuple are your friends here.
You want to keep things simple: A plain dictionary object might be a good choice due to the convenient syntax that 
closely resembles JSON.
You need full control over your data structure: It’s time to write a custom class with @property setters and getters.
You need to add behavior (methods) to the object: You should write a custom class, either from scratch or by extending
collections.namedtuple or typing.NamedTuple.
You need to pack data tightly to serialize it to disk or to send it over the network: Time to read up on struct.Struct 
because this is a great use case for it.
"""