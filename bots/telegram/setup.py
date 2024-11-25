from setuptools import setup, find_packages

setup(
    name="bot",
    version="0.1.0",
    description="A suite of AI-powered bots Telegram",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    author="Khanh Tran",
    author_email="tryevertth@gmail.com",
    url="https://github.com/tryevertthhub/bot",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot",
        "aiohttp",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "run_telegram_bot=bot:run_telegram_bot", 
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
