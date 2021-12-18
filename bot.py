from telegram.ext import Updater, CommandeHandler, MessageHandler, Filters
from settings import TG_TOKEN


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text('Здравствуйте, я бот! \n'
                           'Поговори со мной!'.format(bot.message.chat.first_name))


def main():
    my_bot = Updater(TG_TOKEN)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()
    my_bot.idle()


main()