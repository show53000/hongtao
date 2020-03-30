#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

username = 'hongtao'
password = '123456'

for i in range(3):
    input_user = str(input("Please enter your name:  "))
    input_pass = str(input("Please enter your password:  "))
    if input_user == username and input_pass == password:
        print("\033[7;37;42m==============================")
        print("Welcome,Login succeeded!!")
        print("==============================\033[7;37;42m")
        print('\033[0m')
        break
    else:
        print("\033[7;31m==============================")
        print(" Incorrect username or password!!")
        print("==============================")
        print("You have "+str(2-i)+ " more chances!!")
        print("==============================\033[1;37;40m")
        print('\033[0m')
else:
    print("\033[7;31m==============================")
    print("Too many incorrect username or password for account !!")
    print("Prohibit further operations!")
    print("==============================\033[1;31;40m")
    print('\033[0m')
