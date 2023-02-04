import telebot
from telebot import types
from datetime import datetime
import Currency

TKN = telebot.TeleBot('6101267878:AAGN7STTjkUm072TtYvCUDh9hVd1Ip6LcTg')


@TKN.message_handler(content_types=['text'])
def get_text_messages(message):  # Bot behavior on user requests
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(
        text='Find out the exchange rate', callback_data='info')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Nothing', callback_data='close')
    keyboard.add(key2)
    if message.text == '/start':
        TKN.send_message(message.from_user.id, 'Hello. I am a Telegram bot of the exchange rate of Belarusbank. ' +
                         'Sorry if I can slow down - I was created in an underground laboratory. Please contact me for further work.')
    elif message.text == 'Hello' or message.text == 'hello' or message.text == 'Hi' or message.text == 'hi':
        TKN.send_message(message.from_user.id,
                         'Hi, can i help you?', reply_markup=keyboard)
    elif message.text == '/help':
        TKN.send_message(message.from_user.id, 'Write Hello')
    else:
        TKN.send_message(message.from_user.id,
                         'I don\'t understand. Write /help or Hello')


@TKN.callback_query_handler(func=lambda call: True)
def iq_callback(query):  # Adding buttons and making them interactive
    keyboard2 = types.InlineKeyboardMarkup()
    key3 = types.InlineKeyboardButton(text='USD', callback_data='get-USD')
    keyboard2.add(key3)
    key4 = types.InlineKeyboardButton(text='EUR', callback_data='get-EUR')
    keyboard2.add(key4)
    key5 = types.InlineKeyboardButton(text='RUB', callback_data='get-RUB')
    keyboard2.add(key5)
    key5 = types.InlineKeyboardButton(text='BYN', callback_data='get-GBP')
    keyboard2.add(key5)
    key5 = types.InlineKeyboardButton(text='PLN', callback_data='get-PLN')
    keyboard2.add(key5)
    data = query.data
    if data == 'exite':
        TKN.send_message(query.message.chat.id, 'Good luck  :)')
    if data == 'info':
        TKN.send_message(query.message.chat.id,
                         'Select currency:', reply_markup=keyboard2)
    if data == 'close':
        TKN.send_message(query.message.chat.id, 'See you!')
    if data.startswith('get-'):
        get_ex_callback(query)
    if data == 'back':
        TKN.send_message(query.message.chat.id,
                         'Select currency:', reply_markup=keyboard2)


def get_ex_callback(query):  # intermediate function
    TKN.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])


# Intermediate function for getting data
def send_exchange_result(message, ex_code):
    TKN.send_chat_action(message.chat.id, 'typing')
    usd = Currency.usd_info
    eur = Currency.eur_info
    rub = Currency.rub_info
    byn = Currency.byn_info
    pln = Currency.pln_info
    TKN.send_message(
        message.chat.id, text_currency(usd, eur, rub, byn, pln, ex_code),
        reply_markup=again_keyboard(),
        parse_mode='HTML'
    )


def again_keyboard():  # Adding buttons again
    keyboard3 = types.InlineKeyboardMarkup()
    key6 = types.InlineKeyboardButton(text='Back', callback_data='back')
    keyboard3.add(key6)
    key7 = types.InlineKeyboardButton(text='Exite', callback_data='exite')
    keyboard3.add(key7)
    return keyboard3


# The function of displaying the result at the request of the user with the current time
def text_currency(usd, eur, rub, byn, pln, ex_code):
    time = (str(datetime.now().hour) + ':' + str(datetime.now().minute) +
            ':' + str(datetime.now().second))
    date = str(datetime.now().date())
    if ex_code == 'USD':
        return ('Belarusbank rate' + '\n\n' + 'USD buy: ' + usd[0] + '\n' + 'USD sale: ' + usd[1] + '\n\n' + date + '  ' + time)
    if ex_code == 'EUR':
        return ('Belarusbank rate' + '\n\n' + 'EUR buy: ' + eur[0] + '\n' + 'EUR sale: ' + eur[1] + '\n\n' + date + '  ' + time)
    if ex_code == 'RUB':
        return ('Belarusbank rate' + '\n\n' + 'RUB buy: ' + rub[0] + '\n' + 'RUB sale: ' + rub[1] + '\n\n' + date + '  ' + time)
    if ex_code == 'GBP':
        return ('Belarusbank rate' + '\n\n' + 'BYN buy: ' + byn[0] + '\n' + 'BYN sale: ' + byn[1] + '\n\n' + date + '  ' + time)
    if ex_code == 'PLN':
        return ('Belarusbank rate' + '\n\n' + 'PLN buy: ' + pln[0] + '\n' + 'PLN sale: ' + pln[1] + '\n\n' + date + '  ' + time)


TKN.polling(none_stop=True, interval=0)
