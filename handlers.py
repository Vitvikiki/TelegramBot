from random import choice

from mongodb import mdb, search_or_save_user, save_user_anketa
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode
from glob import glob
from telegram.ext import ConversationHandler

from utility import get_keyboard

def sms(bot, update):
    user = search_or_save_user(mdb, bot.effective_user, bot.message)
    print(user)

    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text('Здравствуйте, {}! \n'
                           'Чем я могу вам помоч?'.format(bot.message.chat.first_name), reply_markup=get_keyboard())

def send_meme(bot, update):
    lists = glob('images/11.jpg')
    picture = choice(lists)
    update.bot.send_photo(chat_id=bot.message.chat.id, photo=open(picture, 'rb'))


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)

def anketa_start(bot, update):
    bot.message.reply_text('Введите ваше имя', reply_markup=ReplyKeyboardRemove())
    return "user_name"

def anketa_get_name(bot, update):
    update.user_data['name'] = bot.message.text
    bot.message.reply_text("Введите вашу фамилию")
    return "user_surname"

def anketa_get_surname(bot, update):
    update.user_data['surname'] = bot.message.text
    bot.message.reply_text("Введите вашу дату рождения")
    return "user_DoB"

def anketa_get_DoB(bot, update):
    update.user_data['DoB'] = bot.message.text
    reply_keyboard = [["1", "2", "3", "4", "5"]]
    bot.message.reply_text(
        "Оцените статью от 1 до 5",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
    return "evaluation"

def anketa_get_evaluation(bot, update):
    update.user_data['evaluation'] = bot.message.text
    reply_keyboard = [["Пропустить"]]
    bot.message.reply_text("Напишите отзыв или нажмите кнопку пропустить этот шаг.",
                           reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
    return "comment"

def anketa_comment(bot, update):
    update.user_data['comment'] = bot.message.text

    user = search_or_save_user(mdb, bot.effective_user, bot.message)
    anketa = save_user_anketa(mdb, user, update.user_data)
    print(anketa)

    text = """Результат опроса:
    <b>Имя:</b> {name}
    <b>Фамилия:</b> {surname}
    <b>Дата рождения:</b> {DoB}
    <b>Оценка:</b> {evaluation}
    <b>Текст сообщения:</b> {comment}
    """.format(**update.user_data)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text("Спасибо вам за комментарий!", reply_markup=get_keyboard())
    return ConversationHandler.END

def anketa_exit_comment(bot, update):

    update.user_data['comment'] = None
    user = search_or_save_user(mdb, bot.effective_user, bot.message)
    save_user_anketa(mdb, user, update.user_data)

    text = """Результат опроса:
    <b>Имя:</b> {name}
    <b>Фамилия:</b> {surname}
    <b>Дата рождения:</b> {DoB}
    <b>Оценка:</b> {evaluation}
    """.format(**update.user_data)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text("Спасибо!", reply_markup=get_keyboard())
    return ConversationHandler.END

def dontknow(bot, update):
    bot.message.reply_text("Я вас не понимаю, выберите оценку на клавиатуре!")
