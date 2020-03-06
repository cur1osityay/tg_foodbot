import telebot

TOKEN = '995973993:AAH3KmGshMXTdWhBcK0G56mYizH_v9BYAFc' 
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=['text'])
def start_message(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
