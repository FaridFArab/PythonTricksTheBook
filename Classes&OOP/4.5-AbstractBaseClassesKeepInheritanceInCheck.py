"""
Abstract Base Classes (ABCs) ensure that derived classes implement particular methods from the base class.
• instantiating the base class is impossible; and
• forgetting to implement interface methods in one of the subclasses raises an error as early as possible
"""

from abc import ABCMeta, abstractmethod
class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass
class Concrete(Base):
    def foo(self):
        pass

assert issubclass(Concrete, Base)


c = Concrete() # TypeError: Can't instantiate abstract class Concrete with abstract method bar

"""
• Abstract Base Classes (ABCs) ensure that derived classes implement particular methods from the base class 
at instantiation time.
• Using ABCs can help avoid bugs and make class hierarchies easier to maintain.
"""