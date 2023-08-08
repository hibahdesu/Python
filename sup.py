#Using enumerate function

supList = ['ringo', 'banana', 'mikan', 'ichigo']

organize = enumerate(supList, 1)

for items in organize:
    
    print(items)


#reverse Function

print(reversed(supList))

reveList = reversed(supList)

for rev in reveList:

    print(rev)

import termcolor
import pyfiglet

# print(dir(termcolor))

print(pyfiglet.figlet_format('Hibah Sindi'))

print(termcolor.colored(pyfiglet.figlet_format('Hibah Sindi'), color="Yellow"))
