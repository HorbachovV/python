# Variable

name = 'Vova'
age = 32

# Expressions and statements

1 + 1
'Hello'
print(name)

# Comments

# this is comment

# Data types

my_name = 'Vova' # string  print(type(my_name))
age = 33 # integer
my_age = 33.11 # float

num = int('20') #integer


# complex for complex number
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictonaries
# set for sets

# Operators

1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
2 // 2 #2

new_num = 32
new_num += 1 # new_num = new_num + 1 

a = 1
b = 2

a == b # false
a != b # true
a > b #false
a <= b #true

condition1 = True
condition2 = False

not condition1 # false
condition1 and condition2 # false
condition1 or condition2 # true

print(0 or 1) #1
print(False or 'hey') #'hey'
print('hi' or 'hey') #'hi'
print([] or False) #false
print(False or []) #[]


def is_adult(age):
    if age > 18:
        return True
    else:
        return False

def is_adult2(age):
    return True if age > 18 else False

# Strings 

print('vova'.upper())
print('VOVA'.lower())
print('vova'.title())
print(len('vova'))

name_2 = 'Vova'
print(name_2[0]) #V
print(name_2[-1]) #a
print(name_2[1:2]) #o start index one ends before index two

# number

num = complex(2, 3)
print(num.real, num.imag) # 2.0 3.0

print(abs(-5.5)) # 5.5
print(round(5.51)) # 6
print(round(5.51, 1)) # 5.5


from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State['ACTIVE']) # State.ACTIVE
print(State['ACTIVE'].value) # 1

# user input

def your_age():
    your_age = input('What is your age: ')
    print(f'Your age is {your_age}')

your_age()

# lists

dogs = ['Roger', 'Jack']
dogs[1] = 'Rex'
print('Roger' in dogs) # true
print(dogs[1]) 
print(dogs)
dogs.append('Buu')
print(dogs)

items = ['Roger', 'Jack', 'Lucky', 'Joe']
items.insert(2, 'test')
items.sort()
print(items)

# tuples

names = ('Roger', 'Syd')
print(names[0]) # Roger
print(names.index('Roger')) #0 index

# dictionary

cat = {'name': 'Roger', 'color': 'brown', 'age': 3}
cat['name'] = 'Garfield'
print(cat['name'])
print(cat.values())
print(cat.keys())

# sets 

set1 = {'Smith', 'Black'}
set2 = {'Luna'}
mod = set1 | set2
print(mod)
# intersect = set1 & set2 # 'Smith'
# print(intersect)
