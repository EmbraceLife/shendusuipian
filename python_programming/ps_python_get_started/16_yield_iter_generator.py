def simple_generator_function():
    yield 1
    yield 2
    yield 3

for value in simple_generator_function():
    print(value)

our_generator = simple_generator_function()
next(our_generator)
next(our_generator)
next(our_generator)
next(our_generator)


def simple_generator_function():
    for i in range(10):
        yield i*2


for value in simple_generator_function():
    print(value)



our_generator = simple_generator_function()

for i in range(12):
    print("number %i: " %i)
    try:
        print(next(our_generator))
    except StopIteration:
        print("no more left")
        break
