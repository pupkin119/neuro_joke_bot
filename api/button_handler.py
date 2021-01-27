# from .game_api_helper import end_game_func, is_end_game, bot
from data_classes.data_joke_types import MarkovJokeTypes, NeuroJokeTypes
import telegram
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

from telegram.ext import  CommandHandler, MessageHandler, Filters, CallbackContext

from random import randint
import environ
from telegram import Update
from telegram import Bot

from markov import markov_chain
from constants import PROJECT_DIR

env = environ.Env(
    DEBUG=(bool, False)
)

bot = Bot(token=env('bot_token'))

mc = markov_chain.MarkovChain()
# with open('corpus/proverbs', 'r') as c:
# with open('corpus/bugurt', 'r') as c:
with open(f'{PROJECT_DIR}/corpus/jokes1', 'r') as c:
    for line in c.readlines():
        if line == "\n":
            continue
        mc.parse_and_add(line.strip())


def get_group_id(update):
    return update.callback_query.message.chat['id']


def btn_markov_handler(update, options):
    # {'action': 'vote', 'group_id': -451618097, 'vote': 1}
    user = update._effective_user
    group_id = update.callback_query.message.chat['id']

    joke_type = options['type']
    text = ""
    if joke_type == MarkovJokeTypes.ranevstakay:
        for i in range(20):
            text += '*** \n'
            text += (mc.generate_sentence(150))
            text += "\n"

    elif joke_type == MarkovJokeTypes.sex_joke:
        for i in range(20):
            text += '*** \n'
            text += (mc.generate_sentence(150))
            text += "\n"

    bot.send_message(
        chat_id=group_id,
        text=text
    )


def btn_neuro_handler(update, options):
    # {'action': 'vote', 'group_id': -451618097, 'vote': 1}
    user = update._effective_user
    group_id = update.callback_query.message.chat['id']

    joke_type = options['type']
    text = ""
    if joke_type == NeuroJokeTypes.sex_joke:
        pass



    bot.send_message(
        chat_id=group_id,
        text=text
    )