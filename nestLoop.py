#Nested Loop Ex

employs = {
    'Mohammed': {
        'HTML': '100%',
        'CSS': '95%',
        'JS': '80%'
    },
    'John': {
        'Python': '100%',
        'PHP': '60%',
        'Java': '70%'
    },
    'Jane': {
        'C++': '40%',
        'Ruby on Rails': '20%',
        '.NET Core': '30%'
    },
    'Maria': {
        'SQL Server 2016/2017': '80%',
        'PostgreSQL': '90%',
        'MongoDB': '70%',
        'Python': '95%'
    }
}

#Checking 
print(employs['Jane'])
print(employs['Jane']['C++'])

for emp in employs: 
    #Looping through the keys of a dictionary
    print(f'The Employee\'s name is {emp}')

    for skill in employs[emp]:
        print(f'  -Skill is: {skill}, level is: {employs[emp][skill]}')