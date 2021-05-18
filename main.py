from PIL import Image
from utility import file_manager
import random
import logging
import tweepy
import os

TIFF_FILES_NUMBER = 5 #Set the number of TIFF files

#Auth to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


#Logger configuration
import logging
logging.basicConfig(filename='event.log', level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S")

#Initialize the files that keep tracks of how often a certain file and a square has been used
for i in range(TIFF_FILES_NUMBER):
    file_manager("tracking/img" + str(i) + ".txt", 108)

file_manager("tracking/master.txt", TIFF_FILES_NUMBER) 

#Random file selection
while True: 
    file_number = random.randrange(0,TIFF_FILES_NUMBER)
    file_log = open("tracking/master.txt", "r")
    lines = file_log.readlines()
    file_log.close()
    if(int(lines[file_number]) <= 108):
        new_lines = open("tracking/master.txt", "w")
        for i in range(len(lines)):
            if i == file_number:
                new_lines.write(str(int(lines[i]) + 1) + "\n")
            else:
                new_lines.write(lines[i])
        new_lines.close()
        break


im = Image.open("photos/img" + str(file_number) + ".tif")
logging.info("Selected file is: img" + str(file_number) + ".tif")


#Random square selection 
#There are 108 squre of size 500x500 per image, we select one at random
while True: #Loop checks if a certain square has been selected previously
    squre_number = random.randrange(0,109) #Selects a random integere between 0 and 108, bounds included
    file_log = open("tracking/img" + str(file_number) + ".txt", "r")
    lines= file_log.readlines()
    file_log.close()
    if(int(lines[squre_number]) != 1):
        new_lines = open("tracking/img" + str(file_number) + ".txt", "w")
        for i in range(len(lines)):
            if i == squre_number:
                new_lines.write(str(1) + "\n")
            else:
                new_lines.write(lines[i])
        new_lines.close()
        break

logging.info("Selected grid is: " + str(squre_number))


#Calculcates the top left nad bottom right point of a cropped image
uper_left = (squre_number % 9 * 500, squre_number//9 * 500) #There are 9 images per row
bottom_right = (uper_left[0] + 500, uper_left[1] + 500)
location = uper_left + bottom_right


im1 = im.crop(location) #Crops the image
im1.show() #Displays the image
im1_new = im1.convert("RGB") #Convert from TIFF to JPG
im1_new.save("photos/image.jpg")
im1_new.close()
im1.close()


#Twiter part
try:
    api.verify_credentials()
    logging.info("Authentication OK")
except:
    logging.error("Error during authentication")

try:
    api.update_with_media("photos/image.jpg", "Have a nice day \U0001F64F")
    logging.info("Tweet has been sucessfuly sent")
except:
    logging.error("Error while sending a tweet")

os.remove("photos/image.jpg")

