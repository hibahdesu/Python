#########################
#Prining a list with map function
#########################

def listItems(staff):

    return f"- {staff.strip().capitalize()}"

subList = ['Manzana ', ' naranja', 'Pan ', 'Agua', 'Leche', 'Cafe', 'Te']

data = map(listItems, subList)

for item in (data): 

    print(item)

