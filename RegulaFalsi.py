# program for finding roots by Regula_falsi method or False position
import math
a=float(input("enter the value of a "))
b=float(input("enter the value of b  "))
e=float(input("enter the value of error  "))

def f(x):
    #you can change the equation according to your qn
    return x**4-x-10


def falsi(a,b):

    if(f(a)*f(b)>0):
        print("invalid statment")
    else:
        
        m=(a*f(b)-b*f(a))/(f(b)-f(a))
        i=1
        while(abs(f(m))>e):
            print(i,"  ",a,"  ",b,"  ",m,"  ",f(m))
            if(f(m)<0):
                a=m
            else:
                b=m
            m=(a*f(b)-b*f(a))/(f(b)-f(a))
            i=i+1   
        print(i,"  ",a,"  ",b,"  ",m,"  ",f(m))
falsi(a,b)
