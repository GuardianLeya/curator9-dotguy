import telebot

bot = telebot.TeleBot('6405308551:AAGhHgXHxeQMeE_G-TVLKloiIBSWgDFtuTw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Приходит ежиха к наркологу и говорит: "У меня муж колится" ')


bot.infinity_polling()