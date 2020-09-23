import telebot
from telebot import types
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import sqlite3
import io

bot = telebot.TeleBot('1262098190:AAGA8ugBKL5UW6D_z2X43rldKNfn32BUiVo')

# db = sqlite3.connect('server.db')
# sql = db.cursor()

# sql.execute("""CREATE TABLE IF NOT EXISTS users (
#  h1 TEXT,
#  h2 TEXT,
#  h3 TEXT,
#  h4 TEXT,
#  h5 TEXT,
#  h6 TEXT,
#  h7 TEXT,
#  week TEXT,
# vg2 TEXT,
# plans TEXT,
# ) """)

# db.commit()
global name


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, """        
Привіт! Я Х-Мама!🤱🏽
Якщо ти ще не зареєструвалася в нашому клубі - я тобі допоможу!🤗
Розкажу про X-Mothers та відповім на питання.
Тисни на - /menu
        """)


@bot.message_handler(commands=['list'])
def list(message):
    user_id = message.from_user.id
    if user_id == 906203059:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("За містом проживання")
        item2 = types.KeyboardButton("Вагітна")
        item3 = types.KeyboardButton("Мама з дитиною до 6 місяців")
        item4 = types.KeyboardButton("Мама з дитиною 1-3х років")
        item5 = types.KeyboardButton("Мама з дитиною до 1 року")
        item6 = types.KeyboardButton("Мама з дитиною 3-7 років")
        item7 = types.KeyboardButton("Мама з дитиною від 7 років(школяр)")
        markup.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.from_user.id, 'Яким тегам?', reply_markup=markup)
        bot.register_next_step_handler(message, get_pp)
    else:
        bot.send_message(message.from_user.id, 'Ця команда тільки для супермам, які 24/7 працюють для вас!')


def get_pp(message):
    g = bot.send_message(message.from_user.id, 'Текст розсилки')

    def geev(message):
        if message.text == 'За містом проживання':
            bot.send_message(message.from_user.id, 'Яке місто?')
            bot.register_next_step_handler(message, get_misto)
            if misto == 'Київ':
                bot.send_message(message.from_user.id, gg)
        elif message.text == 'Вагітна':
            if vg == 'Так':
                bot.send_message(message.from_user.id, gg)
        elif message.text == 'Мама з дитиною до 6 місяців':
            if babyl == babyl < int(1):
                bot.send_message(message.from_user.id, gg)
        elif message.text == 'Мама з дитиною 1-3х років':
            if babyl == int(2):
                bot.send_message(message.from_user.id, gg)
            elif babyl == int(3):
                bot.send_message(message.from_user.id, gg)
        elif message.text == 'З дитиною до одного року':
            if babyl == int(1):
                bot.send_message(message.from_user.id, gg)
        elif message.text == 'Мама з дитиною 3-7 років':
            if babyl == int(3):
                bot.send_message(message.from_user.id, gg)
            elif babyl == int(4):
                bot.send_message(message.from_user.id, gg)
            elif babyl == int(5):
                bot.send_message(message.from_user.id, gg)
            elif babyl == int(6):
                bot.send_message(message.from_user.id, gg)
            elif babyl == int(7):
                bot.send_message(message.from_user.id, gg)
        elif message.text == 'Мама з дитиною від 7 років(школяр)':
            if babyl == babyl > int(6):
                bot.send_message(message.from_user.id, gg)
        else:
            bot.send_message(message.from_user.id, 'Ви зробили щось не так')


