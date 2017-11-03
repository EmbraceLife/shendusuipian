# use of with to prevent memory leak
from urllib.request import urlopen
with urlopen("http://sixty-north.com/c/t.txt") as story:
    story_words = [] # global variable
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)

# python 02_module.py
# python -m pdb 02_module.py
# import 02_module (won't accepted)

#################################
# turn implictly

def func_no_return():
    print("no return")

w = func_no_return()
w is None

def func_return_nothing():
    print("return nothing")
    return

w = func_return_nothing()
w is None

def func_return_more():
    print("return nothing")
    return (1, 2), "two things"

a, b = func_return_more()
a
b
