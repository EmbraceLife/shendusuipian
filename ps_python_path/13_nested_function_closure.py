def get_students():

    students = ['mike', 'kenny']

    def get_students_titlecase():
        students_titlecase=[]
        for student in students:
            students_titlecase.append(student.title())
        return students_titlecase+lst

    lst = ["yes or no"]

    students_titlecase_names = get_students_titlecase()

    print(students_titlecase_names)

get_students()
