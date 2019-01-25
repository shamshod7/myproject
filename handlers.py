def echo(client, message):
    message.reply(message.text)


def echo_reversed(client, message):
    message.reply(message.text[::-1])
