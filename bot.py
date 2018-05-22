# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
import info
import test
from telebot import types
from emoji import emojize
from pymongo import MongoClient
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

admins=[441399484]
games={}

client1=os.environ['database']
client=MongoClient(client1)
db=client.chlenomer
users=db.ids_people


@bot.message_handler(commands=['begin'])
def begin(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            bot.send_message(m.chat.id, 'Начинаем делать ставки (в лс бота)! Про коэффициенты выигрышей вы можете узнать с помощью команды /help')
            games[m.chat.id]['began']=1
            for ids in games[m.chat.id]['players']:
                bot.send_message(ids, 'Напишите, сколько членокоинов вы хотите поставить.')

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, 'Коэффициенты ставок:\n'+
                     '1-15, 16-30: *1.5*\n'+
                     '1-5, 6-10, 11-15, 16-20, 21-25, 26-30: *5*\n'+
                     '0: *15*', parse_mode='markdown')
            
            
@bot.message_handler(commands=['join'])
def join(m):
    if m.chat.id in games:
        if m.from_user.id not in games[m.chat.id]['players']:
          if games[m.chat.id]['began']!=1:
            try:
                bot.send_message(m.from_user.id, 'Вы участвуете в казино!')
                bot.send_message(m.chat.id, m.from_user.first_name+' Вошел в казино!')
                games[m.chat.id]['players'].update(createuser(m.from_user.id, m.from_user.first_name))
            except:
                bot.send_message(m.chat.id, m.from_user.first_name+', сначала напишите боту в личку!')


@bot.message_handler(commands=['roll'])
def roll(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
            
                
                
@bot.message_handler(commands=['stavki'])
def stavki(m):
  if m.from_user.id in admins:
    if m.chat.id not in games:
        games.update(createlobby(m.chat.id))
        bot.send_message(m.chat.id, 'Казино открыто! Жмите /join, чтобы испытать удачу и выиграть членокоины!')
  else:
    bot.send_message(m.chat.id, 'Создать лобби может только администратор казино!')

@bot.message_handler(content_types=['text'])
def texttt(m):
    if m.chat.id==m.from_user.id:
        i=0
        for ids in games:
            if m.from_user.id in games[ids]['players']:
                i=1
                y=games[ids]
        if i==1:
            try:
                x=int(m.text)
                x=round(x, 0)
                player=users.find_one({'id':m.from_user.id})
                if player!=None:
                    if player['chlenocoins']>=x:
                    y['players'][m.from_user.id]['bet']=x
                    kb=types.InlineKeyboardMarkup()
                    kb.add(types.InlineKeyboardButton(text='1-15', callback_data='1-15'),types.InlineKeyboardButton(text='16-30', callback_data='16-30'),types.InlineKeyboardButton(text='1-5', callback_data='1-5'))
                    kb.add(types.InlineKeyboardButton(text='6-10', callback_data='6-10'),types.InlineKeyboardButton(text='11-15', callback_data='11-15'),types.InlineKeyboardButton(text='16-20', callback_data='16-20'))
                    kb.add(types.InlineKeyboardButton(text='21-25', callback_data='21-25'),types.InlineKeyboardButton(text='26-30', callback_data='26-30'),types.InlineKeyboardButton(text='0', callback_data='0'))
                    bot.send_message(m.from_user.id, 'Вы поставили '+str(x)+' членокоинов! Теперь выберите, на что вы их ставите:')
                
            
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  i=0
  for ids in games:
    if call.from_user.id in games[ids]['players']:
        i=1
        y=games[ids]
  if i==1:
        y['players']['betto']=call.data
        medit('Ставка принята. Вы поставили '+str(y['players']['bet'])+' членокоинов на '+call.data+'! Ждите результатов в чате', call.from_user.id, call.message.message_id)
        
    
    
    
def createuser(id, name):
    return{id:{
        'id':id,
        'bet':None,
        'betto':None,
        'name':name
    }
          }
    
def createlobby(id):
    return{id:{
        'id':id,
        'began':0,
        'players':{},
        'result':None,
        'coef':{'1-15':1.5,
                '16-30':1.5,
                '0':15,
                '1-5':5,
                '6-10':5,
                '11-15':5,
                '16-20':5,
                '21-25':5,
                '26-30':5
               }
             }
           }
        
                
                
        
        
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


