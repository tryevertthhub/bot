# Telegram AI ChatBot

A powerful Telegram bot that allows users to interact with an AI API (GPT-4) to receive responses to their questions and messages. The bot supports multiple command interactions, providing a user-friendly experience with personalized greetings and handling both direct and interactive queries.

## Features

- **/start**: Sends a welcome message to guide users on available commands.
- **/call**: Allows users to initiate an AI conversation with a personalized greeting.
- **/ask**: Enables users to ask a question directly to the AI without the personalized greeting.
- **Intelligent Response Handling**: Automatically splits long responses to meet Telegram's message length limit.
- **Thinking Indicator**: Displays a "Thinking..." message to inform users that the bot is processing their request.

## Prerequisites

1. **Python 3.8+**: Ensure Python is installed and accessible from your command line.
2. **Telegram Bot Token**: Create a new Telegram bot with [BotFather](https://core.telegram.org/bots#botfather) to obtain the `TELEGRAM_BOT_TOKEN`.
3. **OpenAI API Key**: Obtain an API key from [OpenRouter](https://openrouter.ai/) to access the AI API.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tryevertthhub/Communeai-bot.git
   cd Telegram
2. **Install Dependencies: Install the required packages using `pip`:**
   ```bash
   pip install python-telegram-bot aiohttp python-dotenv
   ```
3. **Configure Environment Variables: Create a `.env` file in the root directory of the project with the following content:**
   ```bash
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OPEN_ROUTER_API_KEY=your_openrouter_api_key
   ```
Replace `your_telegram_bot_token` and `your_openrouter_api_key` with your actual API tokens.

## Running the Bot
 - To start the bot, simply run the following command:
   ```bash
    python bot.py
   ```
Once the bot is running, you should see confirmation output in the terminal indicating that the bot has connected to Telegram and is ready to receive messages.

## Usage
### Commands
1. `/start`: Sends a welcome message with instructions on how to use the bot.

- Example: `/start`
2. `/call` <message>: Sends a personalized greeting to the user and forwards the provided <message> to the AI API, which responds with a generated answer.

- Example: `/call` Hello, what can you do?

3. `/ask` <question>: Sends the <question> directly to the AI without a personalized greeting. Ideal for straightforward Q&A with the AI.

- Example: `/ask` What is the capital of France?

## Code Overview
### Key Files
- `bot.py`: Main bot script containing command setup, message handling, and AI response fetching logic.
### Important Classes and Functions
- TelegramAIChatBot: Primary class that initializes the bot, registers commands, and contains all core functionalities.
- setup_commands: Registers the `/start`, `/call`, and `/ask` commands, along with a message handler for non-command text.
- call_command: Handles the `/call` command with a personalized greeting before forwarding the user’s message to the AI.
- ask_command: Processes the `/ask` command, directly sending the user’s question to the AI.
- fetch_ai_response: Makes an asynchronous request to the AI API, retrieving a generated response.
- show_thinking_message: Displays a "Thinking..." message to let users know the bot is processing their input.
- display_response_with_chunks: Splits the AI's response into smaller chunks if it exceeds Telegram's message length limit, ensuring no content is cut off.

### Example Code Snippet
Here is an example of how the `/call` command is structured:

```python
async def call_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name or "User"
    greeting = f"Hello, {user_name}, I am your assistant."
    await update.message.reply_text(greeting)
    
    # Get the message text after /call command
    message_text = " ".join(context.args)
    if message_text:
        await self.show_thinking_message(update, message_text)
    else:
        await update.message.reply_text("Please provide a message after /call.")

```
### Environment Variables
`TELEGRAM_BOT_TOKEN`: The Telegram bot token provided by BotFather.
`OPEN_ROUTER_API_KEY`: API key for accessing OpenAI's GPT-4 model via OpenRouter.
