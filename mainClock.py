import asyncio
import sys
from datetime import datetime
import pytz
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# Windows fix
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

api_id = 1566396
api_hash = "e011d9796aea5ea661ac0286a35d89ed"

client = TelegramClient("session_name", api_id, api_hash)

async def update_loop():
    await client.start()
    tz = pytz.timezone("Asia/Tashkent")

    while True:
        now = datetime.now(tz).strftime("%H:%M")
        bio = f"🕒 Time now: {now}"

        try:
            await client(UpdateProfileRequest(about=bio))
            print("Updated:", bio)
        except Exception as e:
            print("Error:", e)

        await asyncio.sleep(60)

async def main():
    while True:
        try:
            await update_loop()
        except Exception as e:
            print("Restarting:", e)
            await asyncio.sleep(5)

asyncio.run(main())