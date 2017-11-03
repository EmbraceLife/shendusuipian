def convert(s):
    x = int(s)
    return x

convert("3")
convert("e3") # ValueError

def convert(s):
    try:
        x = int(s)
        print("Succeed!")
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x
convert("3")
convert("e3")
convert([1,2,3])

def convert(s):
    try:
        x = int(s)
        print("Succeed!")
    except ValueError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("Conversion failed!")
        x = -1
    return x
convert([1,2,3])

def convert(s):
    try:
        x = int(s)
        print("Succeed!")
    except (ValueError, TypeError):
        print("Conversion failed!")
        x = -1
convert([1,2,3])

# IndentationError, SyntaxError, NameError not to catch inside try_except, to be corrected when programming not running

def convert(s):
    try:
        return int(s)

    except (ValueError, TypeError) as e:
        print("Conversion failed! due to %s" % str(e))
        return -1
convert([1,2,3])

# raise error again
def convert(s):
    try:
        return int(s)

    except (ValueError, TypeError) as e:
        print("Conversion failed! due to %s" % str(e))
    raise
convert([1,2,3])


##########################
# exceptions as part of API
def sqrt(x):
    guess = x
    i = 0
    while guess*guess != x and i < 20:
        guess = (guess + x / guess)/2.0
        i += 1
    return guess

sqrt(9)
sqrt(2)
sqrt(-1)

def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print("can't computer sqrt of negative number")
    print("acknowledge error but continue ")
main()

# raise 自制的Error Message
def sqrt(x):
    if x < 0:
        raise ValueError("can't compute sqrt of %d" %x)
    guess = x
    i = 0
    while guess*guess != x and i < 20:
        guess = (guess + x / guess)/2.0
        i += 1
    return guess
sqrt(-1)

import sys
def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ValueError as e:
        # print(e, file=sys.stderr)
        print(str(e))
    print("acknowledge error but continue ")
main()

# IndexError
l = [1,4,2]
l[4]
# ValueError
int("python")
# KeyError
dct = {"py":3.6, "pytorch":1.2}
dct["pyto"]
# suggest not to catch TypeError

# try...finally
import sys
def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)
    finally:
        print("finally will run no matter what!")
main()
