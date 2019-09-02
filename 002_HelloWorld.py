name = input("Type your name ")
print("Hello " + name)


print("Hello", name)

grade=5

print("Student rating %s is %s" % (name, grade))
print("Student rating %(u)s is %(o)s" % {"u": name, "o": grade})
print("Student rating {} is {}".format(name, grade))
print("Student rating {0} is {1}".format(name, grade))
print("Student rating {u} is {o}".format(u=name, o=grade))
print("Student rating",name,"is",grade)
