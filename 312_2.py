#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

'''def send_invitation(exports,informed):
    while exports:
        export=exports.pop()
        print(export+" 您好，现在邀请您参加会议....")
        informed.append(export)

def print_invitation(exports,informed):
    print('执行前：experts= '+str(exports)+' ,informed= '+str(informed))
    send_invitation(exports[:],informed)
    print('执行后：experts= '+str(exports)+' ,informed= '+str(informed))


exports=['洪韬','肖伟宏','洪语禅','洪语谧']
informed = []

print_invitation(exports,informed)
'''

def show_magicians(names):
    for name in names:
        print(name.title())


def make_great(names):
    for i in range(len(names)):
        names[i]="The great "+names[i].title()
    return names

def contrast(names):
    print('Before execution :'+str(magicians_names))
    make_great(magicians_names[:])
    print('After execution :' + str(magicians_names))

def contrast2(names):
    print('Before execution :'+str(magicians_names))
    make_great(magicians_names)
    print('After execution :' + str(magicians_names))

magicians_names = ['hong tao','xiao weihong','hong yumi','hong yuchan']

contrast(magicians_names)

contrast2(magicians_names)

