from telegram.bot import Bot
from time import sleep
import requests, os, sys

API_KEY = str(os.getenv('TELEGRAM_BOT_API_KEY'))
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
SLEEP_CHECK_REBOOT_REQUIRED = int(os.getenv('SLEEP_CHECK_REBOOT_REQUIRED'))

def test():
    return "test"

# Check if the Telegram API-Key is valid (make sure that Token isn't used by another script)
def check_API_KEY():
    api_url = 'https://api.telegram.org/bot' + API_KEY + '/getUpdates'
    response = requests.get(api_url, verify=True)
    if response.status_code != 200:
        return False
    else:
        return True

def main():
    if check_API_KEY() == True:
        print("Valid API-Key")
    else:
        print("API_KEY is not valid. Please check your API_KEY!")
        sys.exit(1)

# Bot send method
def send(_text):
    bot.send_message(chat_id=CHAT_ID, text=_text)

def check_reboot_required():
    while True:
        try:
            reboot_required_file = "/var/bot/run/reboot-required.pkgs"
            if os.path.isfile(reboot_required_file) == True:
                file = open(reboot_required_file, "r")
                data = file.read()
                file.close()
                send("Reboot is required due to\n" + data)
            sleep(SLEEP_CHECK_REBOOT_REQUIRED)
        except Exception as exception:
            send("Error while checking for reboot required: " + str(exception))

if __name__ == "__main__":
    main()
    bot = Bot(API_KEY)
    check_reboot_required()
