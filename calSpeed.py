#Calculating the speed of a function by another function

from time import time

def speed(fun):

    def wrapper():

        start = time()

        fun()

        end = time()

        print(f"The function took about {end - start} to run")

    return wrapper


@speed
def mulNum():

    for num in range(1, 3000):

        print(num)


mulNum()    


