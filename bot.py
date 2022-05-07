#Importing Modules
import numpy as nm
import pyautogui
import pytesseract
import time
import telegram_send
import logging
import requests
import cv2

#Importing specific datas
from PIL import ImageGrab
from edit import *
from pygame import mixer

#Telegram API
key = bot_api_token
base_url = "https://api.telegram.org/bot"+key+"/sendMessage?parse_mode=MARKDOWN"

#Logging Everything
logging.basicConfig(filename=("slot.log"), 
					format='%(asctime)s %(message)s', 
					filemode='a') 
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

#Main Loop
def imToString():

	# Path of tesseract executable
	pytesseract.pytesseract.tesseract_cmd = pathoftocr
	message='start'
	# opening the counter file
	with open('counter','r') as f:
		# reading the count of last session
		count=f.read()
	while(True):
		logger.warning("Log No : "+str(count))
		asdf=(message)
		# ImageGrab-To capture the screen image in a loop.
		# Bbox used to capture a specific area.
		cap = pyautogui.screenshot(region=(coordinates))
		logger.info("Screshot Done") 
		# Converted the image to monochrome for it to be easily
		# read by the OCR and obtained the output String.
		tesstr = pytesseract.image_to_string(
				cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
				lang ='eng')
		logger.info("Converted OCR")
		logger.debug(tesstr) 
		message = tesstr[39:][:-2]
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		print("Available date is : " + message + " at " + current_time)
		logger.info("Available date is : " + message + " at " + current_time)
		if asdf == message or message == "":
		    print('The date is same as previous, so no update.')
		    logger.info('The date is same as previous, so no update.')            
		else:
		    print("It's New Date. So, sending message.")
		    logger.info("It's New Date. So, sending message.")
		    chatid = users
		    usercounter=1
		    mixer.init()
		    mixer.music.load('sound.mp3') #Loading Music File
		    mixer.music.play() #Playing Music with Pygame
		    logger.critical("The sound was played.") 
		    for chat_id in chatid:
		        parameters = {"chat_id" : chat_id, "text" : "***"+message+"***"}
		        resp = requests.get(base_url, data = parameters)
		        logger.info(resp.text)
		        print("Sent to user : "+ str(usercounter) + " who is " + chat_id)
		        usercounter = usercounter + 1
		    mixer.music.stop()
		if message == "":
		    logger.critical("The scan was empty.") 
		    message=(asdf)
		print()
		logger.warning("Log No : "+str(count)+ " Ended")
		logger.info("")
		logger.info("")
		count = int(count) + 1
		with open('counter','w') as f:
		    f.write(str(count))
		logger.info("Updated the Log Number.")
		logger.info("")
		logger.info("")
		time.sleep(refreshtime)

# Calling the function
imToString()
