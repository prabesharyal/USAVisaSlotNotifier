# Table of Contents
 1. [Introduction](#1)
    1. [Abot Bot](#1.1)
	2. [Working Principle](#1.2)
	3. [VIP Section](#1.3)
 2. [Get All Variables](#2)
	1. [BOT Token](#2.1)
    2. [Tesseract Location](#2.2)
	3. [Screen Coordinate](#2.3)
	4. [Chat ID's](#2.4)
 3. [Required Softwares](#3)
    1. [Python](#3.1)
		1. [PIPs](#3.1.1)
	2. [Tesseract-OCR](#3.2)
 4. [Deploy](#4)
 5. [License](#lic)

# Read this throughly before deploying the bot: <a name="1"></a>

## What is this bot about?<a name="1.1"></a>
This bot is make specifically for one purpose. That is to monitor visa appointment schedules in your screen and send notification whenever there is change in available dates.

## How does this bot work?<a name="1.2"></a>
> **This bot works in various steps as :**
> - It screenshot your screen's area which is defined in "edit.py".
> - It converts the screenshot toblack and white photo.
> - It scans the photo and converts photo to text using TesseractOCR.
> - Finally, It sends message to the defined (as many as) users in "edit.py".
> - Also, if the message is same as previous  it will skip. 
> - It will also skip empty messages for a reason defined below in **[VIP section](#1.3)**.
> - It prints logs to txt per session. After a session log file is reset.
		



## VIP Section (root of bot)<a name="1.3"></a>

>This bot just captures screen, it doesn't have any access to website of cgi federal. Nor it does other tasks on website. So you've to login and refresh your browser yourself.
>
>Instead refreshig everytime,you can refresh the cgi federal logged in dash page by using the script below.
>
>For that :
> - Press **CTRL+SHIFT+I** and **Ctrl+V** and then **Enter** in that page. 
> - Close that side pane. Now, the pagewill be refreshed every *'N' seconds* as said in the code.

 - javascript :(paste this) <a name="jscript"></a>
 ```
// Start Pasting From Here
function refresh(secs) {
  document.documentElement.innerHTML = '<body style="margin:0px;padding:0px;overflow:hidden"><iframe frameborder="0" style="overflow:hidden;overflow-x:hidden;overflow-y:hidden;height:100%;width:100%;position:absolute;top:0px;left:0px;right:0px;bottom:0px" height="100%" width="100%" id="p" src="' + window.location.href + '"></iframe></body>'
  setInterval(() => document.getElementById('p').src = document.getElementById('p').src, secs * 1000)
}

refresh(10) // 10 here means This page will refresh every 10 seconds
 // paste upto here
 ```

>*While Reloading, sometimes empty reloading page is captured which causes the problem of blank screenshot, and the old value is sent again cause it was new screenshot. But I changed the loop such that empty value is same as old date and hence, only new values are sent.*

> ***Note Section***
> - *Don't open bot.py file if you don't have knowledge.*
> - *Edit variables in edit.py file. That's sufficient.*
		
		
# Get Variables <a name="2"></a>

## Bot Token <a name="2.1"></a>
 - You can get Telegram Bot Token from BotFather bot on telegram.
 
## Tesseract Location <a name="2.2"></a>
 - Go to C:\Program Files or C:\Program Files(X86) and locate Tesseract-OCR and then locate the exact software location.
 - > *First Install it from From [Below](#3.2)*
 
## Screen Coordinate <a name="2.3"></a>
 - Use save.py to locate the screen coordinate if the program can't show any text.
 - You can run this and determine at first whether the correct region is being captured or not.
 
## Getting Chat Ids <a name="2.4"></a>
 - Go to [GroupHelpBot](https://t.me/GroupHelpBot) or [Rose Bot](https://t.me/MissRose_bot) on telegram and type
> - /info @username for public groups/users/channels
> - For private channels or users you have to add bot and users in one same group and send /info command (by mentioning for users).

# Download Softwares and Languages <a name="3"></a>

## Python <a name="3.1"></a>
> Download Python From here :
> - [Python Latest Version](https://www.python.org/downloads/)

> *While installing, tick install **path / environment** variables whatever is given*

### Python Snippets <a name="3.1.1"></a>
- **Install required python snippets using commands below:**
> - `pip install pyautogui`
> - `pip install pytesseract`
> - `pip install numpy`
> - `pip install opencv-python`

- __Install all other missing modules using :__
> - `pip install missing_module_name`

## Tesseract-OCR Executable <a name="3.2"></a>
> Download Tesseract-OCR Executable From here :
> - [Latest Versions Here](https://github.com/UB-Mannheim/tesseract/wiki)
> - [tesseract-ocr-w32-setup-v5.0.1.20220118.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.1.20220118.exe) 32-bit Executable File
> - [tesseract-ocr-w64-setup-v5.0.1.20220118.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe) 64-bit Executable File

# Deploying the bot <a name="4"></a>

- Install Python, Python Snippets and Tesseract-OCR Executable using [above methods](#3)
- Download all files in this repo.
- Insert **[Bot Token](#2.1)**, **[User ID](#2.4)** , **[Tesseract-OCR's Location](#2.2)** in *edit.py* file .
- Open **[CGI Federal Website](https://cgifederal.secure.force.com/)** and Log In using **Dummy Account** and the paste this [script](#jscript)
- **Shift + Right Click** inside the folder where the files are located and select *Open Command Window here*

> Type ***any one*** of the following command on terminal to run bot:
> - `py bot.py`
> - `python bot.py`
> - `python3 bot.py`

- Now, maximize CGI's website if not already. Bot will send updates to groups/users whenever there is change in date.
- Also all logs are saved in logfile.


# License <a name="lic"></a>
> Distributed Under GPL by [@PrabeshAryalNP](https://facebook.com/prabesharyalnp) on [social](https://twitter.com/prabesharyalnp) or [@PrabeshAryal](https://github.com/prabesharyal) on code sites.
		
		