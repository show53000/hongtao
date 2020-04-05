#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names):
    for i in range(len(great_names)):
        great_names[i]='The great '+great_names[i]
    return great_names

magicians_names = ['hong tao','xiao weihong','hong yumi','hong yuchan']

great_names=magicians_names[:]

make_great(great_names)

show_magicians(magicians_names)

show_magicians(great_names)


