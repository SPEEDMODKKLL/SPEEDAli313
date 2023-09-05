import telebot
from telebot import types
import requests

bot = telebot.TeleBot("6342575063:AAEzun8dg5g4QL70xYWT1PEFix1Xh5Bx9w8")

headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': '*/*',
    'Accept-Language': 'ar',
    'Content-Length': '25',
    'User-Agent': 'Nicegram/101 CFNetwork/1404.0.5 Darwin/22.3.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    isrs = types.InlineKeyboardButton(text=" ~ ايديي", callback_data="get_id")
    dragon = types.InlineKeyboardButton(text=" ~ المطور", url="https://t.me/A1X13")
    keyboard.add(isrs)
    keyboard.add(dragon)
    
    bot.send_message(message.chat.id, text="مرحبا بك \n الان فقط قم بارسال ايدي الحساب لمعرفه تاريخ الانشاء ✅", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def t7(message):
    data = '{"telegramId":' + str(message.text) + '}'
    response = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data).json()
    date = response['data']['date']
    if date:
        mej = f"~ الايدي {message.text}\n ~ تاريخ انشاء الحساب {date}"
        bot.reply_to(message, mej)

@bot.callback_query_handler(func=lambda call: call.data == "get_id")
def get_id(call):
    id_message = f"~ ايديك : {call.message.chat.id}"
    bot.send_message(call.message.chat.id, text=id_message)

bot.infinity_polling()