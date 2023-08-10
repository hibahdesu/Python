#Validation
import re

email = re.search(r'[A-z0-9\.]+@[A-z0-9]+\.(com|net)', 'hibo@hotmail.com')

if email:

    print('Valid Email')

else: 
    print('Unvalid Email')