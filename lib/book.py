#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, val):
        if isinstance(val, str):
            self._title = val


    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, val):
        if isinstance(val, int):
            self._page_count = val
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        