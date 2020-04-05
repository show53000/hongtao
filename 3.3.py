#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

"""
def make_shirt(Clothing_size,describe_shirt='I LOVE PYTHON'):
    print("This shirt is "+Clothing_size.title()+" ,"+"There is text '"+describe_shirt+"' printed on the shirt !")

make_shirt(Clothing_size='Large')
make_shirt(Clothing_size='Medium')


def describe_cite(city_name,country='china'):
    print(city_name.title()+" is in "+country.title())
describe_cite(city_name='beijing',country='china')
describe_cite(city_name='tokoy',country='japan')
describe_cite(city_name='moscow',country='russia')

def function(x,y):
    z=x+y
    return z
print(function(2,3))


def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' +last_name
    return full_name.title()
musician = get_formatted_name('hong','tao')

print(musician)

musician = get_formatted_name('hong','yu','chan')
print(musician)



def greet_users(names):
    for name in names:
        msg="hello,"+name.title()+"!"
        print(msg)
usernames=['hongtao','hongyuchan','hongyumi','xiaoweihong']
greet_users(usernames)

"""

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
comleted_modes = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    comleted_modes.append(current_design)

print("\nThe following models have been printed: ")
for comleted_mode in comleted_modes:
    print(comleted_mode)


