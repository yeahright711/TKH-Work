nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


evens1=[]
odds1= []

for num in nums:
    if num % 2 == 0:
        evens1.append(num)
    else:
        odds1.append(num)

print(evens1)
print(odds1)

odds1 = [var for var in nums if var % 2 == 1]
evens2 = [var for var in nums if var % 2 == 0]
print(evens2)
print(odds1)

foo = "hello world"
z = foo.split()
print("z", z)


def polynom(x):
    return x ** 2 + 5