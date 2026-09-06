class vector2d:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f"The vector of a and b is {self.a*self.b}")

class vector3d(vector2d):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def show(self):
        print(f"The vector of a , b and c is {self.a*self.b*self.c}")

o = vector2d(10, 20)
o.show()
p = vector3d(10, 20, 30)
p.show()


class animal:
    def __init__(self):
        pass

class pet(animal):
    def __init__(self):
        super().__init__()

class dog(pet):
    def __init__(self , bark):
        super().__init__()
        self.bark = bark

    def sound(self):
        print(f"The dog barks {self.bark}")

d = dog("Bhow Bhow")
d.sound()