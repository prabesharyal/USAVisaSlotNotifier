import requests, time, os
from dotenv import load_dotenv
load_dotenv()


BOT_API = os.getenv("TELEGRAM_BOT_TOKEN")
CITY = os.getenv("CITY")
VISA = int(os.getenv("VISA"))
RESPECTIVE_CHATS = [
    int(x) for x in os.getenv("CHATS").split(",")
]


# The code is too much modififable as per the use cases.
def get_waittime(CITY):
    resp = requests.get(
        "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid={}&aid=VisaWaitTimesHomePage".format(
            CITY
        )
    )
    if resp.status_code != 200:
        return 404
    the_data = resp.text.replace("\r\n", "").split("|")
    # B1_B2,F_M_J,H_L_O_P_Q, C_D, W_F_M_J, W_H_L_O_P_Q, W_B1_B2,W_C_D=the_data
    """
    All Explanations in Order:
        Interview Required Visitors (B1/B2)
        Interview Required Students/Exchange Visitors (F, M, J)
        Interview Required Petition-Based Temporary Workers (H, L, O, P, Q)
        Interview Required Crew and Transit (C, D, C1/D)	
        Interview Waiver Students/Exchange Visitors (F, M, J)	
        Interview Waiver Petition-Based Temporary Workers (H, L, O, P, Q)
        Interview Waiver Visitors (B1/B2)
        Interview Waiver Crew and Transit (C, D, C1/D)	            
    """
    return the_data  # or F_M_J as per your use_case


def send_telegram_message(chat_id: int, message: str, BOT_Hash=BOT_API):
    api_URL = (
        "https://api.telegram.org/bot" + BOT_Hash + "/sendMessage?parse_mode=MARKDOWN"
    )
    parameters = {
        "chat_id": chat_id,
        "text": "❗️❗️❗️ ALERT ❗️❗️❗️\n"
        + "\t Visa Appointment Available in : \n"
        + "\t\t\t***"
        + message
        + "***",
    }
    send_message = requests.get(api_URL, data=parameters)
    response_json = send_message.json()
    if send_message.status_code == 200:
        print("Sent '{}' to {}".format(message, response_json['result']['chat']['first_name']))
        return True
    else:
        return False


def initialize_logic():
    previous_date = ""
    while True:
        new_date = get_waittime(CITY)
        if new_date != 404 and new_date != previous_date:
            for chats in RESPECTIVE_CHATS:
                send_telegram_message(chat_id=chats, message=new_date[VISA])
        elif new_date == 404:
            raise "SiteError: Couldn't Get Date From the main Site"
        time.sleep(1)
        previous_date=new_date


def main():
    print("Visa Slot Notifier is Running !")
    try:
        initialize_logic()
    except Exception as e:
        print("Some error occurred.")
        print(e)

if __name__ == '__main__':
    main()
