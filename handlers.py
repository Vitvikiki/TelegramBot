from utility import get_keyboard


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text('Здравствуйте, {}! \n'
                           'Чем я могу вам помоч?'.format(bot.message.chat.first_name), reply_markup=get_keyboard())

def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)
