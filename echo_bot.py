# -*- coding: utf-8 -*-

import time
import requests
import logging
import telebot
import random
from threading import Timer
from random import randint

TOKEN = '400737756:AAEajsn0Uj_J1IacoXMn0dAC6lU9RqXPD8k'

MALIKI = [362796559, 448235552]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(5)
    sent = bot.send_sticker(message.chat.id, random.choice(['CAADAgADDgADYFElCzjtivqDRz-JAg', 'CAADAgADCQADYFElC8SlykRG1IyOAg']))
    time.sleep(5)
    sent = bot.send_message(message.chat.id, random.choice(['Блин перечитывал что вы тут настрочили, Стасик так и не понял что фраза " деньги есть но жалко " про него', 'Привет', 'Привет )', 'Всем привет']))
    while True:
        time.sleep(random.randint(30, 120)*60)
        sent = bot.send_sticker(message.chat.id, random.choice(['CAADAgADDgADYFElCzjtivqDRz-JAg', 'CAADAgADCQADYFElC8SlykRG1IyOAg', 'CAADAgADIgADYFElCzdPGYTy6r3GAg', 'CAADAgADLQADYFElC62sNq9zeKBVAg', 'CAADAgADJwADYFElC-nJXsrzq6MLAg', 'CAADAgADHwADYFElC4mGqBU_41usAg', 'CAADAgADDwADYFElC6zz9r-iJuukAg', 'CAADAgADJAADYFElC8b6QDYeGPMTAg', 'CAADAgADBAADYFElC-cFHLeZlXwaAg', 'CAADAgADIwADYFElC4uAa3oid7KBAg', 'CAADAgADBAADLEIJDAidfMcy0eS1Ag', 'CAADAgADFgADYFElC2wJeVbxDl9wAg', 'CAADAgADNAADYFElCwmxwZ_5UiOOAg', 'CAADAgADEAADYFElCwcLwYWI_VAjAg']))

@bot.message_handler(content_types=['sticker'])
def handle_message(message):
    if message.chat.id in MALIKI:
        sent = bot.send_chat_action(message.chat.id, 'typing')
        sent = bot.send_message(message.chat.id, random.choice(['Иногда задумываешься какой же я дурачок', 'Самому интересно как я не заебался это слать']))

@bot.message_handler(regexp="малик иди на")
def handle_message(message):
    time.sleep(5)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    sent = bot.send_sticker(message.chat.id, "CAADAgADCgADLEIJDPIZjwWtRVGFAg")

@bot.message_handler(regexp="янка")
def handle_message(message):
    sent = bot.send_sticker(message.chat.id, random.choice(["CAADAgADKwADYFElC691e3KpsQ7YAg", "CAADAgADMQADYFElCw8cVWLTWdBPAg", "CAADAgADKgADYFElC_1NkBKJnWZWAg", "CAADAgADBAADYFElC-cFHLeZlXwaAg", "CAADAgADBwADYFElC6B7FNaqMfZcAg", "CAADAgADMgADYFElC7LWS8ywIXC_Ag", "CAADAgADKAADYFElC6DSoW1DIOTgAg", "CAADAgADBQAD2VwoDP1KKlT9p-3RAg"]))

@bot.message_handler(regexp="стасик")
def handle_message(message):
    time.sleep(5)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(5)
    sent = bot.send_message(message.chat.id, random.choice(['Денег жалко, но они есть', 'Можно ли считать Стаса в 31, примером для подражания', 'Стас знает больше чем ты сам себе думаешь)', 'У Стасика скоро горе от ума начнется', 'Стасик думает что все знает) лучше самих людей', 'Если вы забыли, то Стасику 31']))
    time.sleep(2)
    sent = bot.send_sticker(message.chat.id, random.choice(["CAADAgADLQADYFElC62sNq9zeKBVAg", "CAADAgADJwADYFElC-nJXsrzq6MLAg"]))

@bot.message_handler(regexp="крым")
def handle_message(message):
    time.sleep(5)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Расскажи всем какая тут жопа', 'Стасик, тут кстати часто истребители летают', 'Жить там в Киеве или другом большом городе хорошо, но деньги отдавать за кВ нужно', 'Крым заслужил такую парочку как мы с янкой']))

