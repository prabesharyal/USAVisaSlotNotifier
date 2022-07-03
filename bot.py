#Importing Modules
from lib2to3.pytree import Base
import time
import logging
import requests


#Importing Submodules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pygame import mixer
from edit import *

#Clearing Problems in Logs
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Browser Files
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Telegram API
key = bot_api_token
base_url = "https://api.telegram.org/bot"+key+"/sendMessage?parse_mode=MARKDOWN"

#Logging Everything
logging.basicConfig(filename=("slot.log"), 
					format='%(asctime)s %(message)s', 
					filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

#Loading Page For First Time
driver.get("https://cgifederal.secure.force.com")
driver.implicitly_wait(3)

#Logging In 
for cookies in cookies:
    driver.add_cookie(cookies)
driver.implicitly_wait(2)
driver.get("https://cgifederal.secure.force.com/applicanthome")
driver.refresh()
time.sleep(5)

class label(Exception): pass  # declare a label
#Main Loop
def imToString():
	message='start'
	# opening the counter file
	with open('counter','r') as f:
		# reading the count of last session
		count=f.read()
	while(True):
		logger.warning("Log No : "+str(count))
		asdf=(message)
			#Finding Available Date
		while(True):	
			try:
				try:
					element = driver.find_element(By.CLASS_NAME, value="leftPanelText")
				except Exception as err:
					print("Refreshing page in 10 seconds cause element not found... ")
					time.sleep(10)
					print("Refreshing now .....")
					driver.refresh()
					continue
				availabledate = element.text
				message = availabledate[31:][:-1]
				t = time.localtime()
				current_time = time.strftime("%H:%M:%S", t)
				print("Available date is : " + message + " at " + current_time)
				logger.info("Available date is : " + message + " at " + current_time)
				if asdf == message:
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
					time.sleep(5)
					mixer.music.stop()
				print()		#Back to Main Previous Loop
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
				driver.refresh()
				break
			except BaseException as err:
				print(err)
				print("Probably the dummy account got banned. Till I create new, Bot is Down")
				chatid = users
				usercounter=1
				logger.critical("The class wasn't found") 
				for chat_id in chatid:
					parameters = {"chat_id" : chat_id, "text" : "***"+"Probably the dummy account got banned. Till I create new, Bot is Down"+"***"}
					resp = requests.get(base_url, data = parameters)
					logger.info(resp.text)
					print("Sent to user : "+ str(usercounter) + " who is " + chat_id)
					usercounter = usercounter + 1
				#Closing Browser
				driver.close()
				quit()

# Calling the function
imToString()