@bot.message_handler(commands=['menu'])
def keyboard(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(
            text='Хочу стати учасницею клуба мам Х-Mothers',
            callback_data='k1'
        ),
        types.InlineKeyboardButton(
            text='Хочу стати партнером',
            url='https://www.xmothers.com/spivprachya/'
        ),
        types.InlineKeyboardButton(
            text='Хочу стати вашим представником',
            url='https://www.xmothers.com/spivprachya/'
        ),
        types.InlineKeyboardButton(
            text='Я мама блогер',
            url='https://www.xmothers.com/spivprachya/'
        ),
        types.InlineKeyboardButton(
            text='FAQ(часті питання)',
            callback_data='k5'
        ),
        types.InlineKeyboardButton(
            text='Про клуб',
            url='https://www.xmothers.com/'
        ),
        types.InlineKeyboardButton(
            text='Наші партнери',
            url='https://www.xmothers.com/partners/'
        ),
        types.InlineKeyboardButton(
            text='Чат мам мого міста',
            url='https://www.xmothers.com/contact/ '
        ),
        types.InlineKeyboardButton(
            text='Ми в соціальних мережах',
            callback_data='k7'
        ),
    ]
    markup.add(*buttons)
    bot.send_message(message.from_user.id, """
Привіт! Ось ми знову й зустрілись☺️
Хочеш стати учсницею клубу X-Mothers – тисни на першу кнопку та заповни анкету.
Чи хочеш спочатку ознайомитись з нашим клубом?
Пам’ятай, ти завжди можеш повернутися в меню командою - /menu """, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'k1':
                bot.send_message(call.message.chat.id, """  
Щоб стати учасницею нашого клубу, дайте відповідь на 10 питань, після чого Ви отримаєте іменну карту учасниці клубу X-Mothers!
  """)
                markup = types.ReplyKeyboardMarkup(True, True)
                item1 = types.KeyboardButton("Так")
                item2 = types.KeyboardButton("Ні");
                markup.add(item1, item2)
                bot.send_message(call.message.chat.id, 'Почнемо?', reply_markup=markup)
                bot.register_next_step_handler(call.message, get_h1)
            elif call.data == 'k2':
                bot.send_message(call.message.chat.id, 'Партнер')
                bot.register_next_step_handler(call.message, get_h2)
            elif call.data == 'k3':
                bot.send_message(call.message.chat.id, 'Я кнопка')
            elif call.data == 'k4':
                bot.send_message(call.message.chat.id, 'Я кнопка')
            elif call.data == 'k5':
                markup = types.InlineKeyboardMarkup(row_width=1)
                buttonss = [
                    types.InlineKeyboardButton(
                        text='Розкажіть мені про клуб',
                        callback_data='f1'
                    ),
                    types.InlineKeyboardButton(
                        text='Що дає карта учасниці клубу?',
                        callback_data='f2'
                    ),
                    types.InlineKeyboardButton(
                        text='Як стати учасницею клубу?',
                        callback_data='f3'
                    ),
                    types.InlineKeyboardButton(
                        text='Хто ваші партнери?',
                        callback_data='f4'
                    ),
                    types.InlineKeyboardButton(
                        text='Чат мам мого міста',
                        callback_data='f5'
                    ),
                    types.InlineKeyboardButton(
                        text='Написати нам!',
                        callback_data='f6'
                    ),
                ]
                markup.add(*buttonss)
                bot.send_message(call.message.chat.id, "Що вас цікавить?", reply_markup=markup)

            elif call.data == 'k6':
                bot.send_message(call.message.chat.id, 'Я кнопка')
            elif call.data == 'k7':
                markup = types.InlineKeyboardMarkup(row_width=1)
                switch_buttonp = [
                    types.InlineKeyboardButton(
                        text='Instagram',
                        url="https://instagram.com/_xmothers_?igshid=13vt14b4z4g1e"
                    ),
                    types.InlineKeyboardButton(
                        text='Telegram',
                        url="tg://resolve?domain=xmothers"
                    ),
                    types.InlineKeyboardButton(
                        text='Facebook',
                        url="https://m.facebook.com/xmothers"
                    ),
                    types.InlineKeyboardButton(
                        text='YouTube',
                        url="https://www.youtube.com/channel/UChbkB6GDX2mf-zgAzvSNxBg/featured"
                    ),
                ]
                markup.add(*switch_buttonp)
                bot.send_message(call.message.chat.id, 'Наші соц. мережі', reply_markup=markup)
            elif call.data == 'f1':
                markup = types.InlineKeyboardMarkup(row_width=1)
                switch_buttong = [
                    types.InlineKeyboardButton(
                        text='Дізнатись більше ',
                        url="https://www.xmothers.com/pro-klub/"
                    ),
                ]
                markup.add(*switch_buttong)
                bot.send_message(call.message.chat.id, """
Клуб X-Mothers створений, щоб об’єднувати мам України. 
    Наша мета – організовувати для мам привілеї та активності, які полегшать життя, принесуть користь, 
задоволення та зекономлять кошти. Зроблять все, щоб материнство було в радість! 
    Ми – клуб, у якому кожна мама знайде щось корисне для себе!
                    """, reply_markup=markup)
            elif call.data == 'f2':
                markup = types.InlineKeyboardMarkup(row_width=1)
                switch_buttonl = [
                    types.InlineKeyboardButton(
                        text='Стати учасницею клубу X-Mothers',
                        callback_data="k1"
                    ),
                ]
                markup.add(*switch_buttonl)
                bot.send_message(call.message.chat.id, """ 
З картою учасниці клубу X-Mothers ви зможете:
✅ Отримувати товари та послуги наших партнерів зі знижками
✅ Брати участь у подіях та майстер-класах клубу
✅ Отримувати підтримку наших мам-координаторів вашого міста
✅ Доступ до чату мам вашого міста
✅ Доступ до актуальної та корисної інформації клубу
✅ Доступ до вакансій для мам у декреті
✅ Брати участь у конкурсах та розіграшах клубу. 
                """, reply_markup=markup)

            elif call.data == 'f3':
                markup = types.InlineKeyboardMarkup(row_width=1)
                switch_buttonll = [
                    types.InlineKeyboardButton(
                        text='Стати учасницею клубу X-Mothers',
                        callback_data="k1"
                    ),
                ]
                markup.add(*switch_buttonll)
                bot.send_message(call.message.chat.id, 'Щоб стати учасницею клубу, необхідно заповнити анкету.',
                                 reply_markup=markup)

            elif call.data == 'f4':
                markup = types.InlineKeyboardMarkup(row_width=1)
                switch_buttonlll = [
                    types.InlineKeyboardButton(
                        text='Наші партнери',
                        url="https://www.xmothers.com/partners/"
                    ),
                ]
                markup.add(*switch_buttonlll)
                bot.send_message(call.message.chat.id, """ Наші партнери - магазини товарів для мам та діточок, мами-блогери, фотографи, компанії, які надають послуги мамам. 
                Щоб отримати привілеї клубу X-Mothers від наших партнерів, продемонструйте картку учасниці в їх офлайн-магазині, або надішліть скріншот в онлайн-магазин.""",
                                 reply_markup=markup)
            elif call.data == 'f5':
                markup = types.InlineKeyboardMarkup(row_width=1)
                switch_buttonllqt = [
                    types.InlineKeyboardButton(
                        text='Наші чати ',
                        url="https://www.xmothers.com/contact/"
                    ),
                ]
                markup.add(*switch_buttonllqt)
                bot.send_message(call.message.chat.id, 'Як мені знайти чат мам мого міста? ', reply_markup=markup)
            elif call.data == 'f6':
                markup = types.InlineKeyboardMarkup(row_width=1)
                switch_buttonllq = [
                    types.InlineKeyboardButton(
                        text='Зв’язатись з представником',
                        url="tg://resolve?domain=xmothers"
                    ),
                ]
                markup.add(*switch_buttonllq)
                bot.send_message(call.message.chat.id, 'Якщо не знайшли відповіді на своє питання – напишіть нам!',
                                 reply_markup=markup)
            else:
                bot.send_message(call.message.chat.id, 'Щось пішло не так. Тисни на - /menu')

    except Exception as e:
        print(repr(e))


@bot.message_handler(func=lambda c: True, content_types=['text'])
def info_message(message):
    bot.edit_message_reply_markup(message.chat.id, message_id=message.message_id - 1, reply_markup='')


@bot.message_handler(content_types=['text'])
def get_h1(message):
    if message.text == 'Так':
        global name
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Ваше прізвище та ім'я", reply_markup=a)
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'Ні':
        bot.send_message(message.from_user.id, 'Передумали? Тисніть на /menu', reply_markup=a)


# def get_h1(message):
# sql.execute("SELECT
# login FROM users WHERE login = '{h1}'")
# if sql.fetchone() is None:
#   sql.execute(f"INSERT INTO users VALUES (?)", (h1))
#   db.commit()
#   bot.send_message(message.from_user.id,"Дата народження")
#   bot.register_next_step_handler(message, get_h2)
# else:
#     bot.send_message(message.from_user.id, 'Такий профіль вже зареєстрований!')
#    bot.send_message(message.from_user.id, 'Повернутися в меню - /menu')

def get_name(message):
    name = message.text
    bot.send_message(message.from_user.id, "Місто проживання")
    bot.register_next_step_handler(message, get_h3)


def get_h3(message):
    h3 = message.text
    bot.send_message(message.from_user.id, "Телефон")
    bot.register_next_step_handler(message, get_h4)


def get_h4(message):
    h4 = message.text
    bot.send_message(message.from_user.id, "Емейл")
    bot.register_next_step_handler(message, get_h5)


def get_h5(message):
    h5 = message.text
    bot.send_message(message.from_user.id, "Посилання на вашу соц. мережу")
    bot.register_next_step_handler(message, get_inst)


def get_inst(message):
    h6 = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні");
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'Ви мама', reply_markup=markup)
    bot.register_next_step_handler(message, get_mama)


