class Student():
    pass


stu1 = Student()
stu2 = Student()

# methods and attrs to overwrite
stu1.__init__
stu1.__repr__

############################
students = []

class Student:
    def add_student(self, name, student_id=332):
        student = {"name":name, "student_id":student_id}
        students.append(student)

student = Student()
student.add_student("Mark") # mutable list change value
student

students


############################
students = []

class Student:
    def __init__(self, name, student_id=332):
        student = {"name":name, "student_id":student_id}
        students.append(student)

jack = Student("Jack", 213)
students

############################
students = []

class Student:
    def __init__(self, name, student_id=332):
        student = {"name":name, "student_id":student_id}
        students.append(student)

    def __str__(self): # self refer to instance or object
        return "this is an instance!"

    def __repr__(self):
        return "I am an instance"
jack = Student("Jack", 213)
students
print(jack)

####################################

students = []

class Student:
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self): # self refer to instance or object
        return "Student: %s" % self.name

    def __repr__(self):
        return "I am %s" % self.name

    def capitalize_title(self):
        return self.name.title()

jack = Student("jack", 213)
students
print(jack)
jack.name
n = jack.capitalize_title()
jack.name

####################################
students = []

class Student:
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self): # self refer to instance or object
        return "Student: %s" % self.name

    def __repr__(self):
        return "I am %s" % self.name

    def capitalize_title(self):
        self.name = self.name.title()

jack = Student("jack", 213)
students
print(jack)
jack.name
jack.capitalize_title() # 改变global variable值的复杂方法
jack.name

####################################
students = []

class Student:

    school_name = "No3 middle school"
    # class attributes used for all objects

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self): # self refer to instance or object
        return "Student: %s" % self.name

    def __repr__(self):
        return "I am %s" % self.name

    def capitalize_title(self):
        self.name = self.name.title()


jack = Student("jack ma", 213)
jack.school_name
Student.school_name


####################################
students = []

class Student:

    school_name = "No3 middle school"
    # class attributes used for all objects

jack = Student()
jack.school_name
