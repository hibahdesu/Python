#Application about the database 
import sqlite3

db = sqlite3.connect('appDb.db')

cr = db.cursor()

#Create table
cr.execute('CREATE TABLE if not exists users(name TEXT, skill TEXT, progress INTEGER, id INTEGER)')

#user id
id = 1

#save and close method
def saveAndClose():

    #commit
    db.commit()

    #close
    db.close()

    print('Connection in closed now.')



#User message
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

    cr.execute(f'SELECT * FROM users WHERE id = "{id}"')

    resule = cr.fetchall()

    # print(f'You have {len(resule)} skills')

    print(resule)

    if len(resule) > 0:

        print(f'You have {len(resule)} skills')

        print('Skills with progress: ')

    else:
        print('You have no skills, try to add some please.')    

    for sk in resule:

        print(f'The skill is {sk[1]}')

        print(f'--The progress is {sk[2]}%')

    saveAndClose()

    

def add():

    skill = input('Write the skill: ').strip().capitalize()

    cr.execute(f'SELECT skill FROM users WHERE skill = "{skill}" WHERE id = "{id}"')

    resule = cr.fetchone()

    # print(resule)

    if (resule == None):

        print("The skill does not exist. You can add it.") 

        level = input('Write the progress of your skill: ').strip()

        cr.execute(f'INSERT INTO users(name, skill, progress, id) values("{user_name}", "{skill}", "{level}", "{id}")')
        

    else:

        print("This skill already exists. You cannot add it again.")

    # print(f'You have {len(resule)} skills')

    

    saveAndClose()


def delete():

    skill = input('Write the skill: ').strip().capitalize()

    cr.execute(f'DELETE FROM users WHERE skill = "{skill}" AND id = "{id}"')

    saveAndClose()

    

def update():

    skill = input('Write the skill: ').strip().capitalize()

    level = input('Write the progress of your new skill: ').strip()

    cr.execute(f'UPDATE users SET progress = "{level}" WHERE skill = "{skill}" AND id = "{id}"')

    saveAndClose()



#Check the commands the user types
if user_chooses in commands:

    # print(f'{user_chooses} Right Command')

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
        print('App Is Closed.')

        saveAndClose()

else:

    print(f'{user_chooses} Wrong Command, try again please.') 


