# Discord AI ChatBot

This project is a Discord bot that interacts with users through GPT-4, providing AI-powered responses to user queries. The bot can be used in both interactive and direct modes, allowing users to either initiate a prompt via a button modal or directly call the AI with a command. 

## Features

- **/ask Command**: Allows users to initiate a query through an interactive button and modal.
- **/call Command**: Enables users to directly query the AI and receive a personalized response.
- **Custom Greeting**: When a user invokes the `/call` command, the bot greets them by their display name, making the interaction more personalized.
- **Handles Long Responses**: The bot automatically splits lengthy AI responses into manageable chunks to comply with Discord’s message limit.

## Prerequisites

1. **Python 3.8+**: Ensure Python is installed and accessible from the command line.
2. **Discord Bot**: Create a Discord bot and obtain its token. See the [Discord Developer Portal](https://discord.com/developers/applications).
3. **OpenAI API Key**: Obtain an API key from [OpenAI's OpenRouter](https://openrouter.ai/).

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/tryevertthhub/Communeai-bot.git
   cd discord-ai-chatbot
2. pip install discord.py aiohttp
   ```bash
     pip install discord.py aiohttp
   ```
3.  Create an `.env` file in the root directory and add the following configuration:
    ```bash
     DISCORD_BOT_TOKEN=your_discord_bot_token
     OPEN_ROUTER_API_KEY=your_openai_api_key
     CLIENT_ID=your_discord_bot_id
    ```
4. Replace `YOUR_DISCORD_BOT_TOKEN` and `YOUR_OPENAI_API_KEY` with your actual tokens in the `.env` file.

## Running the Bot
Run the following command to start the bot:

   ```bash
    python bot.py
   ``` 
The bot will log in and sync commands. You should see a message indicating that the bot is connected and ready.

## Usage
 1. `/ask` Command: Type `/ask` in any channel where the bot has access. This will display a button labeled “Ask the AI.”

- Click the button, enter your query in the modal that appears, and submit it.
- The bot will then respond to your query directly.

 2. `/call` Command: Type `/call` <your message> to directly interact with the AI.

- The bot will respond with a personalized greeting like, "Hello, <user name>, I am your assistant," followed by the AI’s response to your message.

## Code Overview
### Key Files and Functions
- `discord-bot.py`: The main script for the bot containing all commands and functionalities.
### Important Functions:
- `setup_commands`: Registers bot commands (/ask and /call) with detailed functionality.
- `ask_command`: Provides a button for users to initiate an AI query through a modal.
- `call_command`: Handles direct AI queries, responding with a greeting and the AI’s response.
- `fetch_ai_response`: Sends the user’s message to the OpenAI API and returns the AI’s response.
- `show_thinking_message`: Displays a “Thinking...” message while awaiting the AI response and updates with the final message.
- `display_response_with_chunks`: Automatically splits and sends long responses to avoid exceeding Discord’s message length limit.
- `handle_modal_interaction`: Presents a modal when users click the "Ask the AI" button and processes the response upon submission. 

## Example Code
Below is a snippet of the main command registration and the /call command with a personalized greeting:

 ```python
 def setup_commands(self):
    @self.tree.command(name="ask")
    async def ask(interaction: discord.Interaction):
        await self.ask_command(interaction)
    
    @self.tree.command(name="call")
    async def call(interaction: discord.Interaction, message: str):
        await self.call_command(interaction, message)

async def call_command(self, interaction: discord.Interaction, message: str):
    await interaction.response.defer(ephemeral=True)
    greeting = f"Hello, {interaction.user.display_name}, I am your assistant."
    await interaction.followup.send(greeting, ephemeral=True)
    await self.show_thinking_message(interaction, message)
```


