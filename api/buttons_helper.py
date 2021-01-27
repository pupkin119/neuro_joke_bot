

# Your application specific imports
import environ
import logging
import numpy as np
from telegram import Update
from telegram import Bot
from numpy.random import randint

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
import json

# convert to string
input = json.dumps({'id': 123})

HELP_BUTTON_CALLBACK_DATA = input

env = environ.Env(
    DEBUG=(bool, False)
)
bot = Bot(token=env('bot_token'))
super_admin_id = env('super_admin_id')
import telegram


def get_group_id(update: Update):
    return update.message.chat['id']


def generate_button(options, text: str):
    callback_data = json.dumps(options)
    standart_button = telegram.InlineKeyboardButton(
        text=text,  # text that show to user
        callback_data=callback_data  # text that send to bot when user tap button
    )
    return standart_button


def generate_markov_button(options, text):
    callback_dict = {"action": "markov"}
    callback_dict.update(options)
    return generate_button(callback_dict, text)


def generate_neuro_button(options, text):
    callback_dict = {"action": "neuro"}
    callback_dict.update(options)
    return generate_button(callback_dict, text)
