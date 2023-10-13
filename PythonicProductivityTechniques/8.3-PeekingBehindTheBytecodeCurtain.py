"""
The bytecode resulting from this compilation step is cached on disk in .pyc and .pyo files so that executing the same
Python file is faster the second time around.
"""

def greet(name):
    return 'Hello, ' + name + '!'

"""
Each function has a __code__ attribute (in Python 3) that we can use to get at the virtual machine instructions, 
constants, and variables used by our greet function.
"""

print(greet.__code__.co_code)
print(greet.__code__.co_consts)
print(greet.__code__.co_varnames)

"""
You can see co_consts contains parts of the greeting string our function assembles. Constants and code are kept separate
to save memory space. Constants are, well, constant—meaning they can never be modified and are used interchangeably in 
multiple places. So instead of repeating the actual constant values in the co_code instruction stream, Python stores 
constants separately in a lookup table. The instruction stream can then refer to a constant with an index into the 
lookup table. The same is true for variables stored in the co_varnames field.

"""

"""
Disassembler to make inspecting the bytecode easier.Python’s bytecode disassembler lives in the dis module that’s part 
of the standard library. So we can just import it and call dis.dis() on our greet function to get a slightly 
easier-to-read representation of its bytecode.
"""
import dis
dis.dis(greet)

"""
The stack is the data structure used as internal working storage for the virtual machine. There are different classes 
of virtual machines and one of them is called a stack machine. CPython’s virtual machine is an implementation of such a 
stack machine. If the whole thing is named after the stack, you can imagine what a central role this data structure 
plays.
"""