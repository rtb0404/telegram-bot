import telebot

bot = telebot.TeleBot("1008970858:AAFb5snJEiD5Yw0ey1keuyDbGBZSsrGEtmA")
keyboard1 = telebot.types.ReplyKeyboardMarkup()


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    print(message)

bot.polling()