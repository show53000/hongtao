#!/usr/bin/env python 
#!coding = UTF-8
# Author = show530


class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self._job = 'Student'
p = Person('Bob')
print (p.name)    # => Bob
print (p._title)  # => Mr
print (p._job)

