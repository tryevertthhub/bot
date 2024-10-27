# setup.py

from setuptools import setup, find_packages

setup(
    name="bot",
    version="0.1.0",
    description="A suite of AI-powered bots for Discord, Telegram, and Twitter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Khanh Tran",
    author_email="tryevertth@gmail.com",
    url="https://github.com/tryevertthhub/bot",
    packages=find_packages(),
    install_requires=[
        "discord.py",
        "python-telegram-bot",
        "tweepy",
        "aiohttp",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "run_discord_bot=bot.discord:run_discord_bot",
            "run_telegram_bot=bot.telegram:run_telegram_bot",
            "run_twitter_bot=bot.twitter:run_twitter_bot"
        ]
    },
)
