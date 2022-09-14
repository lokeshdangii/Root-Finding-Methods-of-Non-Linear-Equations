# program to find the roots of Bisection Method
import math
a=float(input("enter the value of a "))
b=float(input("enter the value of b  "))
e=float(input("enter the value of error  "))

def f(x):
    
    return x**4-x-10


def bisection(a,b):

    if(f(a)*f(b)>0):
        print("invalid statment")
    else:
        
        m=(a+b)/2
        i=1
        while(abs(f(m))>e):
            print(i,"  ",a,"  ",b,"  ",m,"  ",f(m))
            if(f(m)<0):
                a=m
            else:
                b=m
            m=(a+b)/2
            i=i+1   
        print(i,"  ",a,"  ",b,"  ",m,"  ",f(m))
bisection(a,b)
