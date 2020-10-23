from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler

from settings import TOKEN


def start(update, context):
    context.bot.send_game(
        chat_id=update.effective_chat.id,
        game_short_name='snake'
    )

def help_command(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Use /start or /game to get a link to the Snake game."
    )

def snake(update, context):
    query_id = update.callback_query.id
    context.bot.answer_callback_query(
        callback_query_id=query_id,
        url="https://htmlpreview.github.io/?https://github.com/cafe-barrita/telegram_snake_bot/blob/main/snake.html"
    )

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    game_handler = CommandHandler('game', start)
    dispatcher.add_handler(game_handler)

    help_handler = CommandHandler('help', help_command)
    dispatcher.add_handler(help_handler)

    snake_handler = CallbackQueryHandler(snake)
    dispatcher.add_handler(snake_handler)

    updater.start_polling()

main()