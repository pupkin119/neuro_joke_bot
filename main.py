# Django specific settings
from telegram import Update
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env('.env')

# Your application specific imports
from telegram.ext import Updater

from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

import logging
import numpy as np

import random

import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Bot
from api.api_helper import help, callback_query_handler, start, error

bot = Bot(token=env('bot_token'))

# updater = Updater(token=env('bot_token'), request_kwargs=REQUEST_KWARGS)
# updater = Updater(token=env('bot_token'), use_context=True, request_kwargs=REQUEST_KWARGS)
updater = Updater(token=env('bot_token'), use_context=True)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)




def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    # Get the dispatcher to register handlers
    dp = updater.dispatcher


    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(telegram.ext.CallbackQueryHandler(callback_query_handler))
    # dp.add_handler(MessageHandler(Filters.text | Filters.photo, get_input))
    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()