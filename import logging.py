import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from tokenfinderbot.tokenfinderbot import TokenBot

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your Telegram bot token
TELEGRAM_TOKEN = '6603797213:AAFYoHR8lj4VdZ9qjmO6wrWzFj9eCBMN0LM'

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Starting the TokenBot...')
    
    # Create an instance of TokenBot and run it
    bot = TokenBot()
    bot.run()

    # Send a confirmation message
    update.message.reply_text('TokenBot has been started with default settings.')

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
