import telebot
import constants
import random
import requests
import os
from PIL import Image
import zipfile


bot = telebot.TeleBot(constants.token)

approve = ['Угу', 'Да', 'Подтверждаю', 'Согласен']
question = ['подтверди', 'согласен']

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
        stickzip = zipfile.ZipFile(r'stickers.zip', 'a')
        stickzip.write(filename+".jpg")
        stickzip.close()
        bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(commands=['tozip'])
def to_zip(message):
    with open('stickers.zip', 'rb') as file:
        bot.send_document(message.chat.id, file)
    
    @bot.send_message(message.chat.id, 'zipppppme')


bot.polling()