````markdown
# Telegram Reaction Analyzer

This script is designed to analyze reactions to messages in a specific Telegram channel for the year 2024. It uses the Telethon library to fetch messages and reactions and performs sentiment analysis with NLTK's VADER. It also allows for keyword-based message filtering.

## Features

- Fetches all messages from a specified Telegram channel.
- Filters messages containing specific keywords using regular expressions.
- Analyzes the reactions to the filtered messages.
- Provides a detailed breakdown of reaction counts and percentages.
- Ensures only messages from the year 2024 are processed.

## Prerequisites

1. **Python 3.8 or higher**
2. **Required Python libraries**:
   - `telethon`
   - `nltk`
3. **Telegram API credentials**:
   - API ID and API hash from the [Telegram API Development Tools](https://my.telegram.org/).

## Installation

1. Clone this repository or copy the script.
2. Install the required libraries:
   ```bash
   pip install telethon nltk
   ```
````

3. Download the NLTK VADER lexicon:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## Setup

1. Replace the following placeholders with your Telegram API credentials:
   ```python
   api_id = 'your_api_id'
   api_hash = 'your_api_hash'
   ```
2. Specify the target Telegram channel username:
   ```python
   channel_username = '@your_channel_username'
   ```
3. Customize the keyword pattern to search for in messages:
   ```python
   pattern = re.compile(r'your_keyword', re.UNICODE)
   ```

## Usage

Run the script in your Python environment:

```bash
python telegram_reaction_analyzer.py
```

The script will:

1. Connect to the specified Telegram channel.
2. Fetch and analyze messages from 2024 containing the specified keyword.
3. Count and display reactions with their percentages.

## Example Output

```plaintext
Total messages checked containing the keyword in 2024: 15
Reaction Analysis:
👍 - 25 reactions (50.00%)
👎 - 10 reactions (20.00%)
❤️ - 15 reactions (30.00%)
```

## Notes

- Ensure your Telegram account has access to the target channel.
- The script stops processing messages once it reaches messages dated before 2024.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit pull requests for new features or bug fixes.

```

This README provides all necessary details for setting up, running, and understanding the functionality of the Telegram Reaction Analyzer script.
```
