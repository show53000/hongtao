#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 2

    def describe_restaurant(self):
        print("The restaurant is  "+ str(self.restaurant_name))
        print("The restaurant offers the following dishes : "+str(self.cuisine_type))

    def open_restaurant(self):
        print("The restaurant is open")

    def number_served_restaurant(self):
        print('There are '+str(self.number_served)+' serveds in the rastaurant')

    def update_number_served(self,number_served):
        if number_served>=0:
            self.update_number_served = number_served
            self.number_served += self.update_number_served
            print('There are '+str(self.number_served)+' serveds in the rastaurant')
            print('There have increased ' + str(self.update_number_served) + ' serveds in this day')
            return self.number_served
        else:
            print("Input error")

restaurant=Restaurant('BeiJing Restaurant','Kung Pao Chicken')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served_restaurant()

restaurant.update_number_served(5)

