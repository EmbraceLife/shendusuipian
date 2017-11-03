students=[]

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
