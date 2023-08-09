######################
#Pillow
######################
#Important Link:
#https://pillow.readthedocs.io/en/stable/#installation
#--https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class
######################


from PIL import Image

#First Open the image
img = Image.open(r'C:\Users\habob\Downloads\python\pillow\p.jpg')

#Show the image
# img.show()

#Cut the image
box = (40, 80, 250, 380)

myImage = img.crop(box)

#Show the new image
myImage.show()

#Convert the image to black and white
blackImage = myImage.convert('L')

blackImage.show()

