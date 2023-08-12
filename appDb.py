#Application about the database 
import sqlite3

message = """
What do you want to do in your profile:
's': Show all skills
'a': Add new a skill
'd': Delete a skill
'u': update a skill
'q': quit the app
Choose one to do:
"""

user_name = input('Type your name: ').strip().capitalize()

user_chooses = input(message).strip().lower()

print(user_name)

print(user_chooses)

#Commands
commands = ['s', 'a', 'd', 'u', 'q']

#Define the methods
def show():

    pass

def add():

    pass

def delete():

    pass

def update():

    pass

def quit():

    pass

#Check the commands the user types
if user_chooses in commands:

    print(f'{user_chooses} Right Command')

    if user_chooses == 's':

        #Show All Skills
        show()

    elif user_chooses == 'a':

        #Add a new Skill
        add()

    elif user_chooses == 'd':

        #Delete an existing skill
        delete()

    elif user_chooses == 'u':

        #Update an existing skill
        update()


    else: 

        #Quit Program
        quit()
        print('App Closed.')

else:

    print(f'{user_chooses} Wrong Command, try again please.') 

