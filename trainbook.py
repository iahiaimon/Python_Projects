from random import randint

class Bus:

    def __init__(self , busNo):
        self.busNo = busNo

    def book_ticket(self ,  fro , to ):
        print(f"The Ticket of this bus (Bus no {self.busNo}) is booked from {fro} to {to}")

    def get_status(self):
        print(f"The Bus will be running on time from ")

    def get_fare(self , fro , to ):
        print(f"The fare from {fro} to {to} is {randint(150 , 1050)}")

a = Bus(9175)
a.book_ticket("Dhaka" , "Baguna")
a.get_status()
a.get_fare("Dhaka" , "Baguna")