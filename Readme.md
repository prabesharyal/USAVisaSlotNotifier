

# Table of Contents
 1. [Introduction](#1)
    1. [Abot Bot](#1.1)
 2. [Get All Variables](#2)
    1. [BOT Token](#2.1)
    2. [City Code](#2.2)
    3. [VISA Type](#2.3)
    4. [Chat ID's](#2.4)
 3. [Required Softwares](#3)
    1. [Python](#3.1)
		1. [PIPs](#3.1.1)
 4. [Deploy](#4)
 5. [License](#lic)

# Read this throughly before deploying the bot: <a name="1"></a>

## What is this bot about?<a name="1.1"></a>
This bot is make specifically for one purpose. That is to monitor visa appointment schedules in your screen and notify you in Telegram whenever there is change in available dates.

# Get Variables <a name="2"></a>

## Bot Token <a name="2.1"></a>
- You can get Telegram Bot Token from BotFather bot on telegram.

## Getting City Code <a name="2.2"></a>
You've to get your city code from [this site](https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/wait-times.html) by inspecting network headers.
>- First visit site
>- Open Devleoper Tools and switch to network
>- Search your city name
>- Click the last item on network tab, Examine the Request URL
>- `https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P50&aid=VisaWaitTimesHomePage`, Here the `P50` is your city code for city 'Chisinau'. 

## Visa Type <a name="2.3"></a>
You need to know what type of visa date to be notified with. The corresponding number is your visa type.
>- `0` for Interview Required Visitors (B1/B2)
>- `1` for Interview Required Students/Exchange Visitors (F, M, J)
>- `2` for Interview Required Petition-Based Temporary Workers (H, L, O, P, Q)
>- `3` for Interview Required Crew and Transit (C, D, C1/D)	
>- `4` for Interview Waiver Students/Exchange Visitors (F, M, J)	
>- `5` for Interview Waiver Petition-Based Temporary Workers (H, L, O, P, Q)
>- `6` for Interview Waiver Visitors (B1/B2)
>- `7` for Interview Waiver Crew and Transit (C, D, C1/D)	 
## Getting Chat Ids <a name="2.4"></a>
 - Go to [GroupHelpBot](https://t.me/GroupHelpBot) or [Rose Bot](https://t.me/MissRose_bot) on telegram and type
> - `/info @username` for public groups/users/channels
> - For private channels or users you have to add bot and users in one same group and send /info command (by mentioning for users)


# Download Softwares and Languages <a name="3"></a>

## Python <a name="3.1"></a>
> Download Python From here :
> - [Python Latest Version](https://www.python.org/downloads/)

> *While installing, tick install **path / environment** variables whatever is given*

### Python Snippets <a name="3.1.1"></a>
- **Install required python snippets using commands below:**
> - `pip3 install -r requirements.txt`

- __Install all other missing modules using :__
> - `pip install missing_module_name`


# Deploying the bot <a name="4"></a>

- Install Python, Python Snippets using [above methods](#3)
- Download all files in this repo.
- Insert **[Bot Token](#2.1)**, **[User ID](#2.4)** in *SAMPLE.env* file and rename it to `.env`.

> Type ***one*** of the following command on terminal to run bot:
> - `py main.py`
> - `python main.py`
> - `python3 main.py`


# License <a name="lic"></a>
> Distributed Under GPL by [@PrabeshAryalNP](https://facebook.com/prabesharyalnp) on [social](https://twitter.com/prabesharyalnp) or [@PrabeshAryal](https://github.com/prabesharyal) on code sites.
		
		