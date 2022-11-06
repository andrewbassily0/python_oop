from datetime import date

class Students:

    students_no = 0
    def __init__(self, name , age):
        self.name= name 
        self.age= age
        Students.students_no += 1

    def describe(self):
        return (f"my name is {self.name} , my age is {self.age}")
        
    @classmethod
    def years( cls, name , birthYear ):
        return cls(name , date.today().year - birthYear)

class Pizza :
    def __init__(self, ingredients):
         self.ingredients = ingredients

    @classmethod 
    def margrita(cls):
        return cls(["mozarila" , "tomato" , "onions"])

    @classmethod 
    def veg(cls):
        return cls(["tomato" , "onions" , "salsa"])

    def des(self):
        print(f"my pizza ingredients {self.ingredients}")

pizza1= Pizza.margrita()
pizza2= Pizza.veg()
pizza3= Pizza(["beef" , "shawrma" , "strips"])

print(pizza3.des())