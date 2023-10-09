"""
Dictionaries are also often called maps, hashmaps, lookup tables, or associative arrays.
"""
# dict – Your Go-To Dictionary

phonebook = {
'bob': 7387,
'alice': 3719,
'jack': 7052,
}
squares = {x: x * x for x in range(6)}
"""
Python’s dictionaries are indexed by keys that can be of any hashable type : A hashable object has a hash value which 
never changes during its lifetime (see __hash__), and it can be compared to other objects (see __eq__). 
In addition, hashable objects which compare as equal must have the same hash value.
Python dictionaries are based on a well-tested and finely tuned hash table implementation that provides the performance 
characteristics you’d expect: O(1) time complexity for lookup, insert, update, and delete operations in the average case.
"""

# collections.OrderedDict – Remember the Insertion Order of Keys
"""
If key order is important for your algorithm to work, it’s best to communicate this clearly by explicitly using the 
OrderDict class.
"""

import collections
d = collections.OrderedDict(one=1, two=2, three=3)
print(d)
d['four'] = 4
print(d)
print(d.keys())

# collections.defaultdict – Return Default Values for Missing Keys
"""
The defaultdict class is another dictionary subclass that accepts a callable in its constructor whose return value will 
be used if a requested key cannot be found.
"""

dd = collections.defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
print(dd['dogs'])

# collections.ChainMap – Search Multiple Dictionaries as a Single Mapping
"""
The collections.ChainMap data structure groups multiple dictionaries into a single mapping Lookups search the 
underlying mappings one by one until a key is found. Insertions, updates, and deletions only affect the first mapping 
added to the chain.
"""

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = collections.ChainMap(dict1, dict2)
print(chain)

# types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries
"""
MappingProxyType is a wrapper around a standard dictionary that provides a read-only view into the wrapped 
dictionary’s data and it can be used to create immutable proxy versions of dictionaries. This can be helpful if you’d 
like to return a dictionary carrying internal state from a class or module, while discouraging write access to this 
object. Using MappingProxyType allows you to put these restrictions in place without first having to create a full copy 
of the dictionary.
"""
from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
#  read_only['one'] = 23 #  TypeError: # "'mappingproxy' object does not support item assignment"