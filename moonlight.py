# main.py | Main logic for monitoring Telegram channels and sending alerts

# --- Imports ---
from telethon import TelegramClient, events
import asyncio
from dotenv import load_dotenv
import os
import re

# --- Load environment variables from .env file ---
load_dotenv()

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
my_number = os.getenv("my_number")        # Your personal Telegram number (used for client login)
token_bot = os.getenv("token_bot")        # Bot token from @BotFather

# --- Configuration ---
TARGET_CHANNEL = '@your_target_channel'  # Replace with your personal or monitored channel
WATCHED_CHANNELS = ['@channel_to_monitor']  # List of channels to monitor

# --- Create clients (Telethon sessions) ---
client = TelegramClient('session_monitor', api_id, api_hash)
bot_client = TelegramClient('session_bot', api_id, api_hash)

# --- Event Handler for New Messages ---
def create_handler(bot_client):
    @client.on(events.NewMessage(chats=WATCHED_CHANNELS))
    async def handler(event):
        # Extract and lowercase the message content
        message = event.message.message.lower()

        # Define the keywords to look for example prices on channels for sales
        if re.search(r"\berror\b|\bprice error\b", message):
            # Try to get the channel name
            source_channel = event.chat.title if hasattr(event.chat, 'title') else "Unknown Channel"

            # Format the alert message
            full_message = (
                f"🔎 **Alert Detected**\n"
                f"📢 **Channel:** {source_channel}\n\n"
                f"{event.message.message}"
            )

            # Send the alert via the bot
            await bot_client.send_message(TARGET_CHANNEL, full_message)
            print(f"✅ Message forwarded to {TARGET_CHANNEL}")

    return handler

# --- Main async function to start both clients ---
async def main():
    await client.start(my_number)
    await bot_client.start(bot_token=token_bot)

    create_handler(bot_client)  # Attach the event handler

    print("🤖 Monitoring messages...")
    await client.run_until_disconnected()

# --- Run the event loop ---
asyncio.run(main())