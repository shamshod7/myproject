from pyrogram import Client, Filters


@Client.on_message(Filters.text & Filters.private)
def echo(client, message):
    message.reply(message.text)


@Client.on_message(Filters.text & Filters.private, group=1)
def echo_reversed(client, message):
    message.reply(message.text[::-1])
