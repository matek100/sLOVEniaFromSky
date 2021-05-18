# sLOVEniaFromSky
Small twitter bot that utomatically tweets an aerial photo of Slovenia once per day.

##Twitter bots based on this code:
[SloveniaFromSky](https://twitter.com/SloveniaSky)

Feel free to message me if you want me to include your bot here.

## Installation guide
1. Put all of your photos into the photos folder. Make sure that that they are enumerated and fallow the format img0.tif.

2. Cropping and image processing only works for the exact photo sizes and format that [GURS](https://www.gov.si/drzavni-organi/organi-v-sestavi/geodetska-uprava/) provides. That is 4500px x 6000px. 
3. In controller.sh configure the path to itself.

4. In main.py configure that tokens required for Twitter API.

5. Run ```pip install -r requirements.txt``` to install dependencies.

6. On UNIX environments start the script by using the command ```./controller.sh```.
By default the bot will post a photo once per day between 8:00 and 20:59. This can be changed by configuring the controller.sh file.  


[Guide on how to get access token for the bot account](https://medium.com/geekculture/how-to-create-multiple-bots-with-a-single-twitter-developer-account-529eaba6a576)
, be sure to enable 3-legged OAuth.
