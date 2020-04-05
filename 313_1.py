#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

def make_pizza(size,*toppings):
    print('\nMaking a'+str(size)+"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- "+topping)

make_pizza(16,'pepperoni')
make_pizza(18,'mushrooms','green peppers','extra cheese')
