import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "8502027930:AAEc4YWFsD6kEKQFztMXl1f4Oqw3F150iTQ"

logging.basicConfig(level=logging.INFO)

async def start(update, context):
    await update.message.reply_text("👋 Hello! I'm your Real Estate Bot. How can I help you today?")

async def reply(update, context):
    user_text = update.message.text
    await update.message.reply_text(f"You said: {user_text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    app.run_polling()

if __name__ == "__main__":
    main()
