#   Single Level Inheritance
# class Parent:
#     a=10
#     b=20
#     c=a+b
#     print("It is Parent Class")
#
# class Son(Parent):
#     print(f"Accessing members of Parent")
#     print(f"The sum:{Parent.a}")                               #Accessing Variables Directly from Parent to child
#
# s=Son()



# Multi Level Inheritance
# class RBI:
#     def Notes(self):
#         self.a=10
#         self.b=20
#         print("Notes are printed by Rbi")
#
# class SBI(RBI):
#     def Money(self):
#         c=self.a+self.b
#         print(c)
#         print("The Sbi will get the notes from rbi")
# class SmallF(SBI):
#     def loan(self):
#         d=self.a*self.b
#         print(d)
#         print("The small will take loan from sbi")
# s=SmallF()
# s.Notes()
# s.Money()
# s.loan()






#Multiple inheritance
# class Restaurant:
#     def M1(self):
#         print("This is Vaishali Restaurant")
#
# class DeliverBoy:
#     def M2(self):
#         print("This is Delivery Boy Class")
#
# class Customer(Restaurant, DeliverBoy):
#     def M3(self):
#         print("This is customer")
#
# c=Customer()
# c.M1()
# c.M2()
# c.M3()



#Hierarchical Inheritance
# class TestYantra:
#     def m1(self):
#         print("it is the parent company")
#
# class QSPY(TestYantra):
#     def M2(self):
#         print("it is child company of test yantra software solutions")
#
# class PYSPY(TestYantra):
#     def M3(self):
#         print("It is also a child company of Test Yantra")
#
# q=QSPY()
# q.m1()
# q.M2()
#
# p=PYSPY()
# p.m1()
# p.M3()



#Hybrid Inheritance






#Method Chaining    (It is use for Method Overriding  to avoid the only updated format andd display both)
# class One:
#     def one(self):
#         print("Class One Method")
#
# class Two(One):
#     def one(self):
#         super().one()
#         print("Class Two Method")
# t=Two()
# t.one()


# class Mobile:
#     def insta(self,username,acc_type):
#         self.name=username
#         self.type=acc_type
#         print(f"Username:{self.name}\nAccount_Type:{self.type}")
# class Instagram(Mobile):
#     def insta(self,followers,following,posts):
#         self.followers=followers
#         self.following=following
#         self.posts=posts
#         super().insta("Akshay_Warhade","Public")
#         print(f"\nFollowers:{self.followers}\nFollowing:{self.following}\nPosts:{self.posts}")
# i=Instagram()
# i.insta(734,602,20)




# class Mobile:
#     def __init__(self,username,acc_type):
#         self.name = username
#         self.type = acc_type
#     def insta(self):
#         print(f"Username:{self.name}\nAccount_Type:{self.type}")
# class Instagram(Mobile):
#     def __init__(self,followers,following,posts):
#         super().__init__("Akshay_Warhade","Public")
#         self.followers = followers
#         self.following = following
#         self.posts = posts
#     def insta(self):
#         super().insta()
#         print(f"\nFollowers:{self.followers}\nFollowing:{self.following}\nPosts:{self.posts}")
# i=Instagram(734,602,21)
# i.insta()









#Constructor Chaining
# class One:
#     def __init__(self):
#         print("Class One Method")
#
# class Two(One):
#     def __init__(self):
#         super().__init__()
#         print("Class Two Method")
# t=Two()




# class Mobile:
#     def __init__(self,cont_name,cont_status):
#         self.cont_name=cont_name
#         self.cont_status=cont_status
#
# class Whatsapp(Mobile):
#     def __init__(self,updates,calls,chats):
#         self.updates=updates
#         self.calls=calls
#         self.chats=chats
#         super().__init__("Akshay","Urgent Calls Only")
#         print(f"The Details of Mobile Class:\n{self.cont_name}\n{self.cont_status}")
#         print(f"The Details of Whatsapp Class: \n{self.calls}\n{self.updates}\n{self.chats}")
#
# w=Whatsapp(updates=3,calls=12,chats=100)






#Method Overriding in Multiple Inheritance
# class A:
#     def spam(self):
#         print("Spam")
#
# class B:
#     def spam(self):
#         print("Demo")
#
# class C(A,B):
#     def cool(self):
#         print("Cool")
#
# c=C()
# c.cool()
# c.spam()
# print(C.__mro__)       #o/p:-(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)



# class A:
#     a=10
#     b=23
#     def add(self):
#         print(self.a+self.b)
# class B:
#     c=27
#     d=78
#     def add(self):
#         print(self.c+self.d)
# class C(A,B):
#     e=23
#     f=12
#     def sub(self):
#         print(self.e-self.f)
#
# c=C()
# c.sub()
# c.add()
# print((C.__mro__))                        #It Stands For METHOD RESOLUTION ORDER use to check the path of execution




# class A:
#     def A1(self):
#         print("Outer Class")
#     class B:
#         def B1(self):
#             print("Inner Calss")
#         class Demo:
#             def D1(self):
#                 print("Demo Class")
# c=A()
# c.A1()
# a=A().B()
# a.B1()
# d=A().B().Demo()
# d.D1()
#
# s=c.B()
# t=s.Demo()
# c.A1()
# s.B1()
# t.D1()


#Hybrid Inheritance

# class One:
#     def one(self):
#         print("It is One class")
#
# class Two:
#     def two(self):
#         print("It is second class")
#
# class Three(One):
#     def three(self):
#         print("it is a third class")
#
# class Four(One,Two):
#     def four(self):
#         print("It is class four")
#
# class Five(Three):
#     def five(self):
#         print("It is fifth class")
#
#
# a=Three()
# a.one()
# a.three()
# b=Four()
# b.one()
# b.two()
# b.four()
# c=Five()
# c.one()
# c.three()
# c.five()
