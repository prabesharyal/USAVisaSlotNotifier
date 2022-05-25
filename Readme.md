# Table of Contents
 1. [Introduction](#1)
    1. [Abot Bot](#1.1)
	2. [Working Principle](#1.2)
 2. [Get All Variables](#2)
	1. [BOT Token](#2.1)
    2. [Session Cookies](#2.2)
	3. [Chat ID's](#2.4)
 3. [Required Softwares](#3)
    1. [Python](#3.1)
		1. [PIPs](#3.1.1)
	2. [JSON Cookie Extension](#3.2)
 4. [Deploy](#4)
 5. [License](#lic)

# Read this throughly before deploying the bot: <a name="1"></a>

## What is this bot about?<a name="1.1"></a>
This bot is make specifically for one purpose. That is to monitor visa appointment schedules in your screen and notify you in your PC and in Telegram whenever there is change in available dates.

## How does this bot work?<a name="1.2"></a>
> **This bot works in various steps as :**
> - It loads CGI_Federal's page
> - Injects your session cookies and log in.
> - The appointment class is extracted and only Day and Dates are Noted.
> - Finally, It sends message to the defined (as many as) users in "edit.py".
> - Also, if the date is same as previous  it will skip. 
> - It prints logs to txt per session. After a session log file is not reset.
		

> ***Note Section***
> - *Don't open bot.py file if you don't have knowledge.*
> - *Edit variables in edit.py file. That's sufficient.*
		
		
# Get Variables <a name="2"></a>

## Bot Token <a name="2.1"></a>
 - You can get Telegram Bot Token from BotFather bot on telegram.
 
## Getting Session Cookies <a name="2.2"></a>
- Paste Your Session Cookies in JSON, Here's an example of format, paste your own.
> - [This Extension](#3.2) works fine, but you'll need to replace "*true*" & "*false*" by  **True** and **False** Respectively .
> - Sample Cookie: ```[{
    "name": "CookieConsentPolicy",
    "value": "0:1",
    "domain": "cgifederal.secure.force.com",
    "path": "/",
    "expires": 1230456.25,
    "httpOnly": False,
    "secure": False
  }, {similar},{similar}
  ]```

 
## Getting Chat Ids <a name="2.4"></a>
 - Go to [GroupHelpBot](https://t.me/GroupHelpBot) or [Rose Bot](https://t.me/MissRose_bot) on telegram and type
> - /info @username for public groups/users/channels
> - For private channels or users you have to add bot and users in one same group and send /info command (by mentioning for users


# Download Softwares and Languages <a name="3"></a>

## Python <a name="3.1"></a>
> Download Python From here :
> - [Python Latest Version](https://www.python.org/downloads/)

> *While installing, tick install **path / environment** variables whatever is given*

### Python Snippets <a name="3.1.1"></a>
- **Install required python snippets using commands below:**
> - `pip3 install selenium`
> - `pip3 install webdriver-manager`
> - `pip install pygame`

- __Install all other missing modules using :__
> - `pip install missing_module_name`

## JSON Cookie Extension <a name="3.2"></a>
> Download Extension From here :
> - [Install Extension From Here](https://bit.ly/38PRX6f)

# Deploying the bot <a name="4"></a>

- Install Python, Python Snippets and Tesseract-OCR Executable using [above methods](#3)
- Download all files in this repo.
- Insert **[Bot Token](#2.1)**, **[User ID](#2.4)** , **[Cookie](#2.2)** in *edit.py* file .
- Open **[CGI Federal Website](https://cgifederal.secure.force.com/)** and Log In using **Dummy Account** and use this [extension](#3.2)
- Replace **true** with **True** and **false** with **False** in the cookies file. Now, paste it in same format in **edit.py** file.

> Type ***any one*** of the following command on terminal to run bot:
> - `py bot.py`
> - `python bot.py`
> - `python3 bot.py`

- Now, minimize browser and do whatever you want. Bot will send updates to groups/users whenever there is change in date.
- Also all logs are saved in logfile.


# License <a name="lic"></a>
> Distributed Under GPL by [@PrabeshAryalNP](https://facebook.com/prabesharyalnp) on [social](https://twitter.com/prabesharyalnp) or [@PrabeshAryal](https://github.com/prabesharyal) on code sites.
		
		