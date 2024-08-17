#Constructors

# class const:
#     def __init__(self):                 #default constructor
#         print("Its  a default constructor")
#
# x=const()     #invoked automatically when object  is created
# const.__init__(x)


# class test:
#     def __init__(self):                 #default constructor
#         print("Its  a default constructor")
#
#     def __init__(self):
#         print("Its a second constructor")
#
# a=test()     #invoked automatically when object  is created



#Default Const
# class One:
#     def __init__(self):
#         print("It is a default const")
# a=One()


# class Two:
#     a=100
#     b="helo"
#     c=[1,2,3]
#
#     def __init__(self):
#         print(f"The variables in without parrameteizedd constructor are:")
#         print(f"{self.a}\n{self.b}\n{self.c}")
#
# a=Two()
# b=Two()
# c=Two()



# class Three:
#     def __init__(self,name,city,job):
#         print(f"The Details from prameterized constructor are:")
#         print(f"name:{name},city:{city},job:{job}")
#
# c=Three("Akshay","Pune","Developer")

#
# class Four:
#     name="Akshay"
#     city="Pune"
#     def __init__(self):
#         print(f"The details are: ")
#         print(f"name:{Four.name},city:{Four.city}")
#         print(f"name:{self.name},city:{self.city}")
#
# a=Four()
# a.name="Modiji"
# a.city="Delhi"   #with object it wont modify
# Four.name = "Modiji"
# Four.city = "Delhi"             #It will modify with class name only
# a=Four()




#Instance Variable


# class Five:
#
#     def __init__(self):
#         self.name = "Akshay"
#         self.batch = "Python"
#         self.job = "developer"
#         self.loc = "Pune"
#         print(f"The details from Constructor: \n name:{self.name}, batch:{self.batch}")         #Modificationn through object cant be done through object
#
#     def inst(self):
#         print(f"The details from Constructor: \n name:{self.job}, batch:{self.loc}")    #Only the modificationn will happen in method
#
# a=Five()
# a.name="Iron man"
# a.batch="Ai"
# a.job="Scientist"
# a.loc="Newyork"
# a.inst()


# class Amazon:
#     def __init__(self,pname,price,type,add,cname):
#         self.pname=pname
#         self.price=price
#         self.type=type
#         self.add=add
#         self.cname=cname
#
#     def shop(self):
#         print(f"The shopping details: \n name:{self.pname},price:{self.price},product type:{self.type}")
#
#     def cust(self):
#         print(f"The customer details: \n name:{self.cname},address:{self.add}")
#
# a=Amazon("Watch",1001,"Accessories","Pune","Akshay")
# a.shop()
# a.cust()





#Method Overloading is not possible in python  ( but can be achieved Partially by using default const)

# class One:
#     def two(self,a,b):
#         print(a,b)
#     def two(self,a,b,c):
#         print(a+b+c)
#     def two(self,a,b,c,d):
#         print(a+b+c+d)
#
#     def two(self,a=10,b=20,c=30,d=40):         #Overloading Method ny  using Default Arguments
#         print(a+b+c+d)
#
# x=One()
# x.two(23,30)
# x.two(10,20,30)
# x.two(12,23,45,67)
# x.two()



#Variable Args to Const
# class Car:
#     def __init__(self,name,price,*args,**kwargs):
#         print(f"Car Name: {name},Price:{price}")
#         print(f"{args}")
#         print(f"Extra Info:{kwargs}")
#
# a=Car("Audi","12345000","Agrs","Variable Positonal",a="Model X7",b="2024")
#



####################################### PPP ################################
# class One():
#
#     def __init__(self):       #User defined Non Parameterized Constructor
#         print(self)           #Pointing to main class object address
#         print("Its is a user defined constructor")
#
#     def __init__(self,amt):       #User defined Parameterizedd constructor
#         self.amt=amt
#         print(f"The added amount is: {amt}")
#
#     def m1(self):
#         print("It is a method")
#         print(f"The amount is : {self.amt}")
#
# # o=One()      #Type Error: missing one argument
# o=One(3000)
# One.amt=5000          #modification into instance var using class name is not possible
# o.m1()


