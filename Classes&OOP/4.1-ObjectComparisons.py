"""
Difference in meaning between equal and identical. And this difference is crucial to understanding how
Python’s is and == comparison operators behave.
The == operator compares by checking for equality.
The is operator, however, compares identities.
"""

a = [1, 2, 3]
b = a

print(a is b, a == b)

c = list(a)
print(c)
print(a is c, a == c)
print(id(a), id(b), id(c))

"""
c and a are pointing to two different objects, even though their contents might be the same.
• An is expression evaluates to True if two variables point to the same (identical) object.
• An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents).
"""