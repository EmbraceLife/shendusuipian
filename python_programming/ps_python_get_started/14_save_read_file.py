
##########################################
import numpy as np

# global variables
students=[] # mutable, 无需输入与输出
students_info=None # 需要输出赋值

def add_student(name, student_id=332):
    """add student name, id as dict
    onto students list
    """
    student = {"name":name.title(), "student_id":student_id}
    students.append(student)# mutable, 无需输入与输出


def print_students_info():
    """ save into numpy array, print
    """

    names = []
    ids = []
    for student in students:
        names.append(student['name'])
        ids.append(student['student_id'])
    names = np.array(names).reshape(-1,1)
    ids = np.array(ids).reshape(-1,1)
    students_new = np.concatenate((names, ids), axis=1)
    if type(students_info) == type(None): # if students_info: or if students_info.exist
        students_full = students_new
    else:
        students_full = np.concatenate((students_info, students_new), axis=0)

    print(students_full)
    return students_full # 需要输出赋值

def save_file():
    """
    append an existing file
    只取出姓名，只保存姓名，一个名字一行
    """

    try:
        np.save("students.npy", students_info)
    except Exception as e:
        print("Could not save it")
        print("error message: \n", e)

def read_file():

    try:
        students_load = np.load("students.npy")
    except Exception as e:
        print("Could not read files")
        print("error message: \n", e)
        students_load = None
        print("read_file finished running ------")
    print(students_load)
    return students_load

students_info = read_file() # load info, and print

while True:
    add = input("add student info? y for yes, n for no: ")
    if add == "n":
        break
    else:
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_student(student_name, student_id)

students_info = print_students_info()
save_file()
