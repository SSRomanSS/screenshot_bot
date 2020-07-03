import telebot
import re
from CONFIG import token
from screenshot import ScreenShot

bot = telebot.TeleBot(token)


def validator(message):
    """Validate inputted url"""
    reg_url = r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    return re.match(reg_url, message.text)


@bot.message_handler(commands=['start'])
def command_help(message):
    bot.reply_to(message, 'Hello, I`ll take screenshot for you. Sent url')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def default_command(message):
    if validator(message):
        bot.reply_to(message, f'This is screenshot of {message.text}')


def listener(messages):
    """When new messages arrive TeleBot will call this function."""
    for m in messages:
        if m.content_type == 'text' and m.text != '/start':
            chat_id = m.chat.id
            if validator(m):
                text = m.text
                ScreenShot(text).fullpage_screenshot()
                photo_name = ScreenShot(text).get_photo_name()
                photo = open(f'{photo_name}.png', 'rb')
                bot.send_document(chat_id, photo)
                ScreenShot(text).delete_photo()
            else:
                bot.reply_to(m, 'Input correct url')


bot.set_update_listener(listener)
bot.polling(none_stop=True)

while True:
    pass
