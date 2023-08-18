from Person import Person
class Student(Person):
   def __init__(self, name, age, academic_year):
     super().__init__(name, age) #how to use parent constructor
     self.academic_year = academic_year
   def say_hi(self):
      return f"Hello {self.name} as Student"