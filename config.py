import os

# Bot token comes from the environment, never from the repo.
# Windows: setx TELEGRAM_BOT_TOKEN "<new token from BotFather>"
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Set the TELEGRAM_BOT_TOKEN environment variable")

CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1001713035295")
