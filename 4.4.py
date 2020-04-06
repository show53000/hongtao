#！/usr/bin/nev python
#-*-coding:utf-8 -*-
# Author:show530

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This cara has "+str(self.odometer_reading)+" miles on it.")
    def update_odimter(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size<85:
            self.battery_size = 85
        return self.battery_size

    def discrib_battery(self):
        print("This car has " + str(self.battery_size)+"-kWh battery.")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()



my_tesla = ElectricCar('tesla','model S',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.upgrade_battery()
my_tesla.battery.discrib_battery()

