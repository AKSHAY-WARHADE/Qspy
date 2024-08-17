import pandas as pd

# print(pd.__version__)
#Series
# a=[1,2,3,4,5]
# x=pd.Series(a)
# x=pd.Series(a,index=("a","e","i","o","u"),name="series1")
# x=pd.Series(a,index=("a","e","i","o","u"),name="series1",dtype=complex)
# print(x)




#DataFrame
a=["Akshay","Rahul","Vaibhav","Mansi","Yashu","Mahima","Rushab"]
b=["Pune","Mumbai","Bengluru","Chennai","Delhi","Hyd","Vizag"]
c=[56080,87100,36009,76022,26501,49340,12300]
d=[23,34,21,45,67,89,34]
e=["Development","QA","IT","Testing","Analysis","Production","Management"]

details=pd.DataFrame({"Name":a,"Location":b,"Salary":c,"Age":d,"Department":e})
#print(details)

#Head
# h=details.head()
# print(h)

#Tail
# t=details.tail(3)
# print(t)

#Single Column
# print(details["Name"])

#Multiple Columns
# print(details[["Name","Age","Location"]])

#Slicing
# print(details[0:5:2])
# print(details[::-1])

#iterows
# for i in details.iterrows():
#     print(list(i)) #list
#     print(i) #tuple

#shape
# print(details.shape)

#describe
# print(details.describe())

#Loc
#print(details.loc[2])

# print(details.loc[0,["Name","Department"]])

# print(details.loc[3:5])

# print(details.loc[2:5,["Age","Salary"]])

# print(details)


#Bank Credentials
First_Name=["Akshay","Shreya","Bhushan","Ajay","Nitish","Vedshree","Sarvagya","Partiksha","Krushna","Harshada"]
Last_Name=["Warhade","Dahake","Khunkar","Wankhede","Singh","Nildawar","Mishra","Bhos","Tale","Bhalekar"]
Mobile_No=[8390229872,7654321902,7028919384,7854284909,8786452334,3409873456,8762460972,4562340987,5678543209,7845320187]
Email=["akshay@gmail.com","shreyu@rediffmail.com","bhushan@gmail.com","ajay@yahoo.com","nitish@github.com","veda@amazon.com","sarvagya@rediffmail.com","pratiksha@hotmail.com","krushna@gmail.com","harshada@hotmail.com"]
Username=["Akshay2001","Shreyu2002","Bhushan2000","Ajay1999","Nitish2000","Veda2003","Sarvagya2001","Pratiksha1999","Krushna2002","Harshada2001"]
Bank=["SBI","CNRB","BOB","HDFC","Axis","BOB","HSBC","Axis","HDFC","SBI"]
Account_Type=["Savings","Current","Fixed","Loan","Joint","Joint","Current","Loan","Reserved","Savings"]
Balance=[5678,878675,3456,8756,34567,2345,98765,1234567,3456987,67898]
PAN=["AGLPW9522C","SHRE6754D","DFGHJ6789K","XCVGB9876W","RTYUI1234S","IHGVKJ3409N","QSCED1093M","OKNED1946B","EUTGV7834T","PLMCS0342B"]
Age=[23,22,56,78,32,56,89,20,76,40]

bank=pd.DataFrame({"First_Name":First_Name,"Last_Name":Last_Name,"Mobile_Number":Mobile_No,"Email_Id":Email,"Username":Username,"Bank_Name":Bank,"Account_Type":Account_Type,"Balance_Amount":Balance,"PAN_Number":PAN,"Age":Age})
pd.options.display.width=None
pd.options.display.max_columns=None
pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',100)
# print(bank)
#
# print(bank.shape)


#print(bank.loc[5])
# #it will display the particular row

#print(bank.loc[4,["First_Name","Age"]])
# #It will display the particular record with only the specified columns

#print(bank.loc[2:9:2])
# It will do slicing on rows #
# In loc  stop index Is INCLUDED

#print(bank.loc[2:7,"First_Name"])
#print(bank.loc[0:5:1,["First_Name","Last_Name","Bank_Name"]])
#It will display the particular no of rows with the specified column name


#print(bank.loc[4:10,"First_Name":"Account_Type"])
#It will the the no of rows and it will also display the columns specified in the range format



#ILOC Here the stop index is EXCLUDED

#print(bank.iloc[3,1])
#It will display the the particular record with the of the specified row number and column number

#print(bank.iloc[0:5,5:11])
#It will display the multiple records by specifying the range of row number as well as column numbers

#print(bank.iloc[0:7,4])
# It will display the multiple records specified in range for a particular column number mentioned

#print(bank.iloc[[2,4,7,9]])
#it will display the no of rows specified


#print(bank.iloc[:,[0,1,4,7]])
#it will display  the all records for specified column numbers


#print(bank.iloc[0:5,[0,1,2,3]])
#it will display ht e no of record specified in the range and the specified column numbers


# a=pd.read_csv(r"C:\Users\LENOVO\Desktop\DataSets\ICC Mens T20 Worldcup.csv")
# print(a)