from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import json
import random
import string

from telegram.ext import CallbackContext
# izveido bota pieslēgumu Telegram
app = ApplicationBuilder().token("7012624613:AAE99uS7aVj_Ldqai9UzoegoJvxq-bnizpM").build()

#функции:
async def jokes_data():
    with open('jokes.json', 'r', encoding='utf-8') as joke_file:
        jokes = json.load(joke_file)
    random_joke = random.choice(jokes)
    return random_joke['joke']
async def lifehacks_data():
    with open('life_hacks.json', 'r', encoding='utf-8') as lifehacks_file:
        lifehacks = json.load(lifehacks_file)
    random_lifehacks = random.choice(lifehacks)
    return random_lifehacks['life hacks']
async def quotations_data():
    with open('quotations.json', 'r', encoding='utf-8') as quotation_file:
        quotation = json.load(quotation_file)
    random_quotations = random.choice(quotation)
    return random_quotations['quotation']
async def advices_data():
    with open('advices.json', 'r', encoding='utf-8') as advices_file:
        advices = json.load(advices_file)
    random_advices = random.choice(advices)
    return random_advices['advices']
async def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    generated_password = generate_password(length)
    print("Your password:", generated_password)
    return password
async def quotations_author_data():
    with open('quotations.json', 'r', encoding='utf-8') as quotation_author_file:
        quotation_author = json.load(quotation_author_file)
    random_quotations_author = random.choice(quotation_author)
    return random_quotations_author['quotation'], random_quotations_author['author'] 
    
    
    

    

#телеграм команды:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and to ask the user what he wants to hear."""
    reply_keyboard = [["/jokes", "/quotations"],
                      ["/advices", "/lifehacks"],
                      ["/password"],]

    await update.message.reply_text(
        "Hi! My name is Rykola Bot. I will hold a conversation with you. "
        "What do you want jokes/quotes/advice/lifehacks or random password?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder=""
        ),
    )

 
async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text(await jokes_data())

async def lifehacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text(await lifehacks_data())

async def quotations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text(await quotations_data())

async def quotations_author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotation, author = await quotations_author_data()
    response = f"{quotation}\n— {author}"
    await update.message.reply_text(response)

async def advices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text(await advices_data())

async def password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text(await generate_password(10))

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text("Hello", update.effective_user.first_name)


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Retrieve passport data
    text = update.message.text
    print(text)
    await update.message.reply_text("What? press /help for a list of commands ")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Here's a list of commands: 1. /start - starts the bot "
                                    "2. /help - shows and explains commands "
                                    "3. /jokes - gives a random joke from the library "
                                    "4. /quotations - gives a random quote from the library "
                                    "5. /advices - gives random advice from the library "
                                    "6. /lifehacks - generates a random lifehack from the library "
                                    "7. /password - generates a random password of 10 characters. "
                                    "8. /quotations_author - random quotation with the author's indication "
                                    "9. /echo - responds that it hears the user's message"
                                    "10. /few_jokes - gives a certain number of jokes that the user chooses.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text =  update.message.text.replace("/echo ", "")
    await update.message.reply_text("I hear: " + text)

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Sorry, I don't know this command. Please use /help for a list of available commands.")

async def few_jokes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    txt = update.message.text
    txt = txt.replace("/few_jokes ", "")
  
    if txt.isdigit() == False:  #pārbauda, vai lietotāja ievadītais teksts nav cipars.
        await update.message.reply_text("It's not a number.")
        return
    
    with open('jokes.json', 'r', encoding='utf-8') as jokes_file:
        joke = json.load(jokes_file)
   
    for i in range(int(txt)):  #tas izvēlas nejaušus jokus, kuru skaitu izvēlas lietotājs.
        random_jokes = random.choice(joke)
        await update.message.reply_text(random_jokes['joke'])

    return random_jokes['joke']







    

# savieno čata komandu ar funkciju
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jokes", jokes)) # /few_jokes 3
app.add_handler(CommandHandler("lifehacks", lifehacks))
app.add_handler(CommandHandler("quotations", quotations))
app.add_handler(CommandHandler("advices", advices))
app.add_handler(CommandHandler("password", password))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("quotations_author", quotations_author))
app.add_handler(CommandHandler("echo", echo))
app.add_handler(CommandHandler("few_jokes", few_jokes))
app.add_handler(MessageHandler(filters.COMMAND, unknown_command))


app.add_handler(MessageHandler(filters.TEXT, answer)) # type: ignore

# sāk bota darbību
app.run_polling() 
