#Add Numbers by a function

def add(num1, num2, num3):

    if type(num1) != int or type(num2) != int or type(num3) != int:
        print("Please enter only integers")

    else:
        print(num1 + num2 + num3)

add(9, 39, 19)

