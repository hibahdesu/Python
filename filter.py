#Using the filter Function to look for some employees 

def emp(name):

    return name.startswith('J')

empEmp = ['Jane', 'Sakura', 'Jhon', 'Jasmen', 'David', 'Rose', 'Remasa', 'Tanaka']

empWithJ = filter(emp, empEmp)

for empJ in empWithJ:
    
    print(empJ)