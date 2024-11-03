# Twitter AI Chat Bot

**Twitter AI Chat Bot** is a Python bot designed for Twitter, powered by OpenAI’s GPT-4 API. This bot allows users to interact with AI, respond to mentions, and answer direct messages on Twitter with intelligent, AI-generated responses.

## Features

- Responds to mentions with AI-generated replies using OpenAI’s GPT-4.
- Answers direct messages when commands like `/call` or `/ask` are used.
- Designed to be interactive and responsive to user questions.

---

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Environment Variables** (stored in `.env`):
  - `TWITTER_API_KEY`
  - `TWITTER_API_SECRET`
  - `TWITTER_ACCESS_TOKEN`
  - `TWITTER_ACCESS_SECRET`
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
   TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET=your_twitter_api_secret
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_SECRET=your_twitter_access_secret
    OPEN_ROUTER_API_KEY=your_open_router_api_key
    ```
3. **Install the Package and Dependencies**
Navigate to the `twitter` directory and install the bot package:command:command:
    ```bash
    cd twitter
    pip install -e .
    ```

## Usage
Once installed, you can start the bot from the command line.

-  Run the Twitter Bot
    ```bash
    run_twitter_bot
    ```
## License