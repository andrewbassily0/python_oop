class Person:
    def __init__(self , name , age):
        self.name = name
        self.age =age

    def des(self):
        return  f" my name is {self.name} my age is {self.age}"

class Women(Person):
    gender ="female"
    num = 0
    def __init__(self, name, age, hair ):
        super().__init__(name, age)
        self.hair = hair

    def des(self):
        string = super().des()
        return string + f" my voice is {self.hair} , my gender is {self.gender}"

class Man(Person):
    gender ="male"
    num = 0
    def __init__(self, name, age, voice ):
        super().__init__(name, age)
        self.voice = voice

    def des(self):
        string = super().des()
        return string + f" my voice is {self.voice} , my gender is {self.gender}"




my = Women("gina","27","soft")
print(Women.des())
print(Women.num)

