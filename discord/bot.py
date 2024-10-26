import discord
from discord.ext import commands
import requests
import json
import aiohttp
import os
from dotenv import load_dotenv


load_dotenv()

# Fetch tokens and keys from environment variables
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
AI_BASE_URL = "https://openrouter.ai/api/v1"

class AIChatBot(commands.Bot):
    """
    A Discord bot that allows users to interact with an AI API via commands.
    Provides both interactive and direct command-based querying functionalities.
    """
    
    def __init__(self):
        """
        Initializes the bot with required intents, command prefix, and event listeners.
        Sets up bot commands and defines intents for message content.
        """
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="/", intents=intents)
        
        # Initialize commands and interactions
        self.setup_commands()

    async def on_ready(self):
        """Event that runs when the bot is ready and connected to Discord."""
        print(f"Logged in as {self.user}!")
        await self.tree.sync()

    def setup_commands(self):
        """Registers all bot commands in the command tree."""
        
        # Register the /ask command
        @self.tree.command(name="ask")
        async def ask(interaction: discord.Interaction):
            """Displays a button for users to initiate an AI query through a modal."""
            await self.ask_command(interaction)
        
        # Register the /call command with personalized greeting
        @self.tree.command(name="call")
        async def call(interaction: discord.Interaction, message: str):
            """Handles a direct AI call with a personalized greeting."""
            await self.call_command(interaction, message)

    async def ask_command(self, interaction: discord.Interaction):
        """
        Displays a button for the user to initiate an AI query via a modal.

        Args:
            interaction (discord.Interaction): The Discord interaction object.
        """
        button = discord.ui.Button(label="Ask the AI", style=discord.ButtonStyle.primary, custom_id="ask_ai_button")
        view = discord.ui.View()
        view.add_item(button)
        await interaction.response.send_message("Click the button to ask the AI:", view=view, ephemeral=True)

    async def call_command(self, interaction: discord.Interaction, message: str):
        """
        Directly sends the user's message to the AI with a personalized greeting, and displays the response.

        Args:
            interaction (discord.Interaction): The Discord interaction object.
            message (str): The message to be processed by the AI.
        """
        await interaction.response.defer(ephemeral=True)
        greeting = f"Hello, {interaction.user.display_name}, I am your assistant."
        await interaction.followup.send(greeting, ephemeral=True)
        await self.show_thinking_message(interaction, message)

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

    async def show_thinking_message(self, interaction: discord.Interaction, message: str):
        """
        Displays a "Thinking..." message, fetches an AI response, and updates the message with the final response.

        Args:
            interaction (discord.Interaction): The Discord interaction object.
            message (str): The user's message to be processed by the AI.
        """
        thinking_message = await interaction.followup.send("Thinking...", ephemeral=True)
        ai_response = await self.fetch_ai_response(message)
        await self.display_response_with_chunks(interaction, ai_response, thinking_message)

    async def display_response_with_chunks(self, interaction: discord.Interaction, response: str, message: discord.WebhookMessage):
        """
        Edits or splits the AI response into manageable chunks if the response length exceeds Discord's message limit.

        Args:
            interaction (discord.Interaction): The Discord interaction object.
            response (str): The full AI response to be displayed.
            message (discord.WebhookMessage): The initial "Thinking..." message to edit.
        """
        if len(response) > 2000:
            response_chunks = [response[i:i + 2000] for i in range(0, len(response), 2000)]
            await message.edit(content=response_chunks[0])
            for chunk in response_chunks[1:]:
                await interaction.followup.send(chunk, ephemeral=True)
        else:
            await message.edit(content=response)

    async def handle_modal_interaction(self, interaction: discord.Interaction):
        """
        Presents a modal to the user to collect input and processes the response upon submission.

        Args:
            interaction (discord.Interaction): The Discord interaction object.
        """
        class AskModal(discord.ui.Modal, title="Ask the AI"):
            question = discord.ui.TextInput(label="What would you like to ask the AI?", style=discord.TextStyle.paragraph)

            async def on_submit(self, interaction: discord.Interaction):
                """
                Handles submission of the modal, defers the interaction, and processes the user message.

                Args:
                    interaction (discord.Interaction): The Discord interaction object upon modal submission.
                """
                await interaction.response.defer(ephemeral=True)
                user_message = self.question.value
                await bot.show_thinking_message(interaction, user_message)

        await interaction.response.send_modal(AskModal())

    async def on_interaction(self, interaction: discord.Interaction):
        """
        Handles interactions for button clicks and modal submissions.

        Args:
            interaction (discord.Interaction): The Discord interaction object.
        """
        custom_id = interaction.data.get("custom_id") if interaction.data else None
        if custom_id == "ask_ai_button":
            await self.handle_modal_interaction(interaction)


# Instantiate and run the bot
bot = AIChatBot()
bot.run(DISCORD_BOT_TOKEN)
