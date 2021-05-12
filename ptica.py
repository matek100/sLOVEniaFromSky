from PIL import Image
import random

while True: #Loop selects a random file
    file_number = random.randrange(0,100)
    file_log = open("master.txt", "r")
    line = file_log.seek(file_number).readline()
    file_log.close()
    if(line != 1):
        file_log = open("master.txt", "w")
        #TO DO: 
        #LINE THAT CHANGES 0 to 1
        break

im = Image.open("img" + file_number + ".tif")


#There are 108 squre of size 500x500 per image, we select one at random
while True: #Loop checks if a certain square has been selected previously
    squre_number = random.randrange(0,109) #Selects a random integere between 0 and 108, bounds included
    file_log = open("img1.txt", "r")
    line = file_log.seek(squre_number).readline()
    file_log.close()
    if(line != 1):
        #TO DO: 
        #LINE THAT CHANGES 0 to 1
        break

uper_left = (squre_number % 9 * 500, squre_number//9 * 500) #There are 9 images per row
bottom_right = (uper_left[0] + 500, uper_left[1] + 500)
location = uper_left + bottom_right


im1 = im.crop(location)
im1.show()
