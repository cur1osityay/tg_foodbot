  
import telebot
import random
 
from telebot import types
 
TOKEN = 'токен бота' 
bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Пошук рецептів")
    item2 = types.KeyboardButton("Усі рецепти")
    item3 = types.KeyboardButton("Збережені рецепти")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, в якому зібрано дуже багато рецептів".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def ui_message(message):
    if message.chat.type == 'private':
        if message.text == 'Пошук рецептів':
            bot.send_message(message.chat.id, 'Функція недоступна')
            if message.text == 'Збережені рецепти':

            	markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Усі рецепти", callback_data='all_rcp')
            item2 = types.InlineKeyboardButton("Додати рецепт", callback_data='add_rcp')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Збережені рецепти:', reply_markup=markup)

        elif message.text == 'Усі рецепти':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Рецепт 1", callback_data='rcp1')
            item2 = types.InlineKeyboardButton("Рецепт 2", callback_data='rcp2')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Ось твої рецепти', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю що відповісти 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    rec_1 = open('recipes/recipe_1.txt', 'r')
    rec_2 = open('recipes/recipe_2.txt', 'r')
    try:
        if call.message:
            if call.data == 'rcp1':
                bot.send_message(call.message.chat.id, rec_1)
            elif call.data == 'rcp2':
                bot.send_message(call.message.chat.id, rec_2)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Усі рецепти",
                reply_markup=None)

 @bot.callback_query_handler(func=lambda call: True)
def callback_inline_2(call):
	#Зв'язок з базою даних
    try:
        if call.message:
            if call.data == 'all_recp':
                bot.send_message(call.message.chat.id, 'Усі твої рецепти:')
            elif call.data == 'add_recp':
                bot.send_message(call.message.chat.id, 'Додати по назві')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Збережені рецепти",
                reply_markup=None)

 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)