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
games=[-1001187120804]

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
                     '0: *25*', parse_mode='markdown')
            
            
@bot.message_handler(commands=['join'])
def join(m):
    if m.chat.id in games:
        if m.from_user.id not in games[m.chat.id]['players']:
          if games[m.chat.id]['began']!=1:
            try:
                bot.send_message(m.from_user.id, 'Вы присоединились к казино!')
                bot.send_message(m.chat.id, m.from_user.first_name+' Вошел в казино!')
                games[m.chat.id]['players'].update(createuser(m.from_user.id, m.from_user.first_name))
            except:
                bot.send_message(m.chat.id, m.from_user.first_name+', сначала напишите боту в личку!')


@bot.message_handler(commands=['roll'])
def roll(m):
    if m.from_user.id in admins:
        if m.chat.id in games:
          if games[m.chat.id]['began']==1:
            x=random.randint(0,30)
            msg=bot.send_message(m.chat.id, 'Крутим барабан...\n'+'🕐')
            t=threading.Timer(0.1, roll2, args=[m.chat.id, msg.message_id])
            t.start()
            
            
def roll2(id, id2):
    medit('Крутим барабан...\n'+'🕑', id, id2)
    t=threading.Timer(0.1, roll3, args=[id, id2])
    t.start()
    
def roll3(id, id2):
    medit('Крутим барабан...\n'+'🕒', id, id2)
    t=threading.Timer(0.1, roll4, args=[id, id2])
    t.start()
    
    
def roll4(id, id2):
    medit('Крутим барабан...\n'+'🕓', id, id2)
    t=threading.Timer(0.1, roll5, args=[id, id2])
    t.start()
    
    
def roll5(id, id2):
    medit('Крутим барабан...\n'+'🕔', id, id2)
    t=threading.Timer(0.1, roll6, args=[id, id2])
    t.start()
    
def roll6(id, id2):
    medit('Крутим барабан...\n'+'🕕', id, id2)    #half
    t=threading.Timer(0.1, roll7, args=[id, id2])
    t.start()
    
def roll7(id, id2):
    medit('Крутим барабан...\n'+'🕖', id, id2)   
    t=threading.Timer(0.1, roll8, args=[id, id2])
    t.start()
    

def roll8(id, id2):
    medit('Крутим барабан...\n'+'🕗', id, id2)   
    t=threading.Timer(0.1, roll9, args=[id, id2])
    t.start()
    
    
def roll9(id, id2):
    medit('Крутим барабан...\n'+'🕘', id, id2)   
    t=threading.Timer(0.1, roll10, args=[id, id2])
    t.start()
    
    
def roll10(id, id2):
    medit('Крутим барабан...\n'+'🕙', id, id2)   
    t=threading.Timer(0.1, roll11, args=[id, id2])
    t.start()
    
    
def roll11(id, id2):
    medit('Крутим барабан...\n'+'🕚', id, id2)   
    t=threading.Timer(0.1, roll12, args=[id, id2])
    t.start()
    
    
def roll12(id, id2):
    medit('Крутим барабан...\n'+'🕛', id, id2)   
    t=threading.Timer(0.1, rollend, args=[id, id2])
    t.start()   
    
    
def rollend(id, id2):
    x=random.randint(0,30)
    medit('Выпавшее число: *'+str(x)+'*.', id, id2)
    text='Результаты:\n\n'
    for ids in games[id]['players']:
      if games[id]['players'][ids]['betto']!=None:
        if games[id]['players'][ids]['betto']=='1-15':
            if x>0 and x<=15:
                win=games[id]['players'][ids]['bet']*1.5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
            
        if games[id]['players'][ids]['betto']=='16-30':
            if x>=16 and x<=30:
                win=games[id]['players'][ids]['bet']*1.5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
         
        if games[id]['players'][ids]['betto']=='1-5':
            if x>=1 and x<=5:
                win=games[id]['players'][ids]['bet']*5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
                
        if games[id]['players'][ids]['betto']=='6-10':
            if x>=6 and x<=10:
                win=games[id]['players'][ids]['bet']*5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
                print(win)
                
        if games[id]['players'][ids]['betto']=='11-15':
            if x>=11 and x<=15:
                win=games[id]['players'][ids]['bet']*5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
                
        if games[id]['players'][ids]['betto']=='16-20':
            if x>=16 and x<=20:
                win=games[id]['players'][ids]['bet']*5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
                
        if games[id]['players'][ids]['betto']=='21-25':
            if x>=21 and x<=25:
                win=games[id]['players'][ids]['bet']*5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
                
        if games[id]['players'][ids]['betto']=='26-30':
            if x>=26 and x<=30:
                win=games[id]['players'][ids]['bet']*5
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
                
        if games[id]['players'][ids]['betto']=='0':
            if x==0:
                win=games[id]['players'][ids]['bet']*25
                win=round(win, 0)
                text+='*'+games[id]['players'][ids]['name']+'*'+' Выиграл '+str(win)+' членокоин(ов)!\n'
                users.update_one({'id':ids}, {'$inc':{'chlenocoins':-games[id]['players'][ids]['bet']}})
            else:
                win=-games[id]['players'][ids]['bet']
                print(int(win))
                text+='*'+games[id]['players'][ids]['name']+'*'+' проиграл '+str(win+(-win*2))+' членокоин(ов)!\n'
      else:
        text+='*'+games[id]['players'][ids]['name']+'*'+' Не поставил ничего!\n'
        win=0
      users.update_one({'id':ids}, {'$inc':{'chlenocoins':win}})
                
    bot.send_message(id, text, parse_mode='markdown')
    del games[id]
        
        
 
    

                
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
                        bot.send_message(m.from_user.id, 'Вы поставили '+str(x)+' членокоинов! Теперь выберите, на что вы их ставите:', reply_markup=kb)
                    else:
                        bot.send_message(m.chat.id, 'Недостаточно членокоинов!')
            except:
                pass
           
                
            
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  i=0
  for ids in games:
    if call.from_user.id in games[ids]['players']:
        i=1
        y=games[ids]
  if i==1:
        y['players'][call.from_user.id]['betto']=call.data
        medit('Ставка принята. Вы поставили '+str(y['players'][call.from_user.id]['bet'])+' членокоинов на '+call.data+'! Ждите результатов в чате', call.from_user.id, call.message.message_id)
        bot.send_message(y['id'], y['players'][call.from_user.id]['name']+' поставил '+str(y['players'][call.from_user.id]['bet'])+' членокоинов на '+call.data+'!')
        
    
    
    
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
                '0':25,
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


