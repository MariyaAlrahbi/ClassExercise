from Person import Person
from Student import Student
from Teacher import Teacher
def main():
    person_1 = Person("Hamza", 22)
    person_2 = Person("Ali", 27)
    print("how many people? ", Person.num_of_persons)
    print(person_1.num_of_persons)
    print(person_2.name , person_2.age)
    print(Person)
    person_1.run()
    person_3 = Person("Isaa", 31)
    print(Person.num_of_persons)
    print("Age :",person_3.get_age())
  
    #print("Age :",Person.get_age()) # Error
    print("Age :",Person.get_age(person_3)) #OK
    person_4 = Person("Sameer") #use default age
    print(person_4.descrip())
    
    student_1 = Student("Salim", 22, 4)
    teacher_1 = Teacher("Khalid", 40, 12)
    
    print(person_1.say_hi())
    print(student_1 .say_hi())
    print(teacher_1.say_hi())
    
main() # call main