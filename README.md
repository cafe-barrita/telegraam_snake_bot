# Telegram Snake Bot

A telegram game bot to play snake.

## Installation

To run this bot, you will need an environment with a python3 client and pip. Then you can install the required libraries:
```pip[3] install -r requirements.txt
```

You will also need a Telegram Bot Token. You can get a token using the BotFather as indicated [here](https://core.telegram.org/bots). Once you have the Token create a file named settings.py and add the following line with your actual token value:
```TOKEN = "<Your Actual Token>"
```

Once you have all the necessary requirements just run:
```python[3] snake_bot.py
``` 

## Usage

To call the bot, start a chat with it. Then you can execute the following methods.

### Start

Tell the bot "/start" or "/game" and it will answer with a link to the Snake game.

### Help

Tell the bot "/help" and it will list you the available commands.

### Play Snake

The Play Snake button redirects you to the snake game url. Unfortunately, it is still under developing.