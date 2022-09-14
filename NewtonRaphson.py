# program to find the roots by Newton Raphson method
import math
b=float(input("enter the value of b  "))
e=float(input("enter the value of error  "))

def f(x):
    
    return x**4-x-10 
def f1(x)  : 
    return 2*x-1 


def Newton(b):

    if(f1(b)!=0):
        m=b-f(b)/f1(b)
        i=1
        while(abs(f(m))>e):
            print(i,"  ",b,"  ",m,"  ",f(m))
            b=m
            m=b-f(b)/f1(b)
            i=i+1   
        print(i,"  ",b,"  ",m,"  ",f(m))
        
    else:
        print("invalid statment")
        
Newton(b)

