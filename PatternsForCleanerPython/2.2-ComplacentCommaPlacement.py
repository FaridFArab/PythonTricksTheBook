"""
Smart formatting and comma placement can make your list, dict, or set constants easier to maintain.
Python’s string literal concatenation feature can work to your benefit, or introduce hard-to-catch bugs.
"""

names_wrong = ['Alice', 'Bob', 'Dilbert']

names_correct = ['Alice',
                 'Bob',
                 'Dilbert',
                 ]

new_names = ['Alice',
             'Bob',
             'Dilbert'
             'Jane']
"""
new_names output ==> ['Alice', 'Bob', 'DilbertJane']
"""