def get_mama(message):
    if message.text == 'Так':
        mama = 'Так'
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_h7)
    elif message.text == 'Ні':
        mama = 'Ні'
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_mama(message):
    vg = message.text
    if message.text == 'Так':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_h7)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_h7(message):
    h7 = message.text
    if message.text == 'Хлопчик':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у нього день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl)
    elif message.text == 'Дівчинка':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у неї день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl)


def get_babyl(message):
    babyl = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні")
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'У вас є ще дітки?', reply_markup=markup)
    bot.register_next_step_handler(message, get_babyone2)


def get_babyone2(message):
    babyone2 = message.text
    if message.text == 'Так':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_q1)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_q1(message):
    q1 = message.text
    if message.text == 'Хлопчик':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у нього день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl)
    elif message.text == 'Дівчинка':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у неї день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl)


def get_babyl(message):
    babyl = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні")
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'У вас є ще дітки?', reply_markup=markup)
    bot.register_next_step_handler(message, get_babyone2)


#
def get_babyone2(message):
    babyone2 = message.text
    if message.text == 'Так':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_q2)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_q2(message):
    q2 = message.text
    if message.text == 'Хлопчик':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у нього день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl1)
    elif message.text == 'Дівчинка':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у неї день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl1)


def get_babyl1(message):
    babyl1 = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні")
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'У вас є ще дітки?', reply_markup=markup)
    bot.register_next_step_handler(message, get_babyone3)