@bot.message_handler(regexp=" ана")
def handle_message(message):
    time.sleep(2)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(3)
    sent = bot.send_message(message.chat.id, random.choice(['Сдохни анна', 'Опять вы про ханну', 'А чего анна кидала?', 'Анька наш арго-котик', 'жаль что рожу ее не исправить уже']))

@bot.message_handler(regexp="денчик")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_sticker(message.chat.id, random.choice(["CAADAgADDwADYFElC6zz9r-iJuukAg", "CAADAgADGAADYFElCw7D4doYu5jfAg", "CAADAgADFAADYFElC_fBxcGDlTTpAg", "CAADAgADNAADYFElCwmxwZ_5UiOOAg", "CAADAgADIgADYFElCzdPGYTy6r3GAg", "CAADAgADFgADYFElC2wJeVbxDl9wAg", "CAADAgADGgADYFElC2YKkbHtTcz5Ag"]))

@bot.message_handler(regexp="анна")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_sticker(message.chat.id, random.choice(["CAADAgADDQADLEIJDMHlgCIT4WLBAg", "CAADAgADDAADLEIJDObpGuspPxszAg"]))

@bot.message_handler(regexp="малик завали ебало")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['ок (', 'я сейчас прям детство вспомнил (', 'прямо как с янкой общаюсь (']))

@bot.message_handler(regexp="вырубите этого малика")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['я щас тебя вырублю', 'все-все, я буду хорошим']))

@bot.message_handler(regexp="вырубите малика")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['я щас тебя вырублю', 'все-все, я буду хорошим']))

@bot.message_handler(regexp="малик заебал")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['все-все, я буду хорошим', 'Янка меня тоже заебала']))

@bot.message_handler(regexp="привет")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Пидора ответ']))

@bot.message_handler(regexp="выезжать")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['до маркета, как обычно', 'в маркете сегодня скидки']))

@bot.message_handler(regexp="кататься")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['до маркета, как обычно', 'в маркете сегодня скидки']))

@bot.message_handler(regexp="балбес")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, 'Это я')

@bot.message_handler(regexp="соси хуй")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Я думал, ты никогда не предложишь =)']))

@bot.message_handler(regexp="хуй малика")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Янка всегда говорила, что он сладенький. Правда, ей и черниговское сладкое']))

@bot.message_handler(regexp="соси")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Кстати янка когда хуй сосет губой все-таки не трясет. Я проверял', 'Мммм']))

@bot.message_handler(regexp="работ")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['После работы я обычно спать )', 'Вообщем норм', 'Нужно время от времени менять работу', 'Работа по найму самое жосткое рабство']))

@bot.message_handler(regexp="кидал")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Заебали про Аньку, она не обещала выходить', 'Есть тут у меня одна маленькая кидала']))

@bot.message_handler(regexp="сись")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Блять, я сисек уже полтора года не видел', 'Жду сисек Анны в инсте']))

@bot.message_handler(regexp="дурачок")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Можно подумать вы тут дохуя умные', 'Спасибо', 'Кто хочет с дурачком попререкаться я к вашим услугам']))

@bot.message_handler(regexp="сасик")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Анна не усыпляй плс', 'Ну Анна, не усыпляй', 'Анна Хуец на связи']))

@bot.message_handler(regexp="секс")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Хочу ебаться пять минут', 'До сих пор обидно, что Александра не пошла ко мне ночевать', 'Лучший мой секс был до янки', 'Люблю представлять Наташу вместо янки']))

@bot.message_handler(regexp="бот")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Приятно, в который раз, что он тратит на это свою жизнь )', 'Это Стасик опять самоутверждается', 'Бля прикинь ему с двух аккаунтов печатать', 'Все в мире относительно', 'Все может быть', 'Янка, бросай своего хуевого малика, я лучше']))

@bot.message_handler(regexp="артем")
def handle_message(message):
    time.sleep(3)
    sent = bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    sent = bot.send_message(message.chat.id, random.choice(['Было время когда Артём разрешал Наташе кататься', 'Артём, а та квартира где ты живёшь не твоя же?']))

bot.polling(none_stop=True)