#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 5

    def describe_user(self):
        print("The first name is "+self.first_name.title())
        print("The last name is "+self.last_name.title())

    def greet_user(self):
        print("Hello,"+self.first_name.title()+self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print('Total '+str(self.login_attempts)+' logins')
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        print('Number of logins is clear!'+'Total '+str(self.login_attempts)+' logins')
        return self.login_attempts

class Privileges():
    def __init__(self,privileges):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Admin permission : ")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges(Admin)



my_admin = Admin('hong','tao')
my_admin.privileges.show_privileges()


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
