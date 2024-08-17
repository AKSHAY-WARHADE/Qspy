# class first:
#     a=10
#     b="Hello"
#     c=[12,34,56]
#
# f=first()           #It will display the MAIN CLASS OBJECT ADDRESS  <__main__.first object at 0x00000202A00C3F20>
# print(f)
#
# f=first
# print(f)     #It will display the main class     <class '__main__.first'>
#
#
# #We call class elements using two methods that is class name and object
#
# #By using object
# print(f.a)
# print(f.b)
# print(f.c)
#
# #By using classname
# print(first.a)

#We have a Document String to see the title of the class
# class Test:
#     "Hello Guys this is Test Class"     #Title of the class
#     a=10
#     b='python'



# print(Test.__doc__)        #display  the title of the class
#
# help(Test)          #help  will list  all the details of the class


# print(Test.__dict__)    #it wil display the internal dictinonary storage will contain the details  : {'__module__': '__main__', '__doc__': 'Hello Guys this is Test Class', 'a': 10, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>}
                        #Internall the class menbers will be stored in the RAM (Random Access Memory) in the form of Dictionary



class Main:
    a=234
    b="heloo"
    c=[223,45,67]

x=Main()
y=Main()

#Befor Modifiation
# print(Main.a)
# print(Main.b)
# print(x.a)
# print(x.b)
# print(y.a)
# print(y.b)
# Output
# 234
# heloo
# 234
# heloo
# 234
# heloo



#Modifing
Main.a=123
Main.b="python"


#After Modificaton in Main Class
# print(Main.a)
# print(Main.b)
# print(x.a)
# print(x.b)
# print(y.a)
# print(y.b)
# Output
# 123
# python                #Modification Affected to Main as well as Both Objects
# 123
# python
# 123
# python




#Modification in object
x.a=890
x.b="hello"


# print(Main.a)
# print(Main.b)
# print(x.a)
# print(x.b)                    #Modification in particular object will affect that only particular object
# print(y.a)
# print(y.b)
# Output
# 123
# python
# 890
# hello
# 123
# python


#Again Modificatioin in Main Class
# Main.a=786
# Main.b="Buddy"
# print(Main.a)
# print(Main.b)
# print(x.a)
# print(x.b)
# print(y.a)
# print(y.b)
# Output
# 786
# Buddy                 #After again modifying the Main class then it will affect the main as well as another object not the previously modified one
# 890
# hello
# 786
# Buddy




#TYPES OF METHODS
# 1. INSTANCE
# 2. CLASS
# 3. STATIC



# 1. Instance Method
#The method using the object address as an argument

# class instance:
#     def method1(self):
#         pass
# a=instance()            #Creating Object
# a.method1()             #Calling thorough object
# instance.method1(a)     #Calling through the claass name
#
# print(id(instance.method1(a)))   #Same id address
# print(id(a.method1()))

# We Have to pass mandatory object name whenever calling through class name

# Local variable
#
# class instance:
#     def method2(self):
#         amount=1000     #Local variable
#         print(amount)
# a=instance()
# a.method2()
# instance.method2(a)


# class instance:
#     def method2(self,amount):
#         print(amount)
# a=instance()              #Passing Argument to instance method
# a.method2(1000)
# instance.method2(a,1000)


# class instance:
#    a=10             #Global variables
#    b='Heloo'
#    def method1(self):
#        print(f'The varivales are {self.a} and {self.b}')              #Shows error it cant be accessed directly inside the method
#                                                                 #We have to use (self.var_name)
#
# x=instance()
# x.method1()




# class instance:
#    a=10             #Global variables
#    b='Heloo'
#    def method1(self):
#        print(f'The varivales are {self.a} and {self.b}')
#
# x=instance()
#
# x.a=12345                           #Modifying  in object class  so their we are using the object.var_name
# x.b="hi"
# x.method1()
# instance.method1(x)

