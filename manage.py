import telebot
from requests import get
bot = telebot.TeleBot("5215240244:AAGXGOCvfxvT9YfaCC-Aal9oyXxxdpDs8ew")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Im NATASHKA CHEBURASHKA")


@bot.message_handler(func=lambda m: True)
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text == 'Hello':
        bot.send_message(message.chat.id, 'O vi iz anglii')
    elif message.text == 'Ты кто?':
        bot.send_message(message.chat.id, 'Я чебурашка')
    elif message.text == 'Скинь фотку':
        bot.send_message(message.chat.id, 'Я дед инсайд')
        bot.send_photo(message.chat.id, get("https://s5o.ru/storage/simple/cyber/edt/77/e5/f8/6a/cyberef474b35d9c.png").content)
        bot.send_message(message.chat.id, 'А ты дед инсайд ?')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, 'Красава')
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Говна ответ')
    elif message.text == 'Скинь песню':
        audio = open('AS.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)


bot.polling()
