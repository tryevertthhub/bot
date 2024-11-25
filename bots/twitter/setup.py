from setuptools import setup, find_packages

setup(
    name="bot",
    version="0.1.0",
    description="A suite of AI-powered bots Twitter",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    author="Khanh Tran",
    author_email="tryevertth@gmail.com",
    url="https://github.com/tryevertthhub/bot",
    packages=find_packages(),
    install_requires=[
        "tweepy",
        "aiohttp",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "run_twitter_bot=bot:run_twitter_bot",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