# class instance:
#    a=10             #Global variables
#    b='Heloo'
#    def method1(self):
#        print(f'The varivales are {self.a} and {self.b}')
#
# x=instance()
# y=instance()
# instance.method1(x)
# x.a=12345
# x.b="hi"
# x.method1()         #Modifying  in main class   so theif we are using the object.var_name it won't affect



#WaP to accept list from the user when the method is called, first index element in the list
# if it is string then reverse the string then replace in same position and return,
# else if it is a integer then ask for user to add a element into a list and return the updated list, else reverse the list and return

# class list:
#     def first(self):
#         a=eval(input("enter a list"))
#         if isinstance(a[1],str):
#                 x=a[1][::-1]
#                 a[1]=x
#                 print(a)
#         elif isinstance(a[1],int):
#                 b=int(input("Enter a number"))
#                 a.append(b)
#                 print(a)
#         else:
#                 a[::-1]
#                 print(a)
# z=list()
# z.first()


# class test:
#     date="31/01/2025"
#     @classmethod
#     def method1(cls):
#         m1=cls()
#         m1.date="23/06/2019"
#         print(f"The Election date is {m1.date}")
#     @classmethod
#     def method2(cls):
#         m2=cls()
#         m2.date="30/12/2021"
#         print(f"The election date is {m2.date}")
#     @classmethod
#     def method3(cls):
#         m3=cls()
#         m3.date="23/05/2056"
#         print(f'The Election date is {m3.date}')
#
# a=test()
# a.method1()
# a.method2()
# a.method3()

# class t:
#     d="Hello"
#     def i(self):
#         print(f"The Modified string is {self.d}")
#
#     @classmethod
#     def c(cls):
#         x=cls()
#         x.d="Buddy"
#         print(f"The modified string is {x.d}")
#
#     @staticmethod
#     def s():
#         print(f"The modifies string is {t.d}")
#
# a=t()
# t.d="Bye"
# a.i()
# a.c()
# a.s()


# class stat:
#     td="23kg"
#     @classmethod
#     def c(cls):
#         print(f'{z.td} is the tredmill weight')
#
#     @staticmethod
#     def s(k):
#         print(f'{z.td} is the weigt of tredmill and passed value={k}')
#
# z=stat()
# z.td="43kg"
# z.c()
# z.s(23)


#################################### Personal Practice Programs ###################################################
# class One():
#     name="Akshay"
#     age=23
#
# print(One.name)
# print(One.age)
#
# c=One
# print(c)
# #op:- <class '__main__.One'>
#
# d=One()
# print(d)
# #op:- <__main__.One object at 0x000002246AEE0500>
#
# print(d.name)
# print(d.age)
#
# print(c.name)
# #Note:If we keep paranthesis while creating the object
# it will show the output otherwise also it will  show the output
# print(c.age)

# print(One.__dict__)

# One.name="Python"
# One.age=25
# print(One.name)
# print(One.age)
# #Modification by class name affecting everypart
# print(c.name)
# print(c.age)
# print(d.name)
# print(d.age)

# c.name="SQl"
# c.age=45            #Modification by object affecting every part
# print(c.name)        #it will affect all only when the object is created without parentheses
# print(c.age)         #that  means the object will be pointing to main class only so modification in main will affect whole part
# print(d.name)
# print(d.age)
# print(One.name)
# print(One.age)

# d.name="Web"
# d.age=78
# print(d.name)         #So here the modification by object only affect when are calling by using that object only
# print(d.age)
# print(c.name)          #Other parts remains the same
# print(c.age)           #And it will also break the relation between main class and object
# print(One.name)
# print(One.age)

# One.name="Prabhu"
# One.age=27
# print(One.name)         #So when again modify using the class name
# print(One.age)          #then it will not affect the recently modofied object
# print(c.name)
# print(c.age)
# print(d.name)
# print(d.age)


# print(One.__doc__)
# #For now the class name don't have any title then it will show NONE as output
# print(c.__doc__)
# print(d.__doc__)


