## function practice 
from _operator import add, mul
from ctypes.wintypes import INT
from builtins import int
from math import factorial
from pip._vendor.distlib.compat import raw_input
def hello():
    print("Hello world!")

hello() #here we can see that we do not need to write the whole code again & aganin, we can call it 100 times if we want 
hello()
hello() 

#practice it again 
def wish():
    print("Happy birthday")
wish() 

def greetings():
    print("Eid Mubarak")
greetings() 

def newyear():
    print("Shuvo Noborsho")
newyear()

# now lets add two numbers and call it as a function 
def add(x,y):
    return(x+y)
print(add(11, 9))
print(add(10, 20))
print(add(45, 55))
## Multiplication
def mult(a,b):
    return(a*b)
print(mult(6, 2))
print(mult(10, 10))
## Divide
def div(s,t):
    return(s/t)
print(div(20,4)) 
## square 
def sqaure(s):
    return(s*s)
print(sqaure(8))
print(sqaure(7))
print(sqaure(10))
## now we will do the function practice form the console
## we will take the input from the console 
def name(name):
    print("What is your name:" + name)
your_name=input("Enter your name:")
name(your_name)
## enter ur namein console and get greetings 
def greet(name):
    print("How are you doing today?:"+name)
Name=input("May I have your name please?:")
greet(Name)

def Hola(firstname):
    print('Hello '+firstname)
first_name=input("What is your First Name? ")
Hola(first_name)

def thanks(lastname):
    print("Gracious! "+lastname)
gratitude=input("What's your last name? ")
thanks(gratitude)

def DOB(dateofbirth):
    print("So, you are new year eve baby")
birthday=int(input("What is your date of birth? "))
DOB(birthday)

#now lets make a od or even number function. 
def checknumber(n):
    if n%2==0:
        print("This is an even number")
    else:
        print("This is an odd number")
check=float(input("enter the number: "))
checknumber(check)
checknumber(check)
## find out a number is prime 
def primenumb(p):
    for p in range(1,10):
        if (p>1):
            for q in range(2,p):
                if (p%q)==0:
                    print("This is not prime",p)
                    break
            else:
                print("This is prime",p)
prime=int(input("Check the prime: "))
primenumb(prime)
## recursion 
def factorial(v):
    if v==1:
        return 1
    else:
        return(v * factorial(v-1))
print(factorial(4))
## recusrsion example
print("hello")




                    
            
        


    



