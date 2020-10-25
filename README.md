# Telegram Snake Bot

A telegram game bot to play snake.

## Installation

### Local

To run this bot, you will need an environment with a python3 client and pip. Then you can install the required libraries:
```
pip[3] install -r requirements.txt
```

You will also need a Telegram Bot Token. You can get a token using the BotFather as indicated [here](https://core.telegram.org/bots). Once you have the Token create a file named settings.py and add the following line with your actual token value:
```
TOKEN = "<Your Actual Token>"
```

Once you have all the necessary requirements just run:
```
python[3] snake_bot.py
``` 

### Docker Deployment

You can deploy the bot in a docker container. This option means you do not need any of the python requirements, but it requires a [docker application](https://docs.docker.com/get-docker/).   

Same as before you will have to add your telegram bot token to the settings.py file, so that it contains:
```
TOKEN = "<Your token>"
```

Then you will have to build the docker image by executing in the repository folder:
```
docker build -t telegram_bot/snake .
```
The -t option serves to tag the generated image so it can be easily accesible later. If you do not like the name feel free to change it. Just remember to leave the "." at the end of the command.

And the final step is to run a container with the generated docker image. If you gave the image a different name than this guide, remember to adapt this command as well.
```
docker run telegram_bot/snake
```

Now the bot should be successfully deployed in a docker container and ready to be used. If you want to know more about docker and what it offers, be sure to check [their official documentation](https://docs.docker.com/).

## Usage

To call the bot, start a chat with it. Then you can execute the following methods.

### Start

Tell the bot "/start" or "/game" and it will answer with a link to the Snake game.

### Help

Tell the bot "/help" and it will list you the available commands.

### Play Snake

The Play Snake button redirects you to the snake game url. If you have a keyboard, you may use the arrows to control the direction of the snake, if you have a touch screen you may use the page buttons.  