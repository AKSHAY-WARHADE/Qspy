class One:
    def __init__(self,name):
         self.name=name
    def m1(self):
         print(f"The name is {self.name}")
    def m2(self):
        self.m1()
    def m3(self):
        self.m2()

o=One("Akshay")
o.m1()
o.m2()
o.m3()

def m4(self):
    print(f"The First Name is Akshay")

One.m1=m4
o.m2()
o.m3()