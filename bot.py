from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from settings import TG_TOKEN
from handlers import *




def main():
    my_bot = Updater(TG_TOKEN)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()