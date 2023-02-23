import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace YOUR_TOKEN_HERE with your bot's API token
bot = telegram.Bot(token='6082427393:AAFjUF7VLejvM13FagNNoWLtqmM08LuoyA0')

# Define a command handler for /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a chatbot. How can I help you today?")

# Define a message handler for text messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Create an Updater object and attach the command and message handlers to it
updater = Updater(token='6082427393:AAFjUF7VLejvM13FagNNoWLtqmM08LuoyA0',
                  use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start polling for new messages from Telegram
updater.start_polling()
updater.idle()