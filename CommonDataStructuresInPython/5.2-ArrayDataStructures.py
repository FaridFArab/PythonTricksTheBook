"""
Arrays consist of fixed-size data records that allow each element to be efficiently located based on its index.
Because arrays store information in adjoining blocks of memory, they’re considered contiguous data structures (as
opposed to linked datas structure like linked lists, for example.)
Performance-wise, it’s very fast to look up an element contained in an array given the element’s index. A proper array
implementation guarantees a constant O(1) access time for this case.
"""

# list – Mutable Dynamic Arrays
"""
Python’s lists are implemented as dynamic arrays.
"""
arr = ['one', 'two', 'three']

# tuple – Immutable Containers
"""
Python’s tuple objects are immutable.
"""
arr_tuple = 'one', 'two', 'three'

# array.array – Basic Typed Arrays
"""
Python’s array module provides space-efficient storage of basic Cstyle data types like bytes, 32-bit integers, 
floating point numbers, and so on.
Arrays created with the array.array class are mutable and behave similarly to lists, except for one important 
difference—they are “typed arrays” constrained to a single data type.
"""

import array
arr_array = array.array('f', (1.0, 1.5, 2.0, 2.5))


# str – Immutable Arrays of Unicode Characters
"""
str is an immutable array of characters. Oddly enough, it’s also a recursive data structure—each character in a 
string is a str object of length 1 itself. String objects are space-efficient because they’re tightly packed and
they specialize in a single data type. Strings are immutable in Python, modifying a string requires creating a 
modified copy.
"""
arr_str = 'abcd'

# bytes – Immutable Arrays of Single Bytes
"""
Bytes objects are immutable sequences of single bytes (integers in the range of 0 <= x <= 255). You can also think of 
them as immutable arrays of bytes. Like strings, bytes have their own literal syntax for creating objects and they’re 
space-efficient. Bytes objects are immutable, but unlike strings, there’s a dedicated “mutable byte array” data type 
called bytearray that they can be unpacked into.
"""
arr_bytes = bytes((0, 1, 2, 3))


# bytearray – Mutable Arrays of Single Bytes
"""
The bytearray type is a mutable sequence of integers in the range 0 <= x <= 255.13 They’re closely related to bytes 
objects with the main difference being that bytearrays can be modified freely—you can overwrite elements, remove 
existing elements, or add new ones. The bytearray object will grow and shrink accordingly. Bytearrays can be converted 
back into immutable bytes objects but this involves copying the stored data in full—a slow operation taking O(n) time.
"""
arr_bytearray = bytearray((0, 1, 2, 3))


"""
NumPy offer a wide range of fast array implementations for scientific computing and data science.
You need to store arbitrary objects, potentially with mixed data types? Use a list or a tuple, depending on whether you 
want an immutable data structure or not.
You have numeric (integer or floating point) data and tight packing and performance is important? Try out array.array
and see if it does everything you need. Also, consider going beyond the standard library and try out packages like 
NumPy or Pandas.
You have textual data represented as Unicode characters? Use Python’s built-in str. If you need a “mutable string,” 
use a list of characters.
You want to store a contiguous block of bytes? Use the immutable bytes type, or bytearray if you need a mutable 
data structure.
In most cases, I like to start out with a simple list. I’ll only specialize later on if performance or storage space 
becomes an issue. Most of the time, using a general-purpose array data structure like list gives you the fastest 
development speed and the most programming convenience.
"""