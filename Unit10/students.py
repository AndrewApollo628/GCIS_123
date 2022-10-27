#Author: Andrew Apollo 

#Class activity 10.1.2
class Student:
    #Class activity 10.2.4
    __slots__ = ["id","name","credits","gpa"]

    #Class Activity 10.2.2
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0

#Class activity 10.1.5
def print_student(a_student):
    print("Student: ", a_student.id , ", " , a_student.name, ", " , a_student.credits, ", " , a_student.gpa)


def main():

    #Class activity 10.1.3
    '''
    student1 = Student()
    student2 = Student()

    #Class activty 10.1.4
    student1.id = '123-ABC'
    student1.name = 'Farris'
    student1.credits = 24
    student1.gpa = 2.7

    #Class activity 10.1.5
    print_student(student1)
    print_student(student2)
    '''

    #Class actiivty 10.2.3
    student1 = Student("ABC123" , "Ferris")
    student2 = Student("DEF456" , "Sarah")

    print_student(student1)
    print_student(student2)
main()