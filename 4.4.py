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

class ElectricCar(Car):
    def _init_(self,make,model,year):
        super.__init__(make,model,year)

my_tesla = ElectricCar('tesla','model S',2016)
print(my_tesla.get_descriptive_name())

