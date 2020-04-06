#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

class User(object):
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print(full_name + " is " + str(
            user_one.age) + " years old,and he's phone number is " + user_one.phone_number + ".")

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello," + full_name + " !")


class Admin(User):
    def __init__(self, first_name, last_name, age, phone_number):
        super().__init__(first_name, last_name, age, phone_number)
        self.privileges = Priviliges()


class Priviliges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("The power of admin are:")
        for privilege in self.privileges:
            print(privilege)


# user_one = User('Jackson', 'Yee', 18, '1234567890')
# user_one.describe_user()
# user_one.greet_user()

admin = Admin('Jackson', 'Yee', 18, '1234567890')
admin.privileges.show_privileges()
