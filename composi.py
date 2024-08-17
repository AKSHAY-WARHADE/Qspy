#Composition

# class One:
#     print("it is class One")
#                                             #Accing one class from another simply
# class Two:
#     print("it is class two")
#     o=One()
# t=Two()



# class One:
#     def __init__(self):
#         print("it is class One constructor")
#
# class Two:                                                        #Accessing Constructor of one class fro another
#     def __init__(self):
#         print("it is class two constructor")
#     o=One()
# t=Two()


# class One:
#     name="Akshay"
#     def __init__(self):
#         print("it is class One constructor")
#
#                                                               #Accessing global variable of one class into another
# class Two:
#     def __init__(self):
#         print("it is class two constructor")
#     o=One()
#     print(o.name)
# t=Two()



# class One:
#     name="Akshay"
#     def __init__(self):
#         print("it is class One constructor")
#     def M1(self):
#         print("It is class one method")                               #Accessing method from one cass to another
#
#
# class Two:
#     def __init__(self):
#         print("it is class two constructor")
#     o=One()
#     print(o.name)
#     o.M1()
# t=Two()



# class One:
#     name = "Akshay"
#     def __init__(self):
#
#         print("it is class One constructor")
#     def M1(self):
#         print("It is class one method")
#
#                                                           #Accessing variable of one class into another class constructor
# class Two:
#     def __init__(self):
#         print("it is class two constructor")
#         self.o = One()
#         print(self.o.name)
#         self.o.M1()
#
# t=Two()




#Accessing variables declared in the method of one class into the method of another class
# class Car:
#     def __init__(self,name,model,price):
#         self.name=name
#         self.model=model
#         self.price=price
#     def Bmw(self):
#         self.color="Blue"                           #These needs to instance variables to be accessed
#         self.seats="Leather"
#         print(f"The car details are Name:{self.name} \n Price={self.price} \n Model:{self.model}")
#
# class Vehicle:
#     def __init__(self,type,wheels):
#         self.type=type
#         self.wheels=wheels
#         self.c=Car("Avantador","Quadrajet","3.5Cr")
#         self.c.Bmw()
#
#     def A(self):
#         print(f"Print the metadata \nType:{self.type}\n wheels:{self.wheels},\n ")
#         # print(f"Method data \n Colour:{x.color},Seat Material:{x.seats}")
#         x=Car("Avantador","Quadrajet","3.5Cr")
#         x.Bmw()
#         print(f"Method data \n Colour:{x.color},Seat Material:{x.seats}")     #we have to call it after object creation by the object of the another class
#
# v=Vehicle("Car","Four")
# v.A()

######################### PPP #############################################
# class One():
#     a="Class One"
#     def m1(self):
#         print("Method of Class One")
#
# class Two():
#     def m2(self):
#         print("Method of class Two")
#         self.x=One()
#         One.m1(self.x)
# t=Two()
# t.m2()