#
def get_babyone3(message):
    babyone3 = message.text
    if message.text == 'Так':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_q2)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_q2(message):
    q2 = message.text
    if message.text == 'Хлопчик':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у нього день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl)
    elif message.text == 'Дівчинка':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у неї день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl)


def get_babyl2(message):
    babyl2 = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні")
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'У вас є ще дітки?', reply_markup=markup)
    bot.register_next_step_handler(message, get_babyone4)


#
def get_babyone4(message):
    babyone4 = message.text
    if message.text == 'Так':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_q4)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_q4(message):
    q4 = message.text
    if message.text == 'Хлопчик':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у нього день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl4)
    elif message.text == 'Дівчинка':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у неї день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl4)


def get_babyl4(message):
    babyl4 = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні")
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'У вас є ще дітки?', reply_markup=markup)
    bot.register_next_step_handler(message, get_babyone5)


def get_babyone5(message):
    babyone5 = message.text
    if message.text == 'Так':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_q5)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_q5(message):
    q5 = message.text
    if message.text == 'Хлопчик':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у нього день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl5)
    elif message.text == 'Дівчинка':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у неї день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl5)


def get_babyl5(message):
    babyl5 = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні")
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'У вас є ще дітки?', reply_markup=markup)
    bot.register_next_step_handler(message, get_babyone5)


#
def get_babyone6(message):
    babyone6 = message.text
    if message.text == 'Так':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Хлопчик")
        item2 = types.KeyboardButton("Дівчинка")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Хто у вас?', reply_markup=markup)
        bot.register_next_step_handler(message, get_q6)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Ви вагітна?', reply_markup=markup)
        bot.register_next_step_handler(message, get_vg2)


def get_q6(message):
    q6 = message.text
    if message.text == 'Хлопчик':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у нього день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl6)
    elif message.text == 'Дівчинка':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Коли у неї день народження?(в такому форматі- дд/мм/рррр)',
                         reply_markup=a)
        bot.register_next_step_handler(message, get_babyl6)


def get_vg(message):
    vg = message.text
    if message.text == 'Так':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'А на якому ви тижні?', reply_markup=a)
        bot.register_next_step_handler(message, get_week)
    elif message.text == 'Ні':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'А плануете?', reply_markup=a)
        bot.register_next_step_handler(message, get_plan)


def get_babyl6(message):
    babyl6 = message.text
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Так")
    item2 = types.KeyboardButton("Ні")
    markup.add(item1, item2)
    bot.send_message(message.from_user.id, 'У вас є ще дітки?', reply_markup=markup)
    bot.register_next_step_handler(message, get_babyone6)


