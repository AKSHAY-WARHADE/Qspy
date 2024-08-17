import os

# print(os.getcwd())

# os.chdir(r"C:\Users\LENOVO\Desktop\demo")
# print(os.getcwd())

#os.mkdir("Akshay")

#os.mkdir("Sql")

# os.rmdir("Akshay")

# print(os.listdir())

# os.popen("akshay.txt")

# os.remove("akshay.txt")

# print(os.path.getsize("Python"))

#print(os.getcwd())
#os.chdir(r"C:\Users\LENOVO\Desktop\demo\Python")
#print(os.getcwd())

# f=open("file1.txt","w")
# f.writelines(["Hello\n","This is my first\n","Filehandling class\n"])

# f=open("file1.txt","r")
# print(list(f))

# with open("file1.txt","r") as file:
    # print(file.read())
    # print(file.readline())
    # print(file.read(2)) Number of characters will be displayed as specified
    #  print(file.write(" Hello\n The is my first\n python class "))  #print the no of characters present in the file
    # print(file.writelines(["Hello\n","Hi\n","This is amazing"]))
    # print(file.read())
    # print(file.tell()) #tell the position  of the cursor
    # print(file.seek(0)) #navigate the cursor position

# from itertools import islice
# with open("file1.txt","r") as file:
#     d=islice(file,0,3,1)
#     # print(list(d))
#     for i in d:
#         print(i)

# from collections import deque
# with open("file1.txt","r") as f:
#     d=deque(f,2)
#     for i in d:
#         print(i)




# with open("h1.csv","w",newline="") as f: #the newline="" will remove the  spaces between lines the syntax has to be followed as it is
#     w=csv.writer(f)
#     w.writerow("Hello")
#     w.writerow(["Hi","Buddy"])
#     w.writerows([["Hello"],["How"],["are"],["you"]])
#
# os.popen("h1.csv")


os.chdir(r"C:\Users\LENOVO\Desktop\demo\Python")
import csv
# with open("h2.csv","w",newline="") as f:
#     d=csv.DictWriter(f,["Name","Age"])
#     d.writeheader()
#     d.writerow({"Name":"Akshay","Age":23})
# os.popen("h2.csv")

# with open("h3.csv","w",newline="")as f:
#     d=csv.DictWriter(f,["Name","Location"])
#     d.writeheader()
#     d.writerows([{"Name":"Akshay Warhade","Location":"Wardha"},{"Name":"Yashshri","Location":"Yavatmal"}])
# os.popen("h3.csv")

# with open("h3.csv","r")as f:
#     d=csv.reader(f)
#     for i in d:
#         print(i)





#Pickle
#Pickling or Serializtion

import pickle
#Without File Handling
# s=("python")
# x=pickle.dumps(s)   #Convert the Python Object to Byte Stream
# print(x)              #Output:  b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00\x8c\x06python\x94.'


#Unpickling or Deserialization
# z=pickle.loads(x)  #Convert the Byte Stream to Python Object
# print(z)        #Output:python



#With File Handling
#Pickling or Serialization
# with open("pic.pkl","wb")as f:
#     d=pickle.dump(["a","e","i","o","u"],f)
#
# os.popen("pic.pkl")



#Unpickling or Deserialization
# with open("pic.pkl","rb")as f:
#     d=pickle.load(f)
#     print(d)
