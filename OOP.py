class Students:
    students_no = 0
    def __init__(self, name , age , courses):
        self.name= name 
        self.age=age
        self.courses=courses
        Students.students_no += 1
    
    def get_name(self):
        return self.name

    def set_name(self, new_name):
         self.name = new_name
    
    def Describe(self):
        print(f'my name is {self.name} , my age is {self.age}, my courses is {self.courses}')
    
    def old(self , num):
      if self.age <= num:
        print("age is not old ")
      else:
        print("age is old")

    
student0 = Students('ahmed', 25, 'CS')
student1 =Students('andrew', 26, 'IT')
student2 =Students('alaa', 28 , 'algorithm')