def get_vg2(message):
    vg2 = message.text
    if message.text == 'Так':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'А на якому ви тижні?', reply_markup=a)
        bot.register_next_step_handler(message, get_week)
    elif message.text == 'Ні':
        markup = types.ReplyKeyboardMarkup(True, True)
        item1 = types.KeyboardButton("Так")
        item2 = types.KeyboardButton("Ні")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'А плануете?', reply_markup=markup)
        bot.register_next_step_handler(message, get_plan)


def get_plan(message):
    if message.text == 'Так':
        plan = 'Планує дитину'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Від подруги")
        item2 = types.KeyboardButton("Через соціальні мережі")
        item3 = types.KeyboardButton("Через рекламу у Google")
        item4 = types.KeyboardButton("Через розсилку")
        item5 = types.KeyboardButton("Через канал на YouTube")
        item6 = types.KeyboardButton("Через оффлайн рекламу")
        markup.add(item1, item2, item4, item5, item6)
        bot.send_message(message.from_user.id, 'Звідки ви дізнались про клуб', reply_markup=markup)
        bot.register_next_step_handler(message, get_PR)

    elif message.text == 'Ні':
        a = telebot.types.ReplyKeyboardRemove()
        plan == ' Не планує дитину'
        bot.send_message(message.from_user.id, 'Реєстрація закінчена', reply_markup=a)
        bot.send_message(message.from_user.id, 'Очікуйте на картку)')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Від подруги")
        item2 = types.KeyboardButton("Через соціальні мережі")
        item3 = types.KeyboardButton("Через рекламу у Google")
        item4 = types.KeyboardButton("Через розсилку")
        item5 = types.KeyboardButton("Через канал на YouTube")
        item6 = types.KeyboardButton("Через оффлайн рекламу")
        markup.add(item1, item2, item4, item5, item6)
        bot.send_message(message.from_user.id, 'Звідки ви дізнались про клуб', reply_markup=markup)
        bot.register_next_step_handler(message, get_PR)


def get_week(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Від подруги")
    item2 = types.KeyboardButton("Через соціальні мережі")
    item3 = types.KeyboardButton("Через рекламу у Google")
    item4 = types.KeyboardButton("Через розсилку")
    item5 = types.KeyboardButton("Через канал на YouTube")
    item6 = types.KeyboardButton("Через оффлайн рекламу")
    markup.add(item1, item2, item4, item5, item6)
    bot.send_message(message.from_user.id, 'Звідки ви дізнались про клуб', reply_markup=markup)
    bot.register_next_step_handler(message, get_reg)


def get_PR(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    item1 = types.KeyboardButton("Від подруги")
    item2 = types.KeyboardButton("Через соціальні мережі")
    item3 = types.KeyboardButton("Через рекламу у Google")
    item4 = types.KeyboardButton("Через розсилку")
    item5 = types.KeyboardButton("Через канал на YouTube")
    item6 = types.KeyboardButton("Через оффлайн рекламу")
    markup.add(item1, item2, item4, item5, item6)
    bot.send_message(message.from_user.id, 'Звідки ви дізнались про клуб', reply_markup=markup)
    bot.register_next_step_handler(message, get_reg)


def smm(message):
    if message.text == 'Від подруги':
        PR = 'Від подруги'
    elif message.text == 'Через соціальні мережі':
        PR = 'Через соціальні мережі'
    elif message.text == 'Через рекламу у Google':
        PR = 'Через рекламу у Google'
    elif message.text == 'Через розсилку':
        PR = 'Через розсилку'
    elif message.text == 'Через канал на YouTube':
        PR = 'Через канал на YouTube'
    elif message.text == 'Через оффлайн рекламу':
        PR = 'Через оффлайн рекламу'


def get_reg(message):
    global name
    text1 = message.from_user.id
    text2 = 'Ось ваша індивідуальна картка'
    text = name
    tatras = Image.open(R'C:\Х-\Foto.jpg')
    idraw = ImageDraw.Draw(tatras)
    font = ImageFont.truetype(R"C:\Windows\Fonts\arial.ttf", size=48)
    font2 = ImageFont.truetype(R"C:\Windows\Fonts\arial.ttf", size=28)
    idraw.text((350, 380), text, font=font)
    idraw.text((900, 10), str(text1), font=font2)
    tatras.save(R'C:\Х-\Foto5.jpg')
    img1 = io.open(R'C:\Х-\Foto5.jpg', 'rb')
    bot.send_photo(message.from_user.id, img1, caption=text2)


bot.polling(none_stop=True, interval=0)