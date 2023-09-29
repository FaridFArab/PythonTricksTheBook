# Objects that support the __iter__ and __next__ dunder methods automatically work with for-in loops.


class RepeaterIterator:
    def __init__(self, source):
        self.source = source #5
    def __next__(self):
        return self.source.value #7

class Repeater:
    def __init__(self, value):
        self.value = value #2
    def __iter__(self):
        return RepeaterIterator(self) #4


if __name__ == '__main__':
    repeater = Repeater('Hello') #1
    for item in repeater: #3
        print(item) #6