# d={}
# print(d)
# print(type(d))
#
# dict=dict()
# print(dict)

d={1:"Hello",2:"Hi",3:"Bye"}
#print(d)
d[4]="GoodNight"
#print(d)


d.update({5:"Good morning"})
#print(d)
d.update({5:"GoodMorning"})
#print(d)
d[(3,4)]=["h","i"]
#print(d)
d.update({(1,2,3):[23,45]})
#print(d)


d.setdefault(7)
#print(d)
d.setdefault(7,"Null")
#print(d)
d.setdefault(6,"Python")
print(d)

# a={234,45}
# print(dict.fromkeys(a))
# print(a)
# print(dict.fromkeys(a,"Happy"))
# b={23:"Helo"}
# print(dict.fromkeys(b,"null"))
# print(b)

# print(d.pop(234,"Key Not Found"))
# print(d.pop((3,4)))
#
print(d.popitem())
print(d.popitem())
print(d)

# print(d.get((1,2,3)))
#
# print((dir(dict)))
# print(d.items())
# print(d.keys())
# print(d.values())

# x=d.copy()
# print(x)
# print(id(d))
# print(id(x))
# x.clear()
# print(x)

