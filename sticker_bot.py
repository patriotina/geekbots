import telebot
import constants
import random
import requests
import os
from PIL import Image

bot = telebot.TeleBot(constants.token)

approve = ['Угу', 'Да', 'Подтверждаю', 'Согласен']
question = ['подтверди', 'согласен']

#@bot.message_handler(func=lambda message: True)
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

@bot.message_handler(content_types=['sticker'])
def save_Sticker(message):
    #pprint.pprint(message.json())
    #print(message)
    #print(message.sticker.file_id)
    #bot.send_message(message.chat.id, str(message))
    sticker_info = bot.get_file(message.sticker.file_id)
    downfile = bot.download_file(sticker_info.file_path)
    #print(sticker_info.file_path)
    filename = os.path.basename(sticker_info.file_path)
    with open(filename, 'wb') as nf:
        nf.write(downfile)
        im = Image.open(filename).convert("RGB")
        im.save(filename+".jpg", "jpeg")
        bot.send_sticker(message.chat.id, message.sticker.file_id)


bot.polling()