import json
mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(mapping)

"""
You can use json.dumps() to pretty print Python dicts with nicer formatting.
"""

print(json.dumps(mapping, indent=4, sort_keys=True))


"""
While this looks nice and readable, it isn’t a perfect solution. Printing dictionaries with the json module only 
works with dicts that contain primitive types—you’ll run into trouble trying to print a dictionary that contains a 
non-primitive data type, like a function
"""

# print(json.dumps({all:"yup"})) --> TypeError: keys must be str, int, float, bool or None, not builtin_function_or_method
# mapping['d'] = {1, 2, 3} # >>> json.dumps(mapping) --> TypeError: "set([1, 2, 3]) is not JSON serializable"


"""
The classical solution to pretty-printing objects in Python is the builtin pprint module.
Compared to json.dumps(), it doesn't represent nested structures as well visually
"""
import pprint

mapping['d'] = {1, 2, 3}
pprint.pprint(mapping)