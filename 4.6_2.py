#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530


# from car import Car
#
# my_new_car = Car('audi','a6',2018)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()



# my_tesla = ElectricCar('tesla','model S',2018)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.discrib_battery()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.discrib_battery()
#
# my_new_car = Car('audi','a6',2018)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


# import car
# my_beetle = car.Car('volkswagen','bettle',2018)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla','roadster',2018)
# print(my_tesla.get_descriptive_name())


from random import randint
# x = randint(1,6)
# print(x)
class Die():
    def __init__(self,roll_number):
        self.roll_number = randint(1,6)

    def roll_die(self):
        print('The number is : '+ str(self.roll_number))

my_die = Die(10)
my_die.roll_die()

