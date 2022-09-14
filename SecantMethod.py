# Root-Finding-Methods-of-Non-Linear-Equations
# program for finding roots by Secant Method
import math
a=float(input("enter the value of frist interval "))
b=float(input("enter the value of second interval  "))
e=float(input("enter the value of error  "))

def f(x):
    #you can change the equation according to your qn
    return x**4-x-10
    


def secant(a,b):

    if(f(a)*f(b)>0):
        print("invalid statment")
    else:
        
        m=(a*f(b)-b*f(a))/(f(b)-f(a))
        i=1
        while(abs(f(m))>e):
            print(i,"  ",a,"  ",b,"  ",m,"  ",f(m))
            a=b
            b=m
            m=(a*f(b)-b*f(a))/(f(b)-f(a))
            i=i+1   
        print(i,"  ",a,"  ",b,"  ",m,"  ",f(m))
secant(a,b)
