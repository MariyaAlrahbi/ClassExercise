from Person import Person
class Teacher(Person):
      def __init__(self, name, age, experience_years):
         super().__init__(name, age)
         self.experience_years = experience_years
      def say_hi(self):
       return f"Hello {self.name} as Teacher"