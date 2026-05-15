from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters 
import os
from sympy import sympify

TOKEN = os.environ.get('TOKEN3')

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # print(f"Received message: {update.message}")
    await update.message.reply_text(str(sympify(update.message.text)))

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler( filters.TEXT & ~filters.COMMAND, calculate))

print("Bot is running...")

app.run_polling()   
