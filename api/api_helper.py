from data_classes.data_joke_types import MarkovJokeTypes, NeuroJokeTypes

# Your application specific imports
import environ

import logging

from telegram import Update
from telegram.ext import CallbackContext
from telegram import Bot

from .button_handler import btn_markov_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

import telegram
from .buttons_helper import generate_markov_button, generate_neuro_button

env = environ.Env(
    DEBUG=(bool, False)
)

import json

bot = Bot(token=env('bot_token'))
super_admin_id = env('super_admin_id')


def start(update: Update, context: CallbackContext):
    help(update, context)

def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    bot.send_message(chat_id=super_admin_id, text=context.error)

def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    text = """Бот для генерации тупых шуток
Для генерации просто нажми кнопку
@ogoltelyi_tusovshik по всем вопросам и ошибкам
код проекта: https://github.com/pupkin119/neuro_joke_bot
    """

    # if update._effective_chat['type'] == 'private':
    #     bot.send_message(chat_id=update.message.chat["id"], text=text)
    #
    # if update._effective_chat['type'] == 'group':
    group_id = update.message.chat["id"]

    buttons = []

    buttons.append([generate_markov_button({"type": MarkovJokeTypes.ranevstakay}, "Цитаты Раневской")])
    buttons.append([generate_markov_button({"type":  MarkovJokeTypes.sex_joke}, "Пошлые Марков")])
    buttons.append([generate_neuro_button({"type":  NeuroJokeTypes.sex_joke}, "Пошлые Нейронка")])

    if buttons == []:
        buttons = [[]]

    bot.send_message(
        chat_id=group_id,
        text=text,
        reply_markup=telegram.InlineKeyboardMarkup(buttons),
    )


def callback_query_handler(update: Update, context: CallbackContext):
    cqd = update.callback_query.data

    if cqd is not None:
        print(cqd)
        result = json.loads(cqd)
        if result['action'] == "markov":
            btn_markov_handler(update, result)
        if result['action'] == "neuro":
            btn_markov_handler(update, result)

        # command_handler_help(bot, update)
    # elif cqd == ... ### for other buttons

