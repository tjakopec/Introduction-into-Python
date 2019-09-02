#
# IF
#
x = 2 

if x == 2:
    print("number is 2")

#if works with bool (boolean) data type
check = x == 2
print(type(check))

if check:
    print("Number is  2")
 

x="2"

if x==2:
    print('Number is  "2"')
else:
    print('Number is not "2"')

# Python tos not have &, only &&
def a():
    print("Check AAAAAA")
    return False

def b():
    print("Check BBBBBB")
    return True

if a() and b():
    print("OK")


# if in
lista = (1,2,2,3,4,2,3,2)
x = 4
if x in lista:
    print("in")


#
# ELIF
#

#no swith
    #only elif

x=5;

if x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
elif x==4:
    print("Four")
elif x==5:
    print("Five")
else:
    print("Not a grade")
    
#inline if

x=2

print("Super" if x==5 else "Not so good")



#
# LOOPS
#


# for
#iterating 0 to 9 for 1
for i in range(10):
    print(i, end = " ")
print()
#iterating 0 to 9 for 1
for i in range(0,10):
    print(i, end = " ")
print()
#iterating 0 to 9 for 2
for i in range(0,10,2):
    print(i, end = " ")
print()
#iterating 10 to 1 for 1
for i in range(10,0,-1):
    print(i, end = " ")
print()

#iterating 10 to 0 for 1
for i in range(10,-1,-1):
    print(i, end = " ")
print()

#force loop continue
for i in range(10):
    if i==2:
        continue
    print(i, end = " ")
print()
#force loop break
for i in range(10):
    if i==2:
        break
    print(i, end = " ")
print()

#while
# works with bool (boolean) data type
#infinit loop
#while True:
#    print("Hello")
i=0
while i<10:
    print(i, end = " ")
    i+=1
print()

# continue and break works the same in while


#
# loop nesting
#

"""
from random import *
while True:
    for i in range(randrange(1,100)):
        if i==1:
            print("Marija, I like you!", end=" ")
        print(random(), end=" ")
"""

#iterating data structures

data_type=[7,7.5,7+2j, "String", bool(1)]
for e in data_type:
    print(e)

data_type=(7,7.5,7+2j, "String", bool(1))

for e in data_type:
    print(e)

data_type={1,7,7,5,5,5,2,2,2,2}

for e in data_type:
    print(e)


x="ESSIS"
for e in x: print(e, end=" ❤ ") #http://graphemica.com/unicode/characters
