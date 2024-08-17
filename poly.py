# class A:
#     def a(self):
#         self.d="Akshay"
#         self.b="Warhade"
#         print(self.d+self.b)
#
# class B(A):                                                   #Method Overriding or Runtime Polymorphism
#     def a(self):
#         super().a()
#         print(f"The class 1 variable are {self.d} and {self.b}")
#
#
# c=B()
# c.a()



# class A:
#     def a(self,k,l):
#         self.k=k
#         self.l=l
#         print(self.k+self.l)
#
# class B(A):                                                   #Method Overriding or Runtime Polymorphism
#     def a(self,m,n):
#         self.m=m
#         self.n=n
#         super().a("Akshay","Warhade")
#         print(f"The class 2 variable are {self.m} and {self.n}")
#
# c=B()
# c.a("Python","SQl")



# class ABC:
#     def __init__(self):
#         self.a=10
#         self.b=20                                  #Constructor Overriding or Run Time Polymorphism
#         print(self.a+self.b)
#
# class DEF(ABC):
#     def __init__(self):
#         super().__init__()
#         print(self.a*self.b)
# a=DEF()


# class AB:
#     def __init__(self,a,b):                               #Constructor Overloading or Compile Time Polymorphism
#         self.a=a
#         self.b=b
#         print(f"The Name is {a} and {b}")
# class BD(AB):
#     def __init__(self,a,b,c):
#         super().__init__("Akshay","Warhade")
#         self.a=a
#         self.b=b
#         self.c=c
#         print(f"The Current Batches Are : {a} {b} {c}")
#
# c=BD("Python","SQL","WebServices")









#Doubt!!!!!!!!!!!!!!!!!!!!!!!!!!         #It is not possible  to access  the methods of one class to another class outside
# class One:                               #by using the super method  outside the method of another class...
#     def one(self):
#         print("It is a first class method")
# class Two(One):
#     super().one()
#
#     def two(self):
#         print("It is a second class method")
# a = Two()
# a.two()
#
# RuntimeError: super(): no arguments






