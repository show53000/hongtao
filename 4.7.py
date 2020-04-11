#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ' '
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# print(len(pi_string))

#frist
filename = 'learning_python.txt'
with open(filename) as file_object:
    print(file_object.read())
# #second
with open(filename) as file_object:
    lines = file_object.readlines()
learning_string =''
for line in lines:
    learning_string += line.strip()+' '
print(learning_string)
print(len(learning_string))
#third
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
