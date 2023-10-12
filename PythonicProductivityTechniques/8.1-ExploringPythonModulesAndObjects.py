"""
Consulting a search engine or looking up the official Python documentation on the web would be one way to do it. But
Python’s builtin dir() function lets you access this information directly from the Python REPL.
"""
import datetime
print(dir(datetime))
"""
Calling dir() on a module gives you an alphabetized list of the names and attributes the module provides.
"""

# you can use to filter down the list of attributes to just the ones you’re interested in
print( [_ for _ in dir(datetime) if 'date' in _.lower()])

"""
Python’s built-in help() function will come to your rescue. With it, you can invoke Python’s interactive help system to 
browse the auto generated documentation for any Python object.
"""
help(datetime)
"""
You can use the cursor up and down keys to scroll through the documentation. Alternatively you can also hit the space 
bar to scroll down a few lines at once. To leave this interactive help mode you’ll need to press the q key. This will 
take you back to the interpreter prompt.
"""
