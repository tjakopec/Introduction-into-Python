#comment one line
"""
Comment multiple
lines
"""


"""
NUMBERS
"""
#integer
x = 7
print(x, "=>", type(x))

#float
x = 7.5
print(x, "=>", type(x))

#complex number
x = 7+2j
print(x, "=>", isinstance(1+2j,complex), "complex number")



"""
LIST
"""
#
# list
#
# elements of list can be different type
list_type=[7,7.5,7+2j, "String", bool(1)]
print(list_type)

#list parts
x = [1,2,3,4,5,6,7,8,9]
print("x[2] = ", x[2])
print("x[0:3] = ", x[0:3])
print("x[5:] = ", x[5:])

#add element to index 0, all other indexes change
x.insert(0,-1)
print(x)
# delete last element
del x[len(x)-1]
print(x)

# the list can be changed (mutable)
x[2]=7
print(x)

#
# tuple
#
# same as list with exception that list elements cannot be modified (immutable)
tuple_type=(7,7.5,7+2j, "String", bool(1))
print(tuple_type)

#patrs of tuple
x = (1,2,3,4,5,6,7,8,9)
print(x)
print("x[2] = ", x[2])
print("x[0:3] = ", x[0:3])
print("x[5:] = ", x[5:])
# tuple cannot be modified (TypeError: 'tuple' object does not support item assignment)
#x[2]=7
#print(x)


#
# set
#
# same as list except that the elements can be unique

x = {1,7,7,5,5,5,2,2,2,2}
print(x)
x=sorted(x, reverse=True)
print(x)
x.insert(0,3)
print(x)
x=sorted(x)
print(x)


#
# dictionary (json look-alike)
#
x={"name":"Tomislav","years": 39}
print(x)
print(x["name"])

#
# combination (kao Praskaton)
#
x=1
data = {
    "id": x,
    "grades": (2,2,3,2,3,2,3,2,3,2),
    "points": [7,8,7,6,5,6,7,6,5,6],
    "items": {1,2,3,4,5,6,7,8,9,10}
    }
print(data)

#
# Array of characters (String)
#

x="ESSIS"
print(x)
print(x[0])   
print(x[2:4])
print(x[2:])    
print(x * 2)
print(x + " 2019") # Prints concatenated string

#String cannot be modified (immutable)
#x[2]="B"
x=list(x)
x[2]="B"
x="".join(x)
print(id(x))
print(x)
x=x.replace("B","l")
print(id(x))
print(x)

#
# conversions
#

x=float("58.8")
print(x)
x=int(x)
print(x)
string=str(x)
print(string)
lista=list(string)
print(lista)
skup=set(string)
print(skup)
ntorka=tuple(string)
print(ntorka)
rjecnik=dict([("x1",1),("x2",1)])
print(rjecnik)

# further reading https://docs.python.org/3/library/functions.html

