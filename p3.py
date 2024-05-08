from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, Updater, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes
import random

with open('token.txt', 'r') as file:
    api_token = file.read().strip()

TOKEN: Final[str] = api_token
BOT_USERNAME: Final[str] = '@YOUR_BOTS_NAME'



# List of your Opps
opps = [
    "Harry Potter.",
"Gandalf.",
"Thanos.",
"Zattana.",
"Naruto.",
"Goku.",
"Tiamat.",
"Gojira a.k.a Godzilla.",
"Mahoraga",
"Jeremy Wade-no Context",
"Being broke- Omoka manzee",
"Njaa",
"The World - It giving mixed feelings, like damn. Dj, play : Do you want me"
    # Add more opps here, them finna catch these hands...
]

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm The Opp Bot")

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I randomly generate some of the opps who finna catch some hands. Type / or click /help for instructions')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    Commands for using the Opp Bot:
    /start -> Welcome message
    /about -> Information about myself
    /help -> Give instructions of use
    /opp -> Randomly generates a listed opp
    /contact ->Contact us

    If in a group, tag to get a response, '@Opp_bot'
    To have the bot function in a group, set it as an admin.

    Don't write the bots name or username when privately texting.
    Type '/' for the list of commands to be given
    """)

async def opp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get a random opp from the list
    random_proverb = random.choice(opps)
    
    # Sends the opp as a reply
    await update.message.reply_text(random_proverb)


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Can contact us at: africanadage254@gmail.com')

# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello! I am The Opp bot.'
    if 'Hey' in processed:
        return "Wassup? I've got opps listed for you gang?" 
    if 'how are you.' in processed:
        return 'Aight bro, what in the kienyeji do you want?'
    if 'what can you do' in processed:
        return 'I can generate randomly generate opps'
    if 'habari' in processed:
        return 'Mzuri sana'
    if 'niaje bazenga' in processed:
        return 'Fiti bazuu'
    if 'niaje bazenga?' in processed:
        return 'Fiti bazuu'
    if 'rada gathee?' in processed:
        return 'Fiti Gathee'
    if 'bonjur?' in processed:
        return "Bonjur, that's the only thing I know in French, /help for instructions"
    if 'hola?' in processed:
        return 'Hola amigo!'

    if 'help' in processed:
        return 'click /help'
    if 'start' in processed:
        return 'click /start '
    if 'instruction' in processed:
        return 'click /help'
    if 'command' in processed:
        return 'click /help'


    if 'opp' in processed:
        return 'Sawa click or type /opp'
    if 'nipee opp' in processed:
        return 'Sawa click or type /opp'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message. text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return


    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = ApplicationBuilder().token(api_token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('about', about_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('opp', opp_command))
    app.add_handler(CommandHandler('contact', contact_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
