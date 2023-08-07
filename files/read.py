#Files
#--Read Files

readFile = open(r"C:\Users\habob\Downloads\python\files\read.txt", "r")

print(readFile)

print(readFile.read())

print(readFile.name)

print(readFile.mode)

print(readFile.encoding)

print(readFile.readline())

for word in readFile:

    print(word)

    
readFile.close()