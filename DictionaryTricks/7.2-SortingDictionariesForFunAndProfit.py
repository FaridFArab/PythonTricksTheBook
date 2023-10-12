xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
"""
To get a sorted list of the key/value pairs in this dictionary, you could use the dictionary’s items() method and then 
sort the resulting sequence in a second pass.
"""
print(sorted(xs.items()))
"""
You can control the ordering by passing a key func to sorted() that will change how dictionary items are compared.
A key func is simply a normal Python function to be called on each element prior to making comparisons. The key func 
gets a dictionary item as its input and returns the desired “key” for the sort order comparisons.
You wanted to get a sorted representation of a dictionary based on its values. To get this result you could use the 
following key func which returns the value of each key/value pair by looking up the second element in the tuple.
"""
print(sorted(xs.items(), key=lambda x: x[1]))
"""
The concept is so common that Python’s standard library includes the operator module. This module implements some of the
most frequently used key funcs as plug-and-play building blocks, like operator.itemgetter and operator.attrgetter.
"""
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
"""
Using the operator module might communicate your code’s intent more clearly in some cases. On the other hand, using a 
simple lambda expression might be just as readable and more explicit. In this particular case, I actually prefer the 
lambda expression.
If you need to reverse the sort order so that larger values go first, you can use the reverse=True keyword argument when
calling sorted()
"""
print(sorted(xs.items(), key=lambda x: x[1], reverse=True)
)