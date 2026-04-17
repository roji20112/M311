import telebot
import os

TOKEN = os.getenv("7415148537:AAHC9RSt6Ka4Ip34qTCleHx0YXtfGaERwIA")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت خدام 🔥")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()