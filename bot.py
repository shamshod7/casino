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

admins=[713258449]
games={-1001445331185}

client1=os.environ['database']
client=MongoClient(client1)
db=client.chlenomer
users=db.ids_people


@bot.message_handler(commands=['70'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *☠️Hech narsa*', parse_mode='markdown')

@bot.message_handler(commands=['69'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')

@bot.message_handler(commands=['68'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql Toshi*', parse_mode='markdown')
                    

@bot.message_handler(commands=['67'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🛩Samalyot bileti*', parse_mode='markdown')
    
@bot.message_handler(commands=['66'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧬Mutatsiya*', parse_mode='markdown')
    
@bot.message_handler(commands=['65'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚞Poyezd bileti*', parse_mode='markdown')
    
@bot.message_handler(commands=['64'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *☠️Hech narsa*', parse_mode='markdown')
    
@bot.message_handler(commands=['63'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *💸Pul*', parse_mode='markdown')
    
@bot.message_handler(commands=['62'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🍗Ovqat*', parse_mode='markdown')
    
@bot.message_handler(commands=['61'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
    
@bot.message_handler(commands=['60'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql Toshi*', parse_mode='markdown')
    
@bot.message_handler(commands=['59'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🤹‍♂️Sirkchi darajasi*', parse_mode='markdown')
    
@bot.message_handler(commands=['58'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔑Kalit*', parse_mode='markdown')
    
@bot.message_handler(commands=['57'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
    
@bot.message_handler(commands=['56'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *⌛️Soat*', parse_mode='markdown')
    
@bot.message_handler(commands=['55'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *💸Pul*', parse_mode='markdown')
    
@bot.message_handler(commands=['54'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🛩Samalyot bileti*', parse_mode='markdown')
    
@bot.message_handler(commands=['53'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🐎Ot*', parse_mode='markdown')
    
@bot.message_handler(commands=['52'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚞Poyezd bileti*', parse_mode='markdown')
    
@bot.message_handler(commands=['51'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚀Raketa*', parse_mode='markdown')
    
@bot.message_handler(commands=['50'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🎛Gidrometr*', parse_mode='markdown')
    
@bot.message_handler(commands=['49'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
    
@bot.message_handler(commands=['48'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚁Vertalyot*', parse_mode='markdown')
    
@bot.message_handler(commands=['47'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql Toshi*', parse_mode='markdown')
    
@bot.message_handler(commands=['46'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *♟Shaxmat ustasi darajasi*', parse_mode='markdown')
 
@bot.message_handler(commands=['45'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *💸Pul*', parse_mode='markdown')
    
@bot.message_handler(commands=['44'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
    
@bot.message_handler(commands=['43'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *⌛️Soat*', parse_mode='markdown')
    
@bot.message_handler(commands=['42'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚞Poyezd bileti*', parse_mode='markdown')
    
@bot.message_handler(commands=['41'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔑Kalit*', parse_mode='markdown')
    
@bot.message_handler(commands=['40'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *♟Shaxmat ustasi darajasi*', parse_mode='markdown')
    
@bot.message_handler(commands=['39'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql Toshi*', parse_mode='markdown')
    
@bot.message_handler(commands=['38'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
    
@bot.message_handler(commands=['37'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql Toshi*', parse_mode='markdown')
    
@bot.message_handler(commands=['36'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🎛Gidrometr*', parse_mode='markdown')
    
@bot.message_handler(commands=['35'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚁Vertalyot*', parse_mode='markdown')
    
@bot.message_handler(commands=['34'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
    
@bot.message_handler(commands=['33'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *💸Pul*', parse_mode='markdown')
    
@bot.message_handler(commands=['32'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🛩Samalyot bileti*', parse_mode='markdown')
    
@bot.message_handler(commands=['31'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🤹‍♂️Sirkchi darajasi*', parse_mode='markdown')
    
@bot.message_handler(commands=['30'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
    
@bot.message_handler(commands=['0'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🎊Cheksizlik qo`lqobi🎊*', parse_mode='markdown')
    
@bot.message_handler(commands=['29'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔑Kalit*', parse_mode='markdown')
    
@bot.message_handler(commands=['28'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🎛Gidrometr*', parse_mode='markdown')
    
@bot.message_handler(commands=['27'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *♟Shaxmat ustasi darajasi*', parse_mode='markdown')
    
@bot.message_handler(commands=['26'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *💸Pul*', parse_mode='markdown')
    
@bot.message_handler(commands=['25'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🖤Tosh yurak*', parse_mode='markdown')
    
@bot.message_handler(commands=['24'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql Toshi*', parse_mode='markdown')
    
@bot.message_handler(commands=['23'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚁Vertalyot*', parse_mode='markdown')
    
@bot.message_handler(commands=['22'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
         
@bot.message_handler(commands=['21'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🤹‍♂️Sirkchi darajasi*', parse_mode='markdown')
     
@bot.message_handler(commands=['20'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🎛Gidrometr*', parse_mode='markdown')
       
@bot.message_handler(commands=['19'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔦Fanar*', parse_mode='markdown')
       
@bot.message_handler(commands=['18'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
       
@bot.message_handler(commands=['17'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql toshi*', parse_mode='markdown')
       
@bot.message_handler(commands=['16'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔑Kalit*', parse_mode='markdown')
       
@bot.message_handler(commands=['15'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🛩Samalyot bileti*', parse_mode='markdown')
       
@bot.message_handler(commands=['14'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🖤Tosh yurak*', parse_mode='markdown')
       
@bot.message_handler(commands=['13'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🚀Raketa*', parse_mode='markdown')
       
@bot.message_handler(commands=['12'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧬Mutatsiya*', parse_mode='markdown')
       
@bot.message_handler(commands=['11'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔦Fanar*', parse_mode='markdown')
            
@bot.message_handler(commands=['10'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *💎Makon toshi*', parse_mode='markdown')
         
@bot.message_handler(commands=['9'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
         
@bot.message_handler(commands=['8'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *⌛️Soat*', parse_mode='markdown')
         
@bot.message_handler(commands=['7'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql toshi*', parse_mode='markdown')
         
@bot.message_handler(commands=['6'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🐎Ot*', parse_mode='markdown')
         
@bot.message_handler(commands=['5'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🧧Qizil bilet*', parse_mode='markdown')
         
@bot.message_handler(commands=['4'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔮Aql toshi*', parse_mode='markdown')
         
@bot.message_handler(commands=['3'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *⌛️Soat*', parse_mode='markdown')
         
@bot.message_handler(commands=['2'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🔦Fanar*', parse_mode='markdown')
         
@bot.message_handler(commands=['1'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, ' *🎰Bilet tikildi...*', parse_mode='markdown')
            bot.send_message(m.chat.id, '🕒Baraban aylanmoqda...')
            bot.send_message(m.chat.id, '🕤Baraban aylanmoqda...')
            bot.send_message(m.chat.id, 'Tabriklaymiz siz yutib oldingiz - *🍗Ovqat*', parse_mode='markdown')
                  
@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, '*Casiondagi yutuqlar*:\n'+
                     '*🔮Aql Toshi*\n'+
                     '*🔮Aql Toshi*\n'+
                     '*🔮Aql Toshi*', parse_mode='markdown')
            

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


