#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530


# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print("The restaurant is  "+ str(self.restaurant_name))
#         print("The restaurant offers the following dishes : "+str(self.cuisine_type))
#
#     def open_restaurant(self):
#         print("The restaurant is open")
#
# restaurant=Restaurant('BeiJing Restaurant','Kung Pao Chicken')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#
#     def describe_user(self):
#         print("The first name is "+self.first_name.title())
#         print("The last name is "+self.last_name.title())
#
#     def greet_user(self):
#         print("Hello,"+self.first_name.title()+self.last_name)
#
# user = User('hong','tao')
# user.describe_user()
# user.greet_user()

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles



my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(25000)
my_used_car.read_odometer()
my_used_car.increment_odometer(5000)
my_used_car.read_odometer()


# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(46)
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(12)
# my_new_car.read_odometer()




