#Add program with reduce function

from functools import reduce

def sum(n1, n2):

    return n1 + n2

nums = [6, 1, 10, 399, 40, 10, 50]

add = reduce(sum, nums)

print(add)

#Mul program with reduce Function

def mul(n1, n2):

    return n1 * n2

mulNum = reduce(mul, nums)

print(mulNum)


#Div program with reduce Function

def div(n1, n2):

    return n2 / n1

divNum = reduce(div, nums)

print(divNum)