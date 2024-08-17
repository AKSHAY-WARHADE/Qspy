from abc import ABC,abstractmethod
# class Sample:
#     @abstractmethod                # In python we don't have any interfaces concept but we can call abstract method as Interface
#     def spam(self):                #The methods declared with decorator'@abstractmethod' are called as abstract method   whereas simple functions are called
#         print("Spam")                 #CONCRATE Method
# c=Sample()                            #Like this Classes with abstract method are called as Abstract Classes otherwise Simple class is called
# c.spam()                              #CONCRATE Class

# class Sample(ABC):
#     @abstractmethod
#     def spam(self):
#         ...
# class One(Sample):
#     def spam(self):
#         print("It is a Spam")
# c=One()
# c.spam()



# class Bank(ABC):
#     @abstractmethod
#     def balance(self):
#         ...
#     @abstractmethod
#     def deposit(self,amount):
#         ...
#     @abstractmethod
#     def withdrawal(self,amount):
#         ...
#
# class ATM(Bank):
#     def __init__(self,b_name,amount):
#         self.b_name=b_name
#         self.amount=amount
#
#     def balance(self):
#         print(f"The availabe balance is {self.amount}")
#
#     def deposit(self,amount):
#         self.amount += amount
#         print(f"After deposit the balance is {self.amount}")
#
#     def withdrawal(self,amount):
#         self.amount-=amount
#         print(f"After Withdrawal The Amount is {self.amount}")
#
# a=ATM("SBI",23000)
# a.balance()
# a.deposit(2300)
# a.withdrawal(1234)




# class Flight(ABC):
#     @abstractmethod
#     def __init__(self,platform_name):
#         ...
#     @abstractmethod
#     def airline(self,airline_name):
#         ...
#     @abstractmethod
#     def location(self,origin,destination):
#         ...
#     @abstractmethod
#     def datetime(self,date,time):
#         ...
#     @abstractmethod
#     def passenger(self,passenger):
#         ...
#
# class Booking(Flight):
#     def __init__(self,platform_name):
#         self.p_name=platform_name
#         print(f"The Flight Booking Platform is : {self.p_name}")
#
#     def airline(self,airline_name):
#         self.a_name=airline_name
#         print(f"The Airline Name is : {self.a_name} ")
#
#     def location(self,origin,destination):
#         self.origin=origin
#         self.destination=destination
#         print(f"The Origin is :{self.origin}\n The Destination is : {self.destination}")
#
#     def datetime(self,date,time):
#         self.date=date
#         self.time=time
#         print(f"The Time is : {self.time} \n Journey Date is : {self.date}")
#
#     def passenger(self,passenger):
#         self.pas=passenger
#         print(f"The  No of Passenger is : {self.pas}")
#
# f=Booking("Make_My_Trip")
# f.airline("Air_India")
# f.location("Mumbai","Pune")
# f.datetime("12-08-2024","12:56")
# f.passenger(3)






#BookMyShow:
class Movie(ABC):
    def __init__(self,city):
        ...
    @abstractmethod
    def theater(self):
        ...
    @abstractmethod
    def film(self):
        ...
    @abstractmethod
    def time(self):
        ...
    @abstractmethod
    def seat_type(self):
        ...
    @abstractmethod
    def ticket(self):
        ...
    @abstractmethod
    def snacks(self):
        ...
    @abstractmethod
    def final(self):
        ...


class Book(Movie):
    def __init__(self,city):
        self.city=city
        print(f"Your Selected Region is : {self.city}")
    def theater(self):
        self.t_list=["INOX","PVR","City Pride","Miraj"]
        print(self.t_list)
        self.t_name=str(input("Enter a Theater Name"))
        if self.t_name in self.t_list:
            print(f"Your selected Theater : {self.t_name}")
        else:
            print(f"The Theater your are looking for is currently not available")
    def film(self):
        self.f_list=["Bad Newz","Deadpool","Kalki","Sarfira"]
        print(self.f_list)
        self.f_name=str(input("Select a Movie from Above"))
        if self.f_name in self.f_list:
            print(f"Your Selected Movie is : {self.f_name}")
        else:
            print("The movie your are looking for is currently not available")
    def time(self):
        self.time1=["12pm","2pm","5pm","8pm","10:30pm"]
        self.time2=["2pm","5pm","8pm","11pm"]
        if self.t_name in ["Miraj","City Pride"]:
            print(f"Available Time Slots : {self.time1}")
        else:
            print(f"Available Time Slots : {self.time2}")
        self.t_slot=str(input("Enter The Time Slot :"))
        if self.t_slot in ["12pm","2pm","11pm","8pm"]:
            print(f"Your Selected Time Slot : {self.t_slot} and it is available")
        else:
            print("Your Selected Time Slot is Housefull\nPlease choose another slot")

    def seat_type(self):
        self.s_list=["Platinum","Lounge","Gold"]
        print(self.s_list)
        self.s_type=str(input("Enter The Seat Type From Above"))

    def ticket(self):
        self.p_list={"Platinum":550,"Gold":300,"Lounge":1000}
        print(self.p_list)
        self.t_type=str(input("Enter The Ticket Class:"))
        self.t_count=int(input("Enter the no of tickets"))
        if self.t_type in self.p_list:
            if self.t_type=="Platinum":
                self.t_price=self.t_count*550
            elif self.t_type=="Gold":
                self.t_price=self.t_count*300
            else:
                self.t_price=self.t_count*1000
        else:
            print("Enter The valid ticket class")

    def snacks(self):
        self.choice=str(input("Want to take Snacks?"))
        if self.choice=="yes" or  "y":
            self.snack_list=["Popcorn","Chicken Nugget","Pizza","Burger"]
            print(f"List of available items:\n{self.snack_list}")
            self.snack_type=str(input("Enter The Item name:"))
            self.s_cont=int(input("Enter the no items"))
            if self.snack_type in self.snack_list:
                if self.snack_type=="Popcorn":
                    self.snack_price=self.s_cont*200
                elif self.snack_type=="Chicken Nugget":
                    self.snack_price = self.s_cont * 400
                elif self.snack_type=="Pizza":
                    self.snack_price = self.s_cont * 350
                else:
                    self.snack_price = self.s_cont * 250

    def final(self):
        self.eff_price=self.snack_price+self.t_price
        print(f"Your Effective Ticket Price is : {self.eff_price}")
        a=int(input("Please Pay The Price Kindly by entering it here"))
        if a==self.eff_price:
            print("You Have Booked The Ticket Successfully")




a=Book("Pune")
a.theater()
a.film()
a.time()
a.seat_type()
a.ticket()
a.final()








