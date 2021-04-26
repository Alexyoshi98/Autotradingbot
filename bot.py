import telegram
bot  =  telegram . Bot ( token = '1654462214:AAF2-p-vdJuXTVS8PfdakiiCHQSR_USiyS0' )

from telegram.ext import Updater
updater = Updater(token='1654462214:AAF2-p-vdJuXTVS8PfdakiiCHQSR_USiyS0', use_context=True)
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenid@ a la version demo del primer robot de Matayoshi. Usted está siendo testigo del comienzo como programador del mejor crack de la historia, vaya suerte que tiene...")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()                

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)