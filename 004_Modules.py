#https://docs.python.org/3/library/math.html
import math #part of basic installation
print(math.pi)


#pip => Python Packaging Index => package manager

# use CLI=> win: cmd, linux: bash, macOs: terminal
# python -m pip install nameOfPackage

#example how to isntall scipy package
#pip install scipy

#1
#from scipy import constants
#print(constants.pi)

#2
import scipy.constants as k
#3
#from scipy import constants as k
print(k.pi)

#http://scienceworld.wolfram.com/physics/ThomsonCrossSection.html
print(k.value("Thomson cross section"))

#više na https://docs.scipy.org/doc/scipy/reference/constants.html

# for kids
import turtle as t
t.fd(100)
