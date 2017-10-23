"student".title()

students=[]

def add_student(name, student_id=332):
    """add student name, id as dict
    onto students list
    """
    student = {"name":name, "student_id":student_id}
    students.append(student)

def get_students_titlecase():
    """ make all students' name capitalized
    and print them all
    Note: most used inside print_students_titlecase()
    """
    students_titlecase=[]
    for student in students:
        students_titlecase.append(student['name'].title())

    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


while True:
    add = input("add student info? y for yes, n for no: ")
    if add == "n":
        break
    else:
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_student(student_name, student_id)


print_students_titlecase()
