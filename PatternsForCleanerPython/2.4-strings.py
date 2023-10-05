"""
• Single Leading Underscore: _var
• Single Trailing Underscore: var_
• Double Leading Underscore: __var
• Double Leading and Trailing Underscore: __var__
• Single Underscore: _
"""

# Single Leading Underscore: “_var”


"""
The underscore prefix is meant as a hint to tell another programmer
that a variable or method starting with a single underscore is intended
for internal use. This convention is defined in PEP 8, the most commonly used Python code style guide.8
"""

class Test:
    def __init__(self):
        """
        the leading single underscore in _bar did not prevent us from “reaching into”
        the class and accessing the value of that variable.
        """
        self.foo = 11
        self._bar = 12 # Hey, this isn’t really meant to be a part of the public interface of this class. Best to leave it alone.

    @property
    def bar(self):
        return self._bar

    def external_func(self):
        return 2

    def _internal_function(self):
        """
        protected member function
        :return:
        """
        return 3


x = Test()
print(x.foo)
print(x.bar)
print(x._bar)
print(x.external_func())
print(x._internal_function())

"""
Single underscores are a Python naming convention that indicates a name is meant for internal use.
if you use a wildcard import to import all the names from the module, Python will not import names with a 
leading underscore (unless the module defines an __all__ list that overrides this behavior).
PEP 8 recommendation that wildcard imports should be avoided.
"""


# Single Trailing Underscore: “var_”

"""
In summary, a single trailing underscore (postfix) is used by convention to avoid naming conflicts with 
Python keywords. This convention is defined and explained in PEP 8. The most fitting name for a variable 
is already taken by a keyword in the Python language.
"""

def make_object(name, class_):
    pass


# Double Leading Underscore: “__var”


class Test:
    def __init__(self):
        """
        The leading underscore is just a convention in this case—a hint for the programmer. It does this to protect
        the variable from getting overridden in subclasses.
        """
        self.foo = 11
        self._bar = 22
        self.__baz = 33


# t = Test()
# print(dir(t))

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overriden'
        self._bar = 'overriden'
        self.__baz = 'overriden'

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
print(t2.__baz) # AttributeError: 'ExtendedTest' object has no attribute '__baz'. Did you mean: '_bar'?
print(t2._Test__baz)



# Double Leading and Trailing Underscore: “__var__”
"""
However, names that have both leading and trailing double underscores are reserved for special use in the language. 
This rule covers things like __init__ for object constructors, or __call__ to make objects callable.
These dunder methods are often referred to as magic methods
"""


# Single Underscore: “_”
"""
You can also use single underscores in unpacking expressions as a “don’t care” variable
Besides its use as a temporary variable, “_” is a special variable in most Python REPLs that represents the result of 
the last expression evaluated by the interpreter.
"""
for _ in range(10):
    print("Hello World")


# Summary
"""
• Single Leading Underscore “_var”: Naming convention indicating a name is meant for internal use. 
Generally not enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.
• Single Trailing Underscore “var_”: Used by convention to avoid naming conflicts with Python keywords.
• Double Leading Underscore “__var”: Triggers name mangling when used in a class context. Enforced by the Python interpreter.
• Double Leading and Trailing Underscore “__var__”: Indicates special methods defined by the Python language. 
Avoid this naming scheme for your own attributes.
• Single Underscore “_”: Sometimes used as a name for temporary or insignificant variables (“don’t care”). 
Also, it represents the result of the last expression in a Python REPL session.
"""
