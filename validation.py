#Validation
import re

#search()
email = re.search(r'[A-z0-9\.]+@[A-z0-9]+\.(com|net)', 'hibo@hotmail.com')

if email:

    print('Valid Email')

    print(email.span())

    print(email.string)

    print(email.group())

else: 
    print('Invalid Email')


#findall()    
userEmail = input('Type your email, Please ')

emails = re.findall(r'[A-z0-9\.]+@[A-z0-9]+\.com|net', userEmail)

users = []

if emails != []:

    users.append(emails)

    print('Valid Email.\nAdded Succefuly')

else:
    print("Invalid Email")

for email in users:

    print(emails)    
