#!/usr/bin/env python 
#!coding = UTF-8
# Author = show530

file_name = 'learning_python.txt'
with open(file_name) as file_object:
    lines = file_object.readline()
    message = ''
for line in lines:
    message += line.strip()+' '
message.replace('python','C')
print(message)



