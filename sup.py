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