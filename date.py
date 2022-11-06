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


student0=Students("ahmed", 25)
student1=Students.years("andrew", 1995 )
print(student1.describe())