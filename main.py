import telebot
from telebot import types

bot = telebot.TeleBot("747767243:AAGOgVWfKZlldBB-JJj83ZhzdxhBa2o4Fr4")
admin_id = "449016557"
updates = bot.get_updates()
last_update = updates[-1]
last_message = last_update.message
@bot.message_handler(commands=['start'])
def any_msg(message):
    bot.send_message(message.chat.id, "Напишите пост, который хотите видеть на канале")
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Прийняти", callback_data="Accept")
    callback_button1 = types.InlineKeyboardButton(text="Відхилити", callback_data="Delay")
    keyboard.add(callback_button, callback_button1)
    bot.send_message(admin_id, message.text, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "Accept":
        bot.send_message("@Mbotchannel", call.message.text)
        bot.send_message(call.message.chat.id, "Ваше повідомлення було одобрене")
    elif call.data == "Delay":
        bot.send_message(call.message.chat.id, "Ваше повідомлення не було одобрене")












bot.polling(True, 0)