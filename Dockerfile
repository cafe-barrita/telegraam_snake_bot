FROM python:3.7

RUN mkdir /etc/telegram_snake_bot
ENV BOT_DIR=/etc/telegram_snake_bot
WORKDIR $BOT_DIR
ADD ./* $BOT_DIR/
RUN pip install -r requirements.txt

CMD ["python", "snake_bot.py"]