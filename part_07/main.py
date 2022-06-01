import settings
import telebot
import requests
import json
import wikipedia

bot = telebot.TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands=['help'])
def help(message):
    mess = 'Для работы с калькулятором введите <u>/calc "выражение"</u>\n'
    mess += 'Получить рандомную утку <u>/duck</u>\n'
    mess += 'Поиск по wikipedia <u>/wiki "что ищем"</u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['calc'])
def calc(message):
    args = message.text.split()
    arg = ''
    if len(args) > 1:
        arg = ''.join(args[1:])
    result = eval(arg)
    mess = result
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['duck'])
def duck(message):
    url = 'https://random-d.uk/api/random'
    response = requests.get(url)
    duck_link = json.loads(response.text)
    mess = duck_link['url']
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['wiki'])
def wiki(message):
    args = message.text.split()
    arg = ''
    if len(args) > 1:
        arg = ' '.join(args[1:])
    response = wikipedia.search(arg, results=10, suggestion=True)
    mess = ''
    mess += f'Результаты поиска для <b>{arg}</b>\n'
    for i in response[0]:
        mess += f'{i}\n'
    bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)
