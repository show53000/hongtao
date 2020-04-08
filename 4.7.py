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


filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ' '
for line in lines:
    line.rstrip() += pi_string



    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

