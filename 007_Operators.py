
# arithmetic operators + - * / % // **

# the is no ++ --

x=3.8 + 2
print(x)


x=9-3
print(x)

x=3.8 * 2.737363635
print(x)

x=1/3
print(x)

x = 3 % 2
print(x)

x= 1 // 3
print(x)

x= 9 // 2
print(x)

x = 2 ** 3
print(x)


#
# comparison operators == < > <= => !=
#

x = 2 # assigning value

if x == 2: print("equals") #equals
if x > 2: print("greater than") # other:  >=  <=

if not(x > 2): print("less")

x = 3
if x != 2: print("not equals")



#
# logical operators and or not
#

x, y = 1, 2 # multiple variable declarations

if x == 1 and y == 2: print("OK")

if x > 0 or y < 10: print("OK")

if not(x != 1 and y != 2): print("OK")


#
# Assignment operators = += -= *= /= %= //= **= &= |= ^= >>= <<=
#

x=2
print(x)
x=x+2
print(x)
x+=2
print(x)


#
# Other operators is | is not | in | not in
#

x=2
y=2
if x is y: print("OK")
if x is not y+1: print("this is OK")
b=[1,1,2,3,4,3,2,2,2]
if 4 in b: print("There is 4 in b")
if 7 not in b: print("There is no 7 in b")



# further reading: https://www.programiz.com/python-programming/operators
