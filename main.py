import os
from flask import Flask, send_from_directory
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = os.environ.get("8757151441:AAF3ob4wrTwlfOWGi-QHP-u6er9qlr_0Jz8")
WEB_APP_URL = os.environ.get("WEB_APP_URL")

bot = telebot.TeleBot(8757151441:AAF3ob4wrTwlfOWGi-QHP-u6er9qlr_0Jz8)
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(
        text="🎬 Open Video App", 
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    markup.add(web_app_button)
    bot.reply_to(message, "স্বাগতম! ভিডিও দেখতে নিচের বাটনে চাপ দিন:", reply_markup=markup)

if __name__ == '__main__':
    from threading import Thread
    def run_bot():
        bot.infinity_polling()
    
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
  
