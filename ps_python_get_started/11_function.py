# function without out args and return
def any_questions():
    print("I got a question!")
any_questions()

# function with return
def why_doing_it():
    print("why do you create this study note blog?")
    return "it makes me feel good"

answer = why_doing_it()
answer

# default args
student_list = []
def who_are_you(account_number = 0,gender = "male"):
    name = input("your name here: ")
    if not name:
        name = 'not given'
    student_list.append({account_number: (name, gender)})
who_are_you()

who_are_you(32, gender='female')
student_list

name = "mike" # "mike", " "
print("string as yes") if name else print("string as false")

# positional and named arguments
def fn (a, b, c = 1):
    return a * b + c

print fn (1, 2)                # returns 3, positional and default.
print fn (1, 2, 3)             # returns 5, positional.
print fn (c = 5, b = 2, a = 2) # returns 9, named.
print fn (b = 2, a = 2)        # returns 5, named and default.
print fn (5, c = 2, b = 1)     # returns 7, positional and named.
print fn (8, b = 0)            # returns 1, positional, named and default.


# *args
def test_start_arg(name, *args):
    print(name)
    print(args)

test_start_arg("musk", "is", 45-5, "amazing person!")

# **args
def test_star_star_args(name, **kwargs):
    print(name)
    # print(kwargs['gender'], kwargs['age'], kwargs['career'])
    for k, v in kwargs.items():
        print(k, v)

test_star_star_args("musk", gender="male", age=36, career="tech_entrepreneur")
