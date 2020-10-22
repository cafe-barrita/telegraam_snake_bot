from telegram.ext import Updater

TOKEN = 'TOKEN'

def main():
    updater = Updater(token=TOKEN, use_context=True)

main()