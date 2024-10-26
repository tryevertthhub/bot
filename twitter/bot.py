import os
import asyncio
import aiohttp
import tweepy
from dotenv import load_dotenv
from tweepy import Stream
from tweepy.streaming import StreamListener

# Load environment variables
load_dotenv()

# Fetch tokens and keys from environment variables
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
AI_BASE_URL = "https://openrouter.ai/api/v1"

# Setup Tweepy API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

class AIChatBotListener(StreamListener):
    """
    A Twitter bot listener that responds to mentions and direct messages using the AI API.
    """
    
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

    def on_status(self, status):
        """
        Event handler for when a tweet mentions the bot.
        """
        if status.user.screen_name != api.me().screen_name:
            command, *message_parts = status.text.split(maxsplit=1)
            message = message_parts[0] if message_parts else ""

            if "/call" in command:
                user_name = status.user.screen_name
                greeting = f"Hello, {user_name}, I am your assistant."
                api.update_status(f"@{status.user.screen_name} {greeting}", in_reply_to_status_id=status.id)
                asyncio.run(self.respond_with_ai(status, message))

            elif "/ask" in command:
                asyncio.run(self.respond_with_ai(status, message))

    def on_direct_message(self, status):
        """
        Event handler for direct messages to the bot.
        """
        dm_text = status.direct_message['text']
        sender_id = status.direct_message['sender_id']
        command, *message_parts = dm_text.split(maxsplit=1)
        message = message_parts[0] if message_parts else ""

        if command in ["/call", "/ask"]:
            api.send_direct_message(sender_id, "Thinking...")
            asyncio.run(self.respond_with_ai_dm(sender_id, message))

    async def respond_with_ai(self, status, message: str):
        """
        Sends the AI response as a tweet reply.

        Args:
            status: The tweet status to reply to.
            message (str): The user’s question or message for the AI.
        """
        ai_response = await self.fetch_ai_response(message)

        # Split response if too long and tweet it
        response_chunks = [ai_response[i:i + 240] for i in range(0, len(ai_response), 240)]
        for chunk in response_chunks:
            api.update_status(f"@{status.user.screen_name} {chunk}", in_reply_to_status_id=status.id)

    async def respond_with_ai_dm(self, sender_id, message: str):
        """
        Sends the AI response as a direct message.

        Args:
            sender_id: The Twitter user ID to send the DM to.
            message (str): The user’s question or message for the AI.
        """
        ai_response = await self.fetch_ai_response(message)

        # Split response if too long and DM it
        response_chunks = [ai_response[i:i + 240] for i in range(0, len(ai_response), 240)]
        for chunk in response_chunks:
            api.send_direct_message(sender_id, chunk)

# Start the Twitter Stream
if __name__ == "__main__":
    listener = AIChatBotListener()
    stream = Stream(auth, listener)
    stream.filter(track=[f"@{api.me().screen_name}"], is_async=True)
