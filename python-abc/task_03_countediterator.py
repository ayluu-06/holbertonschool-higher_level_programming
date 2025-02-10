#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        save = next(self.iterable, None)
        if save is None:
            raise StopIteration
        self.count += 1
        return save
