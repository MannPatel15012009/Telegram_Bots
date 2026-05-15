from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters 
import os

TOKEN = os.environ.get('TOKEN1')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot is running...")

app.run_polling()