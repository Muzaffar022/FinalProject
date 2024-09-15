from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler, ConversationHandler
from apps.telegrambot import States
from apps.telegrambot.handlers import commands

BOT_TOKEN = "7276506721:AAG5yXemCAFCSn5cnBYsqz83hoeEK5GHnic"
bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(
    ConversationHandler(
        entry_points=[CommandHandler("start", commands.start)],
        states={
            States.PHONE: [MessageHandler(Filters.all, commands.get_phone)],
            States.FULL_NAME: [MessageHandler(Filters.all, commands.get_first_name)],
            States.PASSPORT: [MessageHandler(Filters.all, commands.get_passport)],
            States.PINFL: [MessageHandler(Filters.all, commands.get_pinfi)],
            States.GENDER: [MessageHandler(Filters.text, commands.get_gender)],
            States.BIRTH_DATE: [MessageHandler(Filters.text, commands.get_birth_date)],
        },
        fallbacks=[
            CommandHandler("cancel", commands.cancel),
            MessageHandler(Filters.all, commands.cancel)
        ]
    )
)

