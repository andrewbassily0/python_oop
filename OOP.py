class Students:
    
    students_no = 0
    def __init__(self, name , age , courses):
        self.__name= name 
        self.__age= age
        self.__courses= courses
        Students.students_no += 1
    
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
         self.__name = new_name
    
    def get_age(self):
        return self.__age

    def set(self, num):
        self.__age = num
    
    def get_courses(self):
        return self.__courses

    def set(self, new):
        self.__courses = new

    def Describe(self):
        print(f'my name is {self.__name} , my age is {self.__age}, my courses is {self.__courses}')
    
    def old(self , num):
      if self.__age <= num:
        print("age is not old ")
      else:
        print("age is old")

    
student0 = Students('ahmed', 25, 'CS')



