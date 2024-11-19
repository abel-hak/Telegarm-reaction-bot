from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from telethon import TelegramClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import asyncio

# Download VADER lexicon
nltk.download('vader_lexicon')

# Setup VADER for sentiment analysis
vader_analyzer = SentimentIntensityAnalyzer()

# Set up your own Telegram API credentials
api_id = '29149446'
api_hash = 'd4a95c48244165f660d8b4341f0c06b5'
channel_username = '@tikvahethiopia'

# Initialize the Telethon client
telethon_client = TelegramClient('session_name', api_id, api_hash)

# Function to analyze reactions
async def analyze_channel_reactions():
    await telethon_client.start()
    messages = await telethon_client.get_messages(channel_username, limit=100)  # Fetch the latest 100 messages

    reaction_counts = {}

    for message in messages:
        if message.reactions:  # Check if the message has reactions
            for reaction in message.reactions.results:
                emoji = str(reaction.reaction)  # Convert emoji to a string to use as a key
                count = reaction.count

                if emoji in reaction_counts:
                    reaction_counts[emoji] += count
                else:
                    reaction_counts[emoji] = count

    # Calculate total reactions
    total_reactions = sum(reaction_counts.values())

    result = "Reaction Analysis:\n"
    if total_reactions > 0:
        for emoji, count in reaction_counts.items():
            percentage = (count / total_reactions) * 100
            result += f"{emoji} - {count} reactions ({percentage:.2f}%)\n"
    else:
        result += "No reactions found."

    return result

# Telegram bot function
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(f'Hello, {user.first_name}! Use /analyze to see the reaction analysis of the channel.')

async def analyze(update: Update, context: CallbackContext):
    result = await analyze_channel_reactions()
    await update.message.reply_text(result)

async def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = Application.builder().token('7621658299:AAEw9RH4D7N14Zf0n7asbXYNUWqOjWpmbbQ').build()

    # Handlers for commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('analyze', analyze))

    # Run the bot until you press Ctrl-C
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
