from telethon import TelegramClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import re
from datetime import datetime

# Download VADER lexicon
nltk.download('vader_lexicon')

# Setup VADER for sentiment analysis
vader_analyzer = SentimentIntensityAnalyzer()

# Set up your own Telegram API credentials
api_id = '29149446'
api_hash = 'd4a95c48244165f660d8b4341f0c06b5'
channel_username = '@tikvahethiopia'

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

async def analyze_channel_reactions():
    await client.start()

    reaction_counts = {}

    # Regular expression to match specific keywords
    pattern = re.compile(r'ዐቢይ አሕመድ', re.UNICODE)  # Replace with your desired keyword(s)

    # Debug: Count of messages checked
    checked_message_count = 0

    # Fetch messages in a loop until all messages from 2024 are processed
    async for message in client.iter_messages(channel_username):
        # Check if the message date is in 2024
        if message.date and message.date.year == 2024:
            if message.message and pattern.search(message.message):  # Search for the pattern in the message content
                checked_message_count += 1

                if message.reactions:  # Check if the message has reactions
                    for reaction in message.reactions.results:
                        emoji = str(reaction.reaction)  # Convert emoji to a string to use as a key
                        count = reaction.count

                        if emoji in reaction_counts:
                            reaction_counts[emoji] += count
                        else:
                            reaction_counts[emoji] = count
        else:
            # Stop fetching once we're past 2024
            if message.date and message.date.year < 2024:
                break

    # Display the total number of checked messages
    print(f"Total messages checked containing the keyword in 2024: {checked_message_count}")

    # Calculate total reactions
    total_reactions = sum(reaction_counts.values())

    # Display reaction numbers and percentages
    if total_reactions > 0:
        print("Reaction Analysis:")
        for emoji, count in reaction_counts.items():
            percentage = (count / total_reactions) * 100
            print(f"{emoji} - {count} reactions ({percentage:.2f}%)")
    else:
        print("No reactions found for messages containing the specified keyword(s) in 2024.")

with client:
    client.loop.run_until_complete(analyze_channel_reactions())
