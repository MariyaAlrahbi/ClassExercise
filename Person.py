class Person:
    num_of_persons = 0 # static variable
    def __init__(self, name, age = 20): #constructor
        #Initialize name and age attributes.
      self.name = name
      self.age = age
      Person.num_of_persons +=1
    def descrip(self):
       return f"Person name is {self.name} and {self.age} years old"
    def set_name(self, new_name):
       self.__name = new_name
    def get_name(self): #What happen if not write self
       return self.name
    def set_age(self, new_age):
       self.__age = new_age
    def get_age(self):
       return self.age
    def say_hi(self):
      return f"Hello {self.name} as Person"
    def run(self):
       print(self.name + " is running.")
    def talk(self):
       print(self.name.title() + " is talking!")