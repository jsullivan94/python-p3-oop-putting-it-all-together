#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, val):
        if isinstance(val, int):
            self._size = val
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")
