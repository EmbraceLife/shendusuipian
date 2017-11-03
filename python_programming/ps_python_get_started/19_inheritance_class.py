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

class HighSchoolStudent(Student): # 继承全部，不overwrite
    pass

jack = HighSchoolStudent("jack")
jack
print(jack)
jack.capitalize_title()
jack.name
jack.school_name

#######################################################
students = []
class HighSchoolStudent(Student): # 继承全部，不overwrite
    def __init__(self, age, name, student_id=233):
        self.age = age
        super().__init__(name, student_id)

    def __str__(self): # self refer to instance or object
        print("I am overwriting __str__ again")
        print(self.name)
        return self.name # must have a return

    def capitalize_title(self):
        print("previously: self.name == %s" % self.name)
        super().capitalize_title()
        print("now, self.name == %s" % self.name)


jack = HighSchoolStudent(18, "qq", 232)
jack.age
jack.name
jack.student_id
print(jack)
jack.capitalize_title()
jack
