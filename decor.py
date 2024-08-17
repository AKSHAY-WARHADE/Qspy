# import time
#
#
# def outer(func):
#     def inner(*args, **kwargs):
#         time.sleep(5)
#         print("it is working")
#         time.sleep(3)
#         func(*args, **kwargs)
#
#     return inner()
#
#
# @outer
# def main():
#     print("Akshay")
#
#
# main()
import time


# def outer(main_func):   #1
#     def inner(a,b):    #3
#         print("Addition Operator")  #7
#         main_func(a,b)  #5
#         print("Addition Operator Completed")
#     return inner   #4
# @outer   #  outer(main_func)--->2
# def main_func(a,b):
#     print(a+b) #8
# main_func(10,20)   #6


# def outer(func):
#     def inner(*args, **kwargs):
#         time.sleep(5)
#         func(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def add(a, b):
#     print(a + b)
# @outer
# def sub(c, d):
#     print(c - d)
# @outer
# def mul(e, f):
#     print(e * f)
#
#
# add(10, 20)
# sub(20, 10)
# mul(5, 5)


# def outer(func):
#     def inner():
#         s=time.time()
#         func()
#         e=time.time()
#         t=e-s
#         print(f"Time taken = {t}")
#     return inner
# @outer
# def start():
#     print("Starting")
#     time.sleep(2)
# @outer
# def end():
#     print("Ending")
# start()
# end()


# write a prog before executing main fun we want to print the main func name
# def outer(func):
#     def inner():
#         print(__name__)
#         func()
#     return inner
#
# @outer
# def main_func():
#     print("It is a main function name")
# main_func()


# Multiple decorator single fun

# def outer_most(func):
#     def inner(*args,**kwargs):
#         print("Qspiders")
#         func(*args,**kwargs)
#     return inner
# def outer(func):
#     def inner_most(*args,**kwargs):
#         print("Pyspiders")
#         func(*args, **kwargs)
#     return inner_most
#
#
# @outer_most
# @outer
# def main():
#     print("Welcome to Python Session")
# main()



# wap to create a decorator to which prints the name of the called function along with it should check if it the number is even or odd
# def outer(func):
#     def inner(a):
#         print(__name__)
#         main_func(a)
#     return inner
# @outer
# def main_func(a):
#     if a%2==0:
#         print(a)
# main_func(10)




# # Create a decorator to  return only positive output from any substraction
# def outer(func):
#     def inner(*args,**kwargs):
#         print(abs(x))
#         func(*args,**kwargs)
#     return inner
# @outer
# def sub(a,b):
#     x=a-b
#     print(x)
# sub(10,20)   Not possible to access the  result variable in decorator


# def outer(func):
#     def inner(a,b):
#         res=func(a,b)
#         return abs(res)
#     return inner
# @outer
# def sub(a,b):
#     print(a-b)
#     return a-b
# print(sub(1,3))





# Q1
# def outer(one):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         one(a,b)
#     return inner
# @outer
# def one(a,b):
#     if a>b:
#         print(a/b)
# one(10,20)
# one(30,5)


# Q2
# def outer(two):
#     def inner(*args):
#         print("performing addition")
#         two(*args)
#         print('Addition Performed')
#     return inner
# @outer
# def two(*args):
#     print(sum(args))
# two(25,20,50,5)


# Q5
# def outer(func):
#     def inner(*args):
#         for i in args:
#             print(type(i))
#         func(*args)
#     return inner
# @outer
# def main_func(*args):
#     print(args)
# main_func(10,20.5,89+76j,True,[1,2,3])



# Q6
# def outer(six):
#     def inner(*args,**kwargs):
#         print(f"The sum of positional arguments:{sum(args)}")
#         six(*args,**kwargs)
#     return inner
# @outer
# def six(*args,**kwargs):
#     print(f"The Length of Keywords Arguments:{len(kwargs)}")
# six(10,20,30,40,a="Hello",b=23,c=78+6j)

# def outer(seven):
#     def inner(a,b):
#         if a>b:
#             print(f"The Multiplication is : {a*b}")
#         else:
#             print(f"The Cubes are : {a**3},{b**3}")
#         seven(a,b)
#     return inner
# @outer
# def seven(a,b):
#     print(f"The Numbers are: {a}, {b}")
# seven(5,15)



# #Delay Decorators
from time import sleep
# def outer(func):
#     def inner(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#     return inner
# @outer
# def main(a,b):
#     time.sleep(2)
#     print(f"Add: {a+b}")
#
# def main1(a,b):
#     time.sleep(2)
#     print(f"Sub: {a-b}")
# main(10,20)
# main1(56,45)



#Parameterized Decorator
# import time
# def outer_most(n):
#     def outer(func):
#         def inner(*a,**k):
#             time.sleep(n)
#             # print(n)
#             func(*a,**k)
#
#         return inner
#     return outer
#
# @outer_most(2)
#
# def add():
#     print("operator")
#
# add()
#
#
# @outer_most(2)
# def sub():
#     print('sub')
# sub()



#We can use here timeit() function also to calculate total execution time

import timeit
code_test="""
s=time.time()
def outer_most(n):
    def outer(func):
        def inner(*args):
            print(n)
            start = time.time()
            print(f"The Start Time of function: {start}")
            print(func.__name__)
            func(*args)
            end=time.time()
            print(f"The End Time of function is : {end}")
            dif=end-start
            print(f"Total Execution Time of function : {dif}")
            return dif
        return inner
    return outer

@outer_most("Add Func")
def one(a,b):
    time.sleep(2)
    print(f"Addition: {a+b}")
@outer_most("Sub Func")
def two(c,d):
    time.sleep(3)
    print(f"Substarction: {abs(c-d)}")
@outer_most("Multi Func")
def three(e,f):
    time.sleep(4)
    print(f"Multiplication : {e*f}")
@outer_most("Div Func")
def four(g,h):
    time.sleep(5)
    print(f"Division: {g/h}")

one(10,20)
two(30,5)
three(35,67)
four(234,44)

e=time.time()
print(f"The Total Execution Time of Program is : {e-s}")
"""
t=timeit.timeit(code_test,number=1)
print(f"Total Execution time using Timeit Function: {t}")







#wap to check the role of the person if the role is admin it should print the username and password if it is an employee it should print access denied if it is not both print invalid role
# count = 0
# def outer_most(role):
#     def outer(func):
#         def inner(*args):
#             if role=="admin":
#                 print("Access Granted")
#                 func(*args)
#                 global count
#             elif role=="employee":
#                 print("Access Denied")
#             else:
#                 print("Invalid Role")
#         return inner
#     return outer
#
# @outer_most("admin")
# def one(username,password):
#     print(f"The username is :{username} and password is : {password}")
# one("admin","admin123")
# one("admin","admin123")
# one("admin","admin123")
# one("admin","admin123")







