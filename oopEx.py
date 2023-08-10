#OOP Example

#Class

class User:
    def __init__(self, user_name, user_last, user_age):

        self.name = user_name

        self.last = user_last

        self.age = user_age

user_one = User('Jane', 'Johnson', 23)

user_two = User('David', 'Joseph', 29)

user_three = User('Tanaka', 'Naoki', 25)   

print(f'The user name is: {user_one.name} {user_one.last}, and his age is: {user_one.age}')

print(f'The user name is: {user_two.name} {user_two.last}, and his age is: {user_two.age}')

print(f'The user name is: {user_three.name} {user_three.last}, and his age is: {user_three.age}')

