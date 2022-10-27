#Author: Andrew Apollo 

import students

def main():

    student = students.Student("628001" ,"Andrew J Apollo")

    print("Student ID=", student.get_id(), ", name=", student.get_name(), ", credits=", student.get_credits(), ", GPA=", student.get_gpa())

    student.print_student()


    gcis_123 = students.Course("GCIS-123", 4, "B+")
    gcis_123.print_course()
    nssa_102 = students.Course("NSSA-102", 3, "A")
    nssa_102.print_course()

    student.add_course(gcis_123)
    student.add_course(nssa_102)

    student.add_course(students.Course("GCIS-123", 4, "B+"))
    student.add_course(students.Course("NSSA-102", 3, "A"))

    print("GPA", student.get_gpa())

main()