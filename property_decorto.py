# class One:
#     def __init__(self,car):
#         self.car=car
#
#     @property
#     def getter(self):
#         return self.car
#
#     @getter.setter
#     def getter(self,car):
#         self.car=car
#
#     @getter.deleter
#     def getter(self):
#         del self.car
#
# c=One("Audi")
# print(c.getter)
# c.getter=("BMW")
# print(c.getter)
# del c.getter
# print(c.getter)
#

# class Twp:
#     def __init__(self,car,price):
#         self._car=car                       #Whenever we have to access multiple objects then we have to delclare variables as protected (_vrname)
#         self._price=price
#
#     @property
#     def getter(self):
#         return self._car,self._price
#
#     @getter.setter
#     def getter(self,model):
#         self._car,self._price=model
#
#     @getter.deleter
#     def getter(self):
#         del self._car
#
#
# c=Twp("Audi","1Cr")
# print(c.getter)
# c.getter=("BMW","X7")
# print(c.getter)
# # del c.getter
# # print(c.getter)