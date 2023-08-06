#First Ex with range
num = range(1, 50)

for n in num: 
    print(n)


#Second Ex with Dic
lang = {
    'Arabic': '100%',
    'English': '90%',
    'Spanish': '40%',
    'Japanese': '40%',
    'Turkish': '20%',
    'Germany': '20%',
    'Korean': '10%',
}

for l in lang :
    if (lang[l] == '100%'):
        print(f'Your level in {l} is {lang[l]}, is native.')
    elif (lang[l] == '90%' or lang[l] == '80%'):
        print(f'Your level in {l} is {lang[l]}, is Advance.')
    elif (lang[l] == '70%' or lang[l] == '60%'):  
        print(f'Your level in {l} is {lang[l]}, is Intermediate.')
    elif (lang[l] == '50%' or lang[l] == '40%'):  
        print(f'Your level in {l} is {lang[l]}, is Advanced Beginner.') 
    else:
        print(f'Your level in {l} is {lang[l]}, is Beginner.') 