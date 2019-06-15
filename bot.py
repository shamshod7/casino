# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
from telebot import types
from emoji import emojize
from pymongo import MongoClient
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

admins=[379168159]
games={-1001398455154}

client1=os.environ['database']
client=MongoClient(client1)
db=client.chlenomer
users=db.ids_people


@bot.message_handler(commands=['begin'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, 'Крутим барабан...\n'+'🕐')
            bot.send_message(m.chat.id, 'Крутим барабан...\n'+'🕐')
            bot.send_message(m.chat.id, 'Крутим барабан...\n'+'🕐')
            bot.send_message(m.chat.id, 'Крутим барабан...\n'+'🕐')
            bot.send_message(m.chat.id, 'Yutdiz...\n'+'🕐')
            
                 
@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, 'Коэффициенты ставок:\n'+
                     '1-15, 16-30: *1.5*\n'+
                     '1-5, 6-10, 11-15, 16-20, 21-25, 26-30: *5*\n'+
                     '0: *25*', parse_mode='markdown')
            

@bot.message_handler(commands=['roll'])
def roll(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
          if games[m.chat.id]['began']==1:
            x=random.randint(0,30)
            msg=bot.send_message(m.chat.id, 'Крутим барабан...\n'+'🕐')
            t=threading.Timer(0.1, roll2, args=[m.chat.id, msg.message_id])
            t.start()
             
        
        
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)

while True:
    from requests.exceptions import ReadTimeout
    from requests.exceptions import ConnectionError
    try:
        bot.polling()
    except(ReadTimeout, ConnectionError):
        pass


