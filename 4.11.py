#!/usr/bin/env python 
#!coding = UTF-8
# Author = show530

filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    # message_string = ''
    for line in lines:
       print(line.rstrip().replace('Python','C'))
