from telegram.ext import Updater
from telegram.ext import CommandHandler

from settings import TOKEN

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Bot example text"
    )

def snake(update, context):
    context.bot.send_game(
        chat_id=update.effective_chat.id,
        game_short_name='snake'
    )

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    snake_handler = CommandHandler('snake', snake)
    dispatcher.add_handler(snake_handler)

    updater.start_polling()

main()