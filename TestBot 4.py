from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application ,CommandHandler, ContextTypes, MessageHandler,filters
import os   
import google.genai as genai    
import dotenv
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN4')
API_KEY = os.getenv('GEMINI_API_1')
client = genai.Client(api_key=API_KEY)  
# for m in client.models.list():
#     print(m.name)
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    wait_msg = await update.message.reply_text("🤔 Processing your query, please wait...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=update.message.text
    )
    # response = client.models.list()
    await wait_msg.edit_text(response.text)
app=Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler( ~filters.COMMAND, generate))           
app.run_polling()
