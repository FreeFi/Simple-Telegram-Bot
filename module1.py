
import telebot

bot = telebot.TeleBot("5847794927:AAHhV6SMQoAVJDFrZHjxWs8rJ9Nb0TBpcXE")

@bot.message_handler(commands=['Старт', 'помощь'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как дела?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()