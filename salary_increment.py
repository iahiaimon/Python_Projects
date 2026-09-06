class Employee:
    # def __init__(self , salary , increment):
    #     self.salary = salary
    #     self.increment = increment

    salary = 220
    increment = 30

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self , salary):
        self.increment = ((salary/self.salary)-1) *100


e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 270
print(e.increment)
    