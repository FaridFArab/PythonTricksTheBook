"""
There are two kinds of data attributes on Python objects:
class variables and instance variables. Class variables are declared inside the class definition (but outside any
instance methods). They’re not tied to any particular instance of a class. Instead, class variables store their contents
on the class itself, and all objects created from a particular class share access to the same set of class variables.
This means, for example, that modifying a class variable affects all object instances at the same time. Instance
variables are always tied to a particular object instance. Their contents are not stored on the class, but on each
individual object created from the class. Therefore, the contents of an instance variable are completely independent of
one object instance to the next. And so, modifying an instance variable only affects one object instance at a time.
"""

class Dog:
    num_legs = 4 # <- Class variable
    def __init__(self, name):
        self.name = name # <- Instance variable
"""
If you try to access an instance variable through the class, it’ll fail with an AttributeError.
Modifying a class variable on the class namespace affects all instances of the class.
"""

jack = Dog('Jack')
jill = Dog('Jill')

Dog.num_legs = 6
print(jack.num_legs, jill.num_legs, Dog.num_legs)

class CountedObject:
    num_instances = 0
    def __init__(self):
        self.__class__.num_instances += 1


print(CountedObject.num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject.num_instances)