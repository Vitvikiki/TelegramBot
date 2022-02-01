from telegram import ReplyKeyboardMarkup

def get_keyboard():

    my_keyboard = ReplyKeyboardMarkup([['Начать'], ['Информация'], ['Заполнить анкету']], request_contact=True)
    return my_keyboard