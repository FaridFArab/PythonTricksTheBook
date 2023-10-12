lst = [1, 2, 3, 4, 5]
print( lst[1:3:1])
# To avoid off-by-one errors, it’s important to remember that the upper bound is always exclusive.
# You can do other interesting things with the step parameter, also called the stride.
# I like to call “:” the sushi operator. It looks like a delicious maki roll cut in half.
print(lst[::-1])
# I’d still stick with list.reverse() and the built-in reversed() function to reverse a list.

del lst[:]
print(lst)
"""
In Python 3 you can also use lst.clear() for the same job, which might be the more readable pattern, depending on
the circumstances.
Creating a shallow copy means that only the structure of the elements is copied, not the elements themselves. Both 
copies of the list share the same instances of the individual elements. If you need to duplicate everything, including 
the elements, then you’ll need to create a deep copy of the list. Python’s built-in copy module will come in handy 
for this.
"""
