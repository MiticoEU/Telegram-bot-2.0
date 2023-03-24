import telegram
import time
import Angebote
import Constanten as KEYS
from datetime import datetime, timedelta
from telegram.ext import Updater
import logging

# Setze deine Telegram-Bot-Token hier ein
bot_token = KEYS.API_KEY

# Erstelle einen Telegram-Bot
bot = telegram.Bot(token=bot_token)

# Bestimme die Zeit, zu der die Funktion einmal am Tag aufgerufen werden soll
today = datetime.now()
run_time = datetime(today.year, today.month, today.day, 17, 0, 0) + timedelta(days=1)

# Konfiguriere das Logging-Modul
logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


# Definiere die Funktion, die einmal am Tag aufgerufen werden soll


def daily_function():
    check_result()

# Definiere die Funktion, die aufgerufen werden soll, wenn sich das Ergebnis ändert


def changed_function():
    result = Angebote.rewe()
    if result:
        bot.send_message(chat_id=KEYS.chat_id, text=result)
        logging.info('Angebot gesendet')
    else:
        logging.info('Keine Angebote gefunden')



# Definiere die Funktion, die das Ergebnis überprüft


def check_result():
    new_result = Angebote.rewe()
    with open("last_result.txt", "r", encoding='utf-8') as infile:
        old_result = infile.read()
    if new_result != old_result:
        with open("last_result.txt", "w", encoding='utf-8') as outfile:
            outfile.write(new_result)
        changed_function()


# Schleife, um die Funktionen automatisch aufzurufen
while True:
    current_time = datetime.now()
    if current_time >= run_time:
        daily_function()
        # Aktualisiere die Zeit für den nächsten Aufruf
        run_time = datetime(current_time.year, current_time.month,
                            current_time.day, 17, 0, 0) + timedelta(days=1)
    time.sleep(60)  # Warte eine Minute, bevor die Schleife wiederholt wird
