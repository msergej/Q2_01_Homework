import os
os.system('cls||clear')

import telebot
from bot_tg import Token
import random 

bot = telebot.TeleBot(Token)
N = 65
TurnMax = 28
LeftCandies = N
TurnCandies = 0
BotTurn = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    match message.text:
        case '/help': 
            bot.reply_to(message, "Всего в игре " + str(N) + " конфет. За каждый ход можно взять не более " + str(TurnMax) + " конфет.")
        case '/start': bot.reply_to(message, "Начинаем игру!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global LeftCandies
    TurnCandies = int(message.text)
    if TurnCandies > LeftCandies : bot.send_message(message.chat.id, "Осталось только " + str(LeftCandies) + " конфет. Повторите попытку.")
    elif TurnCandies > TurnMax : bot.send_message(message.chat.id, "Можно брать не более " + str(TurnMax) + " конфет. Повторите попытку.")
    else : 
        LeftCandies -= int(message.text)
        if (LeftCandies > TurnMax) and (LeftCandies > 0) : BotTurn = random.randint(1,TurnMax)
        elif (LeftCandies < TurnMax) and (LeftCandies > 0) : BotTurn = random.randint(1,LeftCandies)
        else : 
            bot.send_message(message.chat.id, "Игра завершена. Поздравляю, Вы выиграли.")
            BotTurn = 0 
        if BotTurn != 0 :
            if BotTurn != LeftCandies : bot.send_message(message.chat.id, "Я взял " + str(BotTurn) + ", Ваш ход.")
            else : bot.send_message(message.chat.id, "Я взял " + str(BotTurn))
            LeftCandies -= BotTurn
            bot.send_message(message.chat.id, "Осталось конфет - " + str(LeftCandies))
        if (LeftCandies == 0) and (BotTurn != 0) : bot.send_message(message.chat.id, "Игра завершена. Ура, я выиграл!")

print("Бот запущен.")
bot.infinity_polling()