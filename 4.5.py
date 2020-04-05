#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def discrib_restaurant(self):
        print("The restaurant is  " + str(self.restaurant_name))
        print("The restaurant offers the following dishes : "+str(self.cuisine_type))

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['Strawberry','chocolate','cocoa','cream','orange']

    def discrib_icecream(self):
        for flavor in self.flavors:
            print("Here are these ice cream: "+flavor)

my_icecream = IceCreamStand('BeiJing Icecream','Icecream')
my_icecream.discrib_icecream()
my_icecream.discrib_restaurant()

