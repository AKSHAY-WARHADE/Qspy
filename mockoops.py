#Basic Methods
# class One():
#     name="Akshay"
#     _b="Hello"
#     __age=23
#
#     def __init__(self,sub):
#         self._subject=sub
#         print(f"It is a parameterized constuctor")
#
#     def inst(self,edu):
#         print("It is an instance method")
#         print(f"Accessing Constructor variables in instance method: \n{self.name}\n{self._subject}")
#         print(f"Method data: {edu}")
#
#     @classmethod
#     def cla(cls,city):
#         print("It is a class method")
#         print(f"Accessing Constructor variables in class method: \n{cls.name}\n{o._subject}")
#         print(f"Accessing method data: {city}")
#
#     @staticmethod
#     def stat(one,two):
#         print("it is a static method")
#         print(f"It is static method data :{one}\n{two}")
#         print(f"Accessing class data : {One.name}\n {One._b} \n{One.__age}")
#
#
# o=One("CS")
# o.inst("MCA")
# o.cla("Pune")
# o.stat("python","sql")




#Inheritance

# class Hybrid():
#     def __init__(self):
#         self.a=10
#         self.b=20
#         print("It  is a parent class constructor")
#     def h1(self,name):
#         self.name=name
#         print("It is a parent class method")
# class Single(Hybrid):
#     def S1(self,age):
#         self.age=age
#         super().h1("Prabhu Sir")
#         print("It is a single class method")
#         print(f"Accessing base class variable for addintion: {self.a+self.b}")
#         print(f"Accessing parent method variable: {s.name}")
#
# class Multilevel(Single):
#     def M1(self,gender):
#         self.gender=gender
#         print("It is a Multilevel Class Method")
#         print(f"Accessing Super Class(Hybrid) : {s.name}")
#         print(f"Accessing Parent Class(Single): {s.age}")
#
# class Multiple(Single,Hybrid):
#     def M2(self):
#         print("it is a multiple class method")
#         print(f"Accessing Variables: {s.age}\n{m.gender}")
#
# s=Single()
# s.h1("Akshay")
# s.S1(23)
# m=Multilevel()
# m.h1("Rahul")
# m.S1(24)
# m.M1("Male")
# mul=Multiple()
# mul.h1("Vaibhav")
# mul.S1(25)
# mul.M2()



#Abstraction
# from abc import *
# class One(ABC):
#     @abstractmethod
#     def m1(self):
#         ...
# class Two(One):
#     def m1(self):
#         print("It is a abstract class method")
# t=Two()
# t.m1()

#Polymorphism
# class One():
#     def m1(self):
#         self.a=10
#         self.b=20
#         print(f"Addition {self.a+self.b}")
#
# class Two(One):
#     def m1(self):
#         super().m1()
#         print(f"Substraction {self.a-self.b}")
#
# t=Two()
# t.m1()

class On():
    @staticmethod
    def a1():
        a=10
        b=20
        print(f"Addition: {a+b}")

class Off(On):
    @staticmethod
    def m2():
        super(On).a1()

o=Off()
o.m2()
print(Off.__mro__)