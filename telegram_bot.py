from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# izveido bota pieslēgumu Telegram
app = ApplicationBuilder().token("7012624613:AAE99uS7aVj_Ldqai9UzoegoJvxq-bnizpM").build()

# # komanda /start
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("I'm test bot. Type /hello or /echo")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [["Boy", "Girl", "Other"]]

    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you. "
        "Send /cancel to stop talking to me.\n\n"
        "Are you a boy or a girl?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Boy or Girl?"
        ),
    )

# savieno čata komandu ar funkciju
app.add_handler(CommandHandler("start", start))

# sāk bota darbību
app.run_polling() 