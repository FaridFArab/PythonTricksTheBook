def yell(text: str):
    return text.upper() + '!'


"""
Functions Are Objects
"""
print(yell('hello'))
bark = yell
print(bark('woof'))

del yell
print(bark('woof'))
print(bark, ', ', bark.__name__)
# print(yell) --> NameError: name 'yell' is not defined

"""
Functions Can Be Stored in Data Structures
"""
funcs = [bark, str.lower, str.capitalize]
for f in funcs:
    print(f, f('hey there'))

"""
Functions Can Be Passed to Other Functions
"""


def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


greet(bark)


def whisper(text):
    return text.lower() + '...'


greet(whisper)

"""
Functions Can Be Nested
"""


def speak(text):
    def whisper(t):
        return t.lower() + '...'

    return whisper(text)


speak('Hello World')

"""
Not only can functions accept behaviors through arguments but they can also return behaviors. How
"""


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


"""
Not only can functions return other functions, these inner functions can also capture and carry some of the 
parent function’s state with them.
In this example, make_adder serves as a factory to create and configure “adder” functions. 
Notice how the “adder” functions can still access the n argument of the make_adder function (the enclosing scope).
"""


def make_adder(n):
    def add(x):
        return x + n

    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)
plus_3(4)  # --> 7
plus_5(4)  # --> 9

"""
Objects Can Behave Like Functions.
In below sample, “calling” an object instance as a function attempts to execute the object’s __call__ method.
"""


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x
