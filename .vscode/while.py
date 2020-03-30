#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

hongtao_age = 38
i=0
while i<5:
    guess_age = int(input("Please guess the hongtao's age:  "))
    if guess_age == hongtao_age:
        print("================")
        print("Yes!you get it!!Good Bye!!")
        print("================")
        break
    elif guess_age < hongtao_age:
        print("You need guess more.....")
    else:
        print("less you guess..........")
    i=i+1
else:
    print("====================================")
    print("You guess too much time!!  Fuck off !!")
    print("====================================")
