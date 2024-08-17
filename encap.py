# class Test:
#     def __init__(self,name,age,gender):
#         self.name=name                               #Public
#         self._age=age                                #Protected
#         self.__gender=gender                         #Private
#         print(self.name)
#         print(self._age)
#         print(self.__gender)
#
#
#     def m1(self):
#         print(self.name)
#         print(self._age)
#         print(self.__gender)
#
#
# c=Test("Akshay","23","Male")
# c.m1()
# print(c.name)
# print(c._age)                           #Accessible outside the class but we should not do it.
#print(c.__gender)                   #AttributeError: 'Test' object has no attribute '__gender'
# To access we can access like (c._Test__gender)   or (Test._Test__gender)



#Accessing Private variable in Child Class:
# class Parent:
#         name="Akshay"
#         _age="23"
#         __gender="male"
#         def demo(self):
#              print(self.name,self._age, self.__gender)
# class Child(Parent):
#     def c(self):
# #       print(self.demo())                               #Here we are directly accessing through method soit will work
#         print(self.name)
#         print(self._age)
# #       print(self.__gender)                                        #AttributeError: 'Child' object has no attribute '_Child__gender'
#
# a=Child()
# a.demo()
# a.c()


# class One:
#     def m1(self):
#         self._name="Sql"
#         self.__city="Pune"
#
# class Two(One):
#     def m2(self):
#         self._name = "Python"
#         self.__city = "Wardha"
#         self.age=20
#
# t=Two()
# #print(t.self._name_)
# #print(t.self__city)




# class One():
#     def __init__(self,name):
#         self.name=name
#
#     def get(self):                                          #Getter method
#         return self.name
#
#     def set(self,name):                                     #Setter method
#         self.name=name
#
#     def delete(self):                                       #Delete Method
#         del self.name
#
# c=One("Akshay")
# print(c.get())
# c.set("Python")
# print(c.get())
# c.delete()
# print(c.get())