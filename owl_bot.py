import telebot
import constants
import random


bot = telebot.TeleBot(constants.token)

approve = ['Угу', 'Да', 'Подтверждаю', 'Согласен']
question = ['подтверди', 'согласен']

@bot.message_handler(content_types=["text"])
def sendHi(message):
    ok = False
    for q in question:
        if q in message.text.lower():
            ok = True
            break
    if ok:
        bot.send_message(message.chat.id, random.choice(approve))
    else:
        bot.send_message(message.chat.id, "не согласен!")

bot.polling()