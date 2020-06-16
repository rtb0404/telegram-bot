import telebot
from telebot import  types

bot = telebot.TeleBot("1296802303:AAGlPGJNxELhkJX4FZ4to8XzrDunCP-csCQ")
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row("Dunyo xabarlari", "Uzbekiston xabarlari", "Makrabimiz xabarlari")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Salom yengi xabarlar kerak emasmi?', reply_markup=keyboard1)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMSXuC1Zx_fs5InXy8LSvvKyNInYJEAAn4FAAL6C7YIVcp3d5Hfk7gaBA')




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Dunyo xabarlari":
        bot.send_message(message.chat.id, "Xozircha bungi xabar yo'q")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMPXuCz-ykDi8RpU-iyKrqqEfcoDaUAArwCAAJjK-IJ-4zaoKwb82caBA')

    elif message.text== "Uzbekiston xabarlari":
        button2 = types.KeyboardButton("Fudbol")

        bot.send_message(message.chat.id, "Xabarlar yoq")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMUXuC2ChhL00pjU_hTrKEUz9M6IUcAAnkFAAL6C7YIhEgx7zSTo84aBA')
    elif message.text== "Makrabimiz xabarlari":
        button3 = types.KeyboardButton("Maktab yangiliklari")
        bot.send_message(message.chat.id, "Maktabimiz sentyabr oyidan boshlanadi")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMTXuC2AAG7tNc6zNOxT9uIoFk_hRGkAALUAgACYyviCRGgFX76sFV6GgQ')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMQXuC0BsUgR6lqKxzzv6VqQ1ZlwsUAAhIDAAJjK-IJkw6POAaUJz0aBA')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row("ddd", "www", "ggg")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Salom yengi xabarlar kerak emasmi?', reply_markup=keyboard2)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMSXuC1Zx_fs5InXy8LSvvKyNInYJEAAn4FAAL6C7YIVcp3d5Hfk7gaBA')



@bot.message_handler(content_types=["text"])
def menu(message):
    if message.text== "ddd":
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton("COVID19")
        button2 = types.KeyboardButton("Fudbol")
        button3 = types.KeyboardButton("Maktab yangiliklari")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Xabarlarni tanlang", reply_markup=markup)
    if message == "COVID19":
        bot.send_message(message.chat.id, "Serverimizda nosozlik!!")
    elif message == "Fudbol":
        bot.send_message(message.chat.id, "Serverimizda nosozlik!!")
    elif message== "Maktab yangiliklari":
        bot.send_message(message.chat.id, "Serverimizda nosozlik!!")

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, interval=0)