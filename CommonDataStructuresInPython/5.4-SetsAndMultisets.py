# 5.4 Sets and Multisets
"""
A set is an unordered collection of objects that does not allow duplicate elements. Typically, sets are used to quickly
test a value for membership in the set, to insert or delete new values from a set, and to compute the union or
intersection of two sets.
"""

# set – Your Go-To Set
"""
The set type is mutable and allows for the dynamic insertion and deletion of elements.
"""
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set('alice')
print(letters.intersection(vowels))


# frozenset – Immutable Sets
"""
The frozenset class implements an immutable version of set that cannot be changed after it has been constructed.
Because frozensets are static and hashable, they can be used as dictionary keys or as elements of another set, 
something that isn’t possible with regular (mutable) set objects.
"""
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})

# collections.Counter – Multisets
"""
The collections.Counter class in the Python standard library implements a multiset (or bag) type that allows elements 
in the set to have more than one occurrence.
"""
from collections import Counter
inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)
more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
print(inventory)