from telebot import types
import requests
import telebot

bot = telebot.TeleBot('TOKEN')  # foydalibot

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row("O'zbek tili", 'Pусский', 'English')


@bot.message_handler(commands=[ 'start' ])
def start_message(message):
    bot.send_message(message.chat.id, '{} {}\n \n Tilni tanlang | Bыберите язык | Select the language'.
                     format(message.from_user.first_name, message.from_user.last_name), reply_markup=keyboard1)


@bot.message_handler(content_types=[ 'text' ])
def send_text(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_havo = types.InlineKeyboardButton(text='Valyuta kurslari')
    keyboard.add(key_havo)

    key_valyuta = types.InlineKeyboardButton(text='Valyuta konvertori')
    keyboard.add(key_valyuta)

    keyboard1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_havo1 = types.InlineKeyboardButton(text='Обменные курсы')
    keyboard1.add(key_havo1)

    key_valyuta1 = types.InlineKeyboardButton(text='Конвертеры валют')
    keyboard1.add(key_valyuta1)

    keyboard2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_havo2 = types.InlineKeyboardButton(text='Exchange rates')
    keyboard2.add(key_havo2)

    key_valyuta2 = types.InlineKeyboardButton(text='Currency converters')
    keyboard2.add(key_valyuta2)

    if message.text.lower() == "o'zbek tili":
        bot.send_message(message.chat.id,
                         'Salom, ' + message.from_user.first_name +
                         message.from_user.last_name + ' sizga qanday yordam bera olaman?',
                         reply_markup=keyboard)

    elif message.text.lower() == 'pусский':
        bot.send_message(message.chat.id,
                         'Привет, ' + message.from_user.first_name
                         + message.from_user.last_name + ' Чем я могу помочь вам',
                         reply_markup=keyboard1)

    elif message.text.lower() == "english":
        bot.send_message(message.chat.id,
                         'Hi, ' + message.from_user.first_name
                         + message.from_user.last_name + 'how can I help you',
                         reply_markup=keyboard2)

    elif message.text.lower() == 'valyuta konvertori':
        bot.send_message(message.chat.id,
                         'Salom {} {}\n\n Ushbu bo\'lim barcha valyutalarni hisboblab beradi.\n '
                         'Kalkulyatorni ishlatish uchun chel el valyutasi miqdorini kiring\n '
                         "masalan: 50\n\n javob namuna:\n Rossiya rubli: 50 RUB - 6959.5 UZS"
                         .format(message.from_user.first_name, message.from_user.last_name, ))

    elif message.text.lower() == 'конвертеры валют' \
            or message.text.lower() == 'currency converters':

        bot.send_message(message.chat.id,
                         'Привет {} {}\n\n''Введите сумму в иностранной валюте, чтобы использовать калькулятор\n'
                         "Например: 50\n\nобразец ответа:\nРусский рубль: 50 RUB - 6959.5 UZS "
                         .format(message.from_user.first_name, message.from_user.last_name, ))

    elif message.text.lower() == 'currency converters':

        bot.send_message(message.chat.id,
                         'Hi {} {}\n\n''This section calculates all currencies\n '
                         "for example: 50\n\n образец ответа:\n Russian ruble: 50 RUB - 6959.5 soums "
                         .format(message.from_user.first_name, message.from_user.last_name, ))

    elif message.text.lower() == 'valyuta kurslari' or \
            message.text.lower() == 'обменные курсы' or message.text.lower() == "exchange rates":

        # imojilar
        y = [ "🇦🇪", "🇦🇺", "🇨🇦", "🇸🇪", "🇨🇳", "🇩🇰", "🇪🇬", "🇪🇺", "🇦🇮", "🇮🇪", "🇯🇵", "🇰🇷",
              "🇰🇼", "🇰🇿", "🇱🇧", "🇲🇾", "🇳🇴", "🇵🇱", "🇷🇺", "🇸🇪", "🇸🇬", "🇹🇷", "🇺🇸", ]

        r = requests.get('https://nbu.uz/uz/exchange-rates/json/')
        data = r.json()
        x = ' '
        text = '🇺🇿 Markaziy Bank valyuta kurslari\n🇷🇺 Обменные курсы ЦБ\n🇬🇧 Central Bank exchange rates\n\n'

        for i, t in zip(data, y):
            x = i[ 'date' ]
            text += '{} {}:\n1 {} - {} UZS \n \n'.format(t, i[ 'title' ], i[ 'code' ], i[ 'cb_price' ])
        text += 'Markaziy bankda oxirgi kurs yangilinish vaqti:\n🕢 {}'.format(x)
        bot.reply_to(message, text)

    elif message.text:
        # imojilar
        i = [ "🇦🇪", "🇦🇺", "🇨🇦", "🇸🇪", "🇨🇳", "🇩🇰", "🇪🇬", "🇪🇺", "🇦🇮", "🇮🇪", "🇯🇵", "🇰🇷",
              "🇰🇼", "🇰🇿", "🇱🇧", "🇲🇾", "🇳🇴", "🇵🇱", "🇷🇺", "🇸🇪", "🇸🇬", "🇹🇷", "🇺🇦", "🇺🇸", ]
        r = requests.get('https://nbu.uz/uz/exchange-rates/json/')
        data = r.json()
        x = message.text
        # a = ''
        text = ''
        vaqt = ''
        if message.text:
            for i, y in zip(data, i):
                vaqt = i[ 'date' ]
                a = float(i[ 'cb_price' ]) * float(x)
                text += "{} {}:\n {} {} - {:,} UZS \n \n".format(y, i[ 'title' ], x, i[ 'code' ], a)
            text += 'Markaziy bankda oxirgi kurs yangilinish vaqti:\n🕢 {}'.format(vaqt)
            bot.reply_to(message, text)

        else:
            bot.send_message(message.chat.id,
                             'Xato' + message.from_user.first_name + message.from_user.last_name,
                             reply_markup=keyboard1)


if __name__ == '__main__':
    bot.polling(none_stop=True)
