#Students Loop

students = {
    'Maria': {
        'Math': '99%',
        'English': '100%',
        'History':'85%',
        'Chemistry': '95%',
        'Physics': '90%'
    },
    'Sally': {
        'Math': '90%',
        'English': '80%',
        'History':'80%',
        'Chemistry': '90%',
        'Physics': '80%'
    },
    'Sakura': {
        'Math': '85%',
        'English': '90%',
        'History':'80%',
        'Chemistry': '85%',
        'Physics': '90%'
    },
    'Jane': {
        'Math': '93%',
        'English': '90%',
        'History':'80%',
        'Chemistry': '90%',
        'Physics': '80%'
    }
}

for name, sub in students.items(): 
    print(f'Student\'s name is: {name}')

    for suSub, suPro in sub.items():
        print(f'  -In {suSub} got: {suPro}')
