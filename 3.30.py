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

# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.login_attempts = 5
#
#     def describe_user(self):
#         print("The first name is "+self.first_name.title())
#         print("The last name is "+self.last_name.title())
#
#     def greet_user(self):
#         print("Hello,"+self.first_name.title()+self.last_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         print('Total '+str(self.login_attempts)+' logins')
#         return self.login_attempts
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print('Number of logins is clear!'+'Total '+str(self.login_attempts)+' logins')
#         return self.login_attempts
#
#
# user = User('hong','tao')
# user.describe_user()
# user.greet_user()
#
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.reset_login_attempts()
