my_items = ['a', 'b', 'c']
i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

print(list(range(len(my_items))))

"""
It’s possible to write loops that keep a running index while avoiding the range(len(...)) pattern I cautioned against. 
The enumerate() built-in helps you make those kinds of loops nice and Pythonic:
"""
for i, item in enumerate(my_items):
    print(f'{i}: {item}')

"""
The range() function comes to our rescue again—it accepts optional parameters to control the start value for the loop 
(a), the stop value (n), and the step size (s). 
"""