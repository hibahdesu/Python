#Convert a number to a binary number with a function

lists = [2, 10, 49, 199, 39, 19, 100, 299, 300, 0, 1]

def binNum(num):

    for b in num: 

        print(bin(b))


print(binNum(lists))


print(sum(lists))

print(sum(lists, 2))


# range(start, end, step)
x = list(range(10))

print(x)

print(binNum(x))

y = list(range(0, 40, 2))

print(y)

print(binNum(y))