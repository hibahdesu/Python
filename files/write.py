#Write a File

writeFile = open(r"C:\Users\habob\Downloads\python\files\write.txt", "w")

writeFile.write("Hello, This file for writting\n")

writeFile.write("--Second, we gonna hav a lot of fun now")

myList2 = ['Manzana\n', 'Naranja\n', 'Pan\n', 'Agua\n', 'Leche\n', 'Cafe\n', 'Te\n']

writeFile.writelines(f'\nThe list for the supermarket is: \n')

writeFile.writelines(myList2)