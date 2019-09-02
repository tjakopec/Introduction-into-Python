#
# CLASS
#

class Person:
    first_name=""
    last_name=""


class Student:
    id=""


class Freshmen(Person,Student):
    fraternitie_member=True

    #magic :) https://rszalski.github.io/magicmethods/
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + ("is" if self.fraternitie_member else "not") + " fraternitie member"


s=Freshmen()

s.first_name="Lada"
s.last_name="Jakopec"
s.id="012327282732"
s.fraternitie_member=True

print(s)

#further reading: 
#https://pythonspot.com/encapsulation/
#https://pythonspot.com/polymorphism/
#https://docs.python.org/3/tutorial/classes.html
#https://realpython.com/python3-object-oriented-programming/

