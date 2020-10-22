'''def multi(numbers):
    i = 1
    print(numbers)
    print(type(numbers))
    for x in numbers:
        i = i * x
    return i
a = (1, 2, 3, 4, 5)
print(multi(a))
print(multi((1, 2, 3, 4, 5)))
#print(multi(1, 2, 3, 4, 5))'''

def multi(*numbers):
    i = 1
    print(numbers)
    print(type(numbers))
    for x in numbers:
        i = i * x
    return i

print(multi(1, 2, 3, 4, 5))

