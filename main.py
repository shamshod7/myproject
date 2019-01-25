from pyrogram import Client, MessageHandler, Filters

from handlers import echo, echo_reversed

app = Client("my_account")

app.add_handler(
    MessageHandler(
        echo,
        Filters.text & Filters.private))

app.add_handler(
    MessageHandler(
        echo_reversed,
        Filters.text & Filters.private),
    group=1)

app.run()
