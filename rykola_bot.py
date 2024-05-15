from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import json
import random

# izveido bota pieslēgumu Telegram
app = ApplicationBuilder().token("7012624613:AAE99uS7aVj_Ldqai9UzoegoJvxq-bnizpM").build()

#функции:
async def jokes_la():
    with open('jokes.json', 'r', encoding='utf-8') as joke_file:
        jokes = json.load(joke_file)
    random_joke = random.choice(jokes)
    return random_joke['joke']




#телеграм команды:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and to ask the user what he wants to hear."""
    reply_keyboard = [["/jokes", "/quotations"],
                      ["/advices", "/life hacks"]]

    await update.message.reply_text(
        "Hi! My name is Rykola Bot. I will hold a conversation with you. "
        "What do you want jokes/quotes/advice/lifehacks?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="jokes or quotes or advice or lifehacks?"
        ),
    )

 
async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text(await jokes_la())


async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Retrieve passport data
    text = update.message.text
    print(text)
    await update.message.reply_text("What? Let me tell a joke/quote/advice/lifehack.")

    

# savieno čata komandu ar funkciju
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jokes", jokes))
# app.add_handler(CommandHandler("echo", echo))
app.add_handler(MessageHandler(filters.TEXT, msg)) # type: ignore

# sāk bota darbību
app.run_polling() 
