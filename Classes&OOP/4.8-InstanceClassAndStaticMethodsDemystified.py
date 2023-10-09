import math


class MyClass:
    def method(self):
        return 'instance method called', self
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'


# Instance Methods
"""
Not only can they modify object state, instance methods can also access the class itself through the self.__class__ 
attribute. This means instance methods can also modify class state.
"""

# Class Methods
"""
Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the 
object instance—when the method is called. Class methods can still modify class state that applies across all
instances of the class.
"""

# Static Methods
"""
Static methods can neither access the object instance state nor the class state. They work like regular functions but
belong to the class’ (and every instance’s) namespace.
A nice and clean way to do that is by using class methods as factory functions for the different kinds.
"""
class Pizza:
    def __init__(self, ingredients, radius: int = 2):
        self.ingredients = ingredients
        self.radius = radius
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

print(Pizza.margherita())
print(Pizza.prosciutto())
"""
We can use the factory functions to create new Pizza objects that are configured just the way we want them. They all use
the same __init__ constructor internally and simply provide a shortcut for remembering all of the various ingredients.
"""

p = Pizza(['mozzarella', 'tomatoes'], 4)
print(p.area())
"""
Static methods can’t access class or instance state because they don’t take a cls or self argument. That’s a big 
limitation— but it’s also a great signal to show that a particular method is independent from everything else around it.
"""