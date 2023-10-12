# values = [expression for item in collection]
squares = [x * x for x in range(10)]

# values = [expression for item in collection if condition]
even_squares = [x * x for x in range(10) if x % 2 == 0]
# The modulo (%) operator used here returns the remainder after division of one number by another.

"""
As you get more proficient at using them, it becomes easier and easier to write code that’s difficult to read. If you’re
not careful, you might have to deal with monstrous list, set, and dict comprehensions soon. Remember, too much of a good
thing is usually a bad thing.
"""