#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
led = 5
DHT_pin = 27

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, initial = 0)
# Enable logging
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
 #                   level=logging.INFO)

#logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def on(bot, update):
    """Send a message when the command /start is issued."""
    GPIO.output(led, GPIO.HIGH)
    update.message.reply_text('LED turned ON')


def off(bot, update):
    """Send a message when the command /help is issued."""
    GPIO.output(led, GPIO.LOW)
    update.message.reply_text('LED turned OFF')

def hum(bot, update):
    """Send a message when the command /hum is issued."""
    humidity = Adafruit_DHT.read_retry(11, DHT_pin)[0]
    update.message.reply_text("Humidity: {} %".format(humidity))

def temp(bot, update):
    """Send a message when the command /temp is issued."""
    temperature = Adafruit_DHT.read_retry(11, DHT_pin)[1]
    update.message.reply_text("Temperature: {} C".format(temperature))

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("Enter your token here")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("on", on))
    dp.add_handler(CommandHandler("off", off))
    dp.add_handler(CommandHandler("temp", temp))
    dp.add_handler(CommandHandler("hum", hum))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

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
