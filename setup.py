from setuptools import setup

setup(
    name="TelegramBotAPI",
    version="0.1",
    description="Telegram Bot API",
    packages=['TelegramBotAPI'],
    install_requires=[
        'pyOpenSSL',
        'service_identity',
    ],
)
