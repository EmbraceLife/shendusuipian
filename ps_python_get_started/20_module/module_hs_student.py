from module_student import *

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
