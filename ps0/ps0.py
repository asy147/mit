#here we must use python ps0.py because for some reason py ps0.py doesnt work, py3 isnt recognizing numpy module
import sys
import numpy as np
print (sys.version)
import math

def fun1(x , y):
    print "x**y = ", x**y

def fun2(x):
    print "log(x) = ", np.log2(x)
    
    
if __name__ == '__main__':
    x = int(input("Enter number x: "))
    y = int(input("Enter number y: "))
    fun1(x,y)
    fun2(x)
