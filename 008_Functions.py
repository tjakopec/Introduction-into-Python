def hello():
    print("Hello")


hello()


def hello(tko):
    print("Hello",tko)


hello("Mara")


def evenNumber(x):
    return x % 2 == 0

x=5

print(x, "is" if evenNumber(x) else "not", "even number")


def optionalParameters(x,y=1,z="OK"):
    return str(x + y) + ": " + z;

print(optionalParameters(1))

print(optionalParameters(1,2))

print(optionalParameters(1,3,"X"))


import time



start = time.time()

import ESSIS as e
x=22 #35925949   4666527007
print(x,"is" if e.primeNumber(x) else "not", "prosti broj")
# execute with
# 4666527007 is prime number
# 6420818817615509 cca 10 min
end = time.time()
print(end - start)


number_from,number_to=24,90

for i in e.primeNumbers(number_from,number_to):
    print(i,end="+")

print("=",e.sumPrimeNumbers(number_from,number_to))

