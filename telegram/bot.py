import os
import json
import aiohttp
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Fetch tokens and keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
AI_BASE_URL = "https://openrouter.ai/api/v1"

class TelegramAIChatBot:
    """
    A Telegram bot that allows users to interact with an AI API.
    Provides both personalized greetings and AI responses.
    """
    
    def __init__(self):
        """Initializes the bot with commands and sets up handlers."""
        self.application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        
        # Register bot commands
        self.setup_commands()

    def setup_commands(self):
        """Registers all bot commands and message handlers."""
        # /start command
        self.application.add_handler(CommandHandler("start", self.start_command))
        
        # /call command
        self.application.add_handler(CommandHandler("call", self.call_command))
        
        # /ask command
        self.application.add_handler(CommandHandler("ask", self.ask_command))

        # Catch-all handler for regular messages
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Responds to the /start command with a welcome message.

        Args:
            update (Update): The Telegram update object.
            context (ContextTypes.DEFAULT_TYPE): The context for the command.
        """
        await update.message.reply_text("Welcome! Use /call <message> or /ask <question> to interact with the AI.")

    async def call_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles the /call command, sends a personalized greeting, and fetches an AI response.

        Args:
            update (Update): The Telegram update object.
            context (ContextTypes.DEFAULT_TYPE): The context for the command.
        """
        user_name = update.effective_user.first_name or "User"
        greeting = f"Hello, {user_name}, I am your assistant."
        await update.message.reply_text(greeting)
        
        # Get the message text after /call command
        message_text = " ".join(context.args)
        if message_text:
            await self.show_thinking_message(update, message_text)
        else:
            await update.message.reply_text("Please provide a message after /call.")

    async def ask_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles the /ask command, fetches an AI response, and sends it to the user.

        Args:
            update (Update): The Telegram update object.
            context (ContextTypes.DEFAULT_TYPE): The context for the command.
        """
        question_text = " ".join(context.args)
        if question_text:
            await self.show_thinking_message(update, question_text)
        else:
            await update.message.reply_text("Please provide a question after /ask.")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles non-command messages and provides a response from the AI.

        Args:
            update (Update): The Telegram update object.
            context (ContextTypes.DEFAULT_TYPE): The context for the command.
        """
        message_text = update.message.text
        await self.show_thinking_message(update, message_text)

    async def fetch_ai_response(self, message: str) -> str:
        """
        Fetches an AI-generated response based on the given user message.

        Args:
            message (str): The user's input message to send to the AI.

        Returns:
            str: The response from the AI, or an error message if the request fails.
        """
        headers = {
            "Authorization": f"Bearer {OPEN_ROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-4",
            "prompt": message,
            "max_tokens": 1000,
            "temperature": 1.0
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(AI_BASE_URL + "/completions", headers=headers, json=data) as response:
                if response.status == 200:
                    response_data = await response.json()
                    return response_data["choices"][0]["text"].strip()
                else:
                    error_message = await response.text()
                    print(f"HTTP error {response.status}: {error_message}")
                    return "Failed to get a response due to an HTTP error."

    async def show_thinking_message(self, update: Update, message: str):
        """
        Sends a "Thinking..." message, fetches an AI response, and updates with the final response.

        Args:
            update (Update): The Telegram update object.
            message (str): The user's message to be processed by the AI.
        """
        thinking_message = await update.message.reply_text("Thinking...")
        ai_response = await self.fetch_ai_response(message)
        
        # If response is too long, send it in chunks
        await self.display_response_with_chunks(update, ai_response, thinking_message)

    async def display_response_with_chunks(self, update: Update, response: str, message):
        """
        Edits or splits the AI response into manageable chunks if the response length exceeds Telegram's message limit.

        Args:
            update (Update): The Telegram update object.
            response (str): The full AI response to be displayed.
            message: The initial "Thinking..." message to edit or replace.
        """
        if len(response) > 4096:
            response_chunks = [response[i:i + 4096] for i in range(0, len(response), 4096)]
            await message.edit_text(response_chunks[0])
            for chunk in response_chunks[1:]:
                await update.message.reply_text(chunk)
        else:
            await message.edit_text(response)


# Instantiate and run the bot
if __name__ == "__main__":
    bot = TelegramAIChatBot()
    bot.application.run_polling()
