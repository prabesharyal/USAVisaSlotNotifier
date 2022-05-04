# Read this throughly before implementing the Logic:

## What is this bot about?
This bot is make specifically for one purpose. That is to monitor visa appointment schedules in your screen and send notification whenever there is change in available dates.

## How does this bot work?
> **This bot works in various steps as :
>		- It screenshot your screen's area which is defined in "edit.py".
>		- It converts the screenshot toblack and white photo.
>		- It scans the photo and converts photo to text using TesseractOCR.
>		- Finally, It sends message to the defined (as many as) users in "edit.py".
>		- Also, if the message is same as previous  it will skip. 
>		- It will also skip empty messages for a reason defined below in **VIP section**.
>		- It prints logs to txt per session. After a session log file is reset.
		



## VIP Section (root of bot)

		> This bot just captures screen, it doesn't have any access to website of cgi federal.So you've to refresh your browser yourself.

		Instead refreshig everytime,you can refresh the cgi federal logged in dash page by using the script below.
		Press **CTRL+SHIFT+I** and **Ctrl+V** and then **Enter** in that page. 
		Close that side pane. Now, the pagewill be refreshed every *'N' seconds* as said in the code.
		
		javascript :(paste this)
		(Start from double slash and end after UP)
		``` // Start Pasting From Here
		function refresh(secs) {
  document.documentElement.innerHTML = '<body style="margin:0px;padding:0px;overflow:hidden"><iframe frameborder="0" style="overflow:hidden;overflow-x:hidden;overflow-y:hidden;height:100%;width:100%;position:absolute;top:0px;left:0px;right:0px;bottom:0px" height="100%" width="100%" id="p" src="' + window.location.href + '"></iframe></body>'
  setInterval(() => document.getElementById('p').src = document.getElementById('p').src, secs * 1000)
}

refresh(10) // 10 here means This page will refresh every 10 seconds
 // paste upto here UP ```
 
 >***Note Section***
>		-*Don't open botv2.py file if you don't have knowledge.*
>		-*Edit variables in edit.py file. That's sufficient.*
		
		

***Distributed Under GPL by @PrabeshAryalNP on social or @PrabeshAryal on code sites.***
		
		