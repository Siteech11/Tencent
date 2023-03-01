import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os
from datetime import datetime

# Replace YOUR_TOKEN_HERE with your bot's API token
bot = telegram.Bot(token='6082427393:AAFjUF7VLejvM13FagNNoWLtqmM08LuoyA0')

aienv = os.getenv('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')
openai.api_key = "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"
completion = openai.Completion()

# Define a command handler for /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a chatbot. How can I help you today?")

# Define a message handler for text messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=ask(update.message.text))

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = 'The following is a chat between two users:\n\n'
    now = datetime.now()
    ampm = now.strftime("%M:%I %I")
    t = '[' + ampm + ']'
    prompt = f'{t}:{question}\n{t}:'
    response = completion.create(
        prompt=prompt, engine="text-davinci-003", stop=['\n'], temperature=0.7,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=250)
    answer = response.choices[0].text.strip()
    return answer

# Create an Updater object and attach the command and message handlers to it
updater = Updater(token='6082427393:AAFjUF7VLejvM13FagNNoWLtqmM08LuoyA0',
                  use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start polling for new messages from Telegram
updater.start_polling()
updater.idle()
