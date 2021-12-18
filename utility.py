from telegram import ReplyKeyboardMarkup

def get_keyboard():

    my_keyboard = ReplyKeyboardMarkup([['Информация', 'Заполните анкету']], request_contact=True)
    return my_keyboard