# class Two():
#     "This is Doc String Example"           #Title for the class
#     a=10
#     b="hello"
#     def m1(self):
#         ...
# t=Two()
# t1=Two
# print(Two.__doc__)      #It will give the title of the class only in output
# print(t.__doc__)
# print(t1.__doc__)
#
# print(help(Two))    #If we use help function the it will show the whole structure including all class members
#print(help(t))
#print(help(t1))



######Methods#####
# class Method():
#
#     name="Akshay"       #Global Variable
#     edu="mca"
#
#     def m1(self):      #Instance Method
#         a=10
#         b="hello"
#         print(a,b)
#
#     def m2(self,c,d):
#         c=c
#         d=d
#         print(c,d)
#
#
#     def datatype(self,x):
#         x=x
#         d=type(x)
#         return d,x
#         #use of return keyword to access local variable outside class
#
#
#     def var(self):
#         print(f"Class variable {self.name} and {self.edu}")
#         #To use class variable inside method we need to use "self" keyword or "classname"
#         print(f"The class variables are: {Method.name} \n {Method.edu}")
#
# m=Method()
# m.m1()
# Method.m1(m)            #Whenever accessing the method by classname then only we have pass the object explicitly
# a=Method                #Same applies here bcoz it points to main class
# a.m1(a)

# m.m2("Akshay ","Warahde")
# Method.m2(m,"Python ","Sql")

# print(m.datatype(23.45))

# m.var()


# class M1():
#     c="Global variable"
#     d="Instance method"
#
#     def m1(self):
#         print(f"The variables are:\n{M1.c}\n{M1.d}")
#         # calling using classname
#         print(f"The data :\n{self.c}\n{self.d}")
#         # calling by "self" so it will affect
#
# a=M1()
# a.m1()
# a.c="Class variable"
# a.m1()
# here after modification the output will be same as we are calling using classname in method
# and we are modifying it using object
# so we have to modify using class name or call using self in method


# class C():
#     var="Hi"
#     @classmethod
#     def method(cls):
#         print("It is a @classmethod")
#
#     @classmethod
#     def method2(cls):
#         print(f"The class variable is {C.var}")
#
#     @classmethod
#     def method3(cls):
#         print(f"the variable is : {cls.var}")
#
#     @classmethod
#     def method4(cls):
#         print(f"the variable is {c.var}")


# C.method()
# here we need not to pass the object explicitly
# as the class method will be pointing to main class itself
# c=C()
# c.method()
# c.method2()
# c.method3()
# c.method4()
# C.var="Python"
# c.method()
# c.method2()
# c.method3()
# c.method4()



# class stat():
#     a=10
#     b=20
#     @staticmethod
#     def m1():
#         print("it is a static method")
#         # print(stat.a+stat.b)
#
#
#     @staticmethod
#     def m2(a,b):
#         print(a+b)        #40
#         print(s.a+s.b)    #300    #here when i'm calling through object and modifying through same it works
#
# s=stat()
# stat.m1()

# stat.a=20
# stat.b=30      #If we are modifying by class name and calling through it then it works

# if we are doing two diff things
# like modifying by diff thing and calling through diff the it wont work
# s.a=20
# s.b=30          #Modification through object and call through same then it will work

# s.m1()
# #s.m2(30, 10)     #If I am calling method first and then modifying then it shows error
# s.a=100
# s.b=200
# s.m2(30, 10)  #Here if i calling it will work and it is taking updated values(passed valued)




# class Combo():
#     a=10
#     b=20
#
#     def inst(self):
#         print(self.a+self.b)
#         print(self)
#
#     @classmethod
#     def cla(cls):
#         print(cls.a*cls.b)
#         print(cls)
#
#     @staticmethod
#     def stat():
#         print(Combo.a/Combo.b)
#         print(c.a/c.b)
#
# c=Combo()
# c.inst()
# c.cla()
# c.stat()
# Combo.a=5
# Combo.b=5
# c.inst()
# c.cla()
# c.stat()


