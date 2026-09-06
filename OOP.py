class programmers:
    company = "Google"
    def __init__(self , name , salary , id):
        self.name = name
        self.salary = salary
        self.id = id 

imon = programmers("Imon" ,25000 , "00245")
print(imon.name , imon.salary , imon.company)

safin = programmers("Safin" , 29000 , "00247")
print(safin.name , safin.salary , safin.company , safin.id)



class calcutale:
    def __init__(self , n ):
        self.n = n
        # self.name = name

    @staticmethod
    def greet(name):
        print(f"\nHello Mr {name}\n")

    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"The Cube of {self.n} is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n**1/2}")

s = calcutale(4)

s.greet("Imon")

s.square()
s.cube()
s.squareroot()
