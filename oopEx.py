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


#Ex 2:
#OOP Example

#Class

class Users:

    not_names = ['Hell', 'Fuck', 'Shit', 'Hhaa', 'God']

    user_numbers = 0

    def __init__(self, user_name, user_last, user_age, user_gender):

        self.name = user_name

        self.last = user_last

        self.age = user_age

        self.gender = user_gender

        Users.user_numbers += 1

    def full_name(self):

        if self.name in Users.not_names:

            raise ValueError('Name is not allowed')
        
        else:

            return f'{self.name} {self.last}'    
    
    def title(self):

        if self.name in Users.not_names:

            raise ValueError('Name is not allowed')
        
        else:

            if  self.gender == 'Male':

                return f'Hello Mr.{self.name}'
        
            elif self.gender == 'Female':

                return f'Hello Mrs.{self.name}'
        
            else: 

                return f'Hello {self.name}'

        
        
    def uage(self):

        return f'{self.age} years old'    
    
    def full_details(self):

        return f'{self.title()} your age {self.uage()} is '
    
    def del_user(self):

        Users.user_numbers -=1

        return f'User {self.name} Deleted'


print(Users.user_numbers)

user_1 = Users('Jane', 'Johnson', 23, 'Male')

user_2 = Users('David', 'Joseph', 29, 'Male')

user_3 = Users('Tanaka', 'Naoki', 25, 'Male')   

user_4 = Users('Sakura', 'Horishima', 26, 'Female')  

# user_5 = Users('Shit', 'Horishima', 26, 'Female') 

print(user_1.full_name())

print(user_1.title())

print(user_4.full_name())

print(user_4.title())

print(user_1.uage())

print(user_1.full_details())

print(user_2.full_details())

print(user_3.full_details())

print(user_4.full_details())

# print(user_5.full_name())

print(Users.user_numbers)

print(user_3.del_user())

print(Users.user_numbers)
