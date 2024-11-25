# Telegram AI Chat Bot

**Telegram AI Chat Bot** is a Python bot designed for Telegram, powered by OpenAI’s GPT-4 API. This bot allows users to interact with AI, ask questions, and receive intelligent responses in Telegram chats.

## Features

- Responds to commands like `/call` and `/ask`.
- Provides AI-generated answers using OpenAI’s GPT-4 for user queries.
- Friendly and interactive user experience within the Telegram app.

---

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Environment Variables** (stored in `.env`):
  - `TELEGRAM_BOT_TOKEN`
  - `OPEN_ROUTER_API_KEY`

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tryevertthhub/bot.git
   cd bot
   ```
2. **Set Up Environment Variables**
Create a `.env` file in the root directory with your credentials:

    ```plaintext
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OPEN_ROUTER_API_KEY=your_open_router_api_key

    ```
3. **Install the Package and Dependencies**
Navigate to the `telegram` directory and install the bot package:command:
    ```bash
    cd telegram
    pip install -e .
    ```

## Usage
Once installed, you can start the bot from the command line.

-  Run the Telegram Bot
    ```bash
    run_telegram_bot
    ```
## License