# Discord AI Chat Bot

**Discord AI Chat Bot** is a Python bot designed for Discord, powered by OpenAI’s GPT-4 API. This bot allows users to interact with the AI, answer questions, and respond to commands in Discord servers.

## Features

- Responds to commands like `/call` and `/ask`.
- Provides responses from OpenAI’s GPT-4 for user queries.
- Interactive modals and buttons for enhanced user experience.

---

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Environment Variables** (stored in `.env`):
  - `DISCORD_BOT_TOKEN`
  - `OPEN_ROUTER_API_KEY`

### Installation

1. **Clone the Repository**

   ```bash
   git clone    git clone https://github.com/tryevertthhub/bot.git

   cd bot

   ```
2. **Set Up Environment Variables**
Create a `.env` file in the root directory with your credentials:

    ```plaintext
    DISCORD_BOT_TOKEN=your_discord_token
    OPEN_ROUTER_API_KEY=your_open_router_api_key
    ```
3. **Install the Package and Dependencies**
Each bot has its own `setup.py`. Install the Discord bot with the following command:
    ```bash
    cd discord
    pip install -e .
    ```

## Usage
Once installed, you can start the bot from the command line.

-  Run the Discord Bot
    ```bash
    run_discord_bot
    ```
## License