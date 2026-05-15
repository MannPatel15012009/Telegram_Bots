import os

from telegram import Update
from telegram.ext import Application, CommandHandler, filters, ContextTypes

TOKEN = os.environ.get('TOKEN2')
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num1=int(context.args[0])
    num2=int(context.args[1])   
    result=num1+num2
    await update.message.reply_text(f"The sum of {num1} and {num2} is {result}")
async def subtract(update: Update, context: ContextTypes.DEFAULT_TYPE):     
    num1=int(context.args[0])
    num2=int(context.args[1])   
    result=num1-num2
    await update.message.reply_text(f"The difference of {num1} and {num2} is {result}")
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("subtract", subtract))

print("Bot is running...")

app.run_polling()             