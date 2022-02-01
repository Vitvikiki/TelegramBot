from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from settings import TG_TOKEN
from handlers import *



def main():
    my_bot = Updater(TG_TOKEN, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Заполнить анкету'), anketa_start)],
                                                      states={"user_name": [MessageHandler(Filters.text, anketa_get_name)],
                                                              "user_surname": [MessageHandler(Filters.text, anketa_get_surname)],
                                                              "user_DoB": [MessageHandler(Filters.text, anketa_get_DoB)],
                                                              "evaluation": [MessageHandler(Filters.regex('1|2|3|4|5'), anketa_get_evaluation)],
                                                              "comment": [MessageHandler(Filters.regex('Пропустить'), anketa_exit_comment),
                                                                          MessageHandler(Filters.text, anketa_comment)]
                                                              },
                                                      fallbacks=[MessageHandler(
                                                          Filters.text | Filters.video | Filters.photo | Filters.document, dontknow)]
                                                      )
                                  )
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Информация'), send_meme))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()