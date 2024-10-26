# Twitter AI ChatBot

A powerful Twitter bot that leverages OpenAI's GPT-4 API to respond to user mentions and direct messages. This bot allows users to interact directly with an AI through commands, making it versatile for general-purpose queries.

## Features

- **/call**: Allows users to send a tweet or DM with `/call <message>` to receive a personalized greeting followed by the AI’s response.
- **/ask**: Users can tweet or DM with `/ask <question>` to directly ask the AI a question and receive a response.
- **Thinking Indicator**: Sends an immediate "Thinking..." message for DMs while processing the AI’s response.
- **Character Limit Handling**: Automatically splits responses into chunks to comply with Twitter's character limits for both tweets and DMs.
  
## Prerequisites

1. **Python 3.8+**: Ensure Python is installed and accessible from your command line.
2. **Twitter Developer Account**: Obtain API keys by creating a new Twitter app on [Twitter Developer](https://developer.twitter.com/).
3. **OpenAI API Key**: Sign up and obtain an API key from [OpenRouter](https://openrouter.ai/) to access GPT-4.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tryevertthhub/Bots
   cd Twitter

2. **Install Dependencies: Install the required packages using `pip`:**
   ```bash
    pip install tweepy aiohttp python-dotenv
   ```
3. **Configure Environment Variables: Create a `.env` file in the root directory of the project with the following content:**

   ```plaintext
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET=your_twitter_api_secret
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_SECRET=your_twitter_access_secret
    OPEN_ROUTER_API_KEY=your_openrouter_api_key
   ```
Replace the placeholders with your actual API keys and tokens.
## Running the Bot
- To start the bot, simply run the following command:
    ```bash
     python bot.py
    ```
Once the bot is running, you should see confirmation output in the terminal indicating that the bot is connected to Twitter and listening for mentions or direct messages.

## Code Overview
### Key Files
- bot.py: Main bot script containing event handling, message processing, and API interaction logic.
### Important Classes and Functions
- AIChatBotListener: Main listener class that uses Tweepy’s StreamListener to monitor mentions and DMs.
- fetch_ai_response: Asynchronous function that sends the user’s message to the OpenAI API and fetches the AI's response.
- on_status: Handles incoming mentions, parses the /call or /ask command, and replies with the AI response.
- on_direct_message: Handles DMs and responds with "Thinking..." while processing the AI response, then replies with the final answer.
- respond_with_ai: Splits and sends the AI response in chunks to avoid Twitter’s character limit.
### Example Code Snippet
Here’s an example of the /call command in the on_status function:

```python
def on_status(self, status):
    if status.user.screen_name != api.me().screen_name:
        command, *message_parts = status.text.split(maxsplit=1)
        message = message_parts[0] if message_parts else ""

        if "/call" in command:
            user_name = status.user.screen_name
            greeting = f"Hello, {user_name}, I am your assistant."
            api.update_status(f"@{status.user.screen_name} {greeting}", in_reply_to_status_id=status.id)
            asyncio.run(self.respond_with_ai(status, message))
```
### Environment Variables
```plaintext
TWITTER_API_KEY: Twitter API key.
TWITTER_API_SECRET: Twitter API secret.
TWITTER_ACCESS_TOKEN: Twitter access token.
TWITTER_ACCESS_SECRET: Twitter access secret.
OPEN_ROUTER_API_KEY: API key for accessing OpenAI’s GPT-4 model via OpenRouter.
```
