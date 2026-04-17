import telebot
import os

TOKEN = os.getenv("7415148537:AAHC9RSt6Ka4Ip34qTCleHx0YXtfGaERwIA")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['m31'])
def start(message):
    bot.send_message(message.chat.id, "👋 أهلا! البوت خدام")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id, "اكتب أي رسالة وأنا نرد عليك 👍")

@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.send_message(message.chat.id, f"قلت: {message.text}")

print("Bot is running...")
bot.infinity_polling()