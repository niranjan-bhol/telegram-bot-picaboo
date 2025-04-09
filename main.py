from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time

with open('token.txt', 'r') as Token:
    TOKEN = Token.read()

updater = Updater(TOKEN,
        use_context=True)

# Start
def start(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text(
		"Hi there, I am a Bot..!!")
    time.sleep(0.5)
    update.message.reply_text("Select an Option:\n/Print_Text\n/Send_document")

# Functions
def text(update: Update, context: CallbackContext):
    update.message.reply_text("This is text message.")

def document(update: Update, context: CallbackContext):
    update.message.reply_document('https://t.me/test_channel_143/2')   # replace 'https://t.me/test_channel_143/2' with your file link

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
         "Sorry '%s' is not a valid command" % update.message.text)

# #####
updater.dispatcher.add_handler(CommandHandler('start', start))

# Content
updater.dispatcher.add_handler(CommandHandler('Print_Text', text))
updater.dispatcher.add_handler(CommandHandler('Send_Document', document))

# Filters out unknown commands & messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# updater.start_polling
updater.start_polling()

print("Bot is Running")

