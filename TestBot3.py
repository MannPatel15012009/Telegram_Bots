from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes         
TOKEN = os.environ.get('TOKEN3')
async def main():
    print("Bot is running...")