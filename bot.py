from pyrogram import Client, filters
import random

api_id = 25893261
api_hash = "17034419f230472d0d1767da2f9cdd62"
bot_token = "7250673685:AAF-Q-tmTAteeV2WG2fo8V9MEgSIiO8"

emojis = ["😂", "😍", "👍", "🔥", "😎", "🥰", "🤔", "😱", "😭", "🤗"]

app = Client("auto-react-bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.text & ~filters.edited)
async def auto_react(client, message):
    try:
        emoji = random.choice(emojis)
        await message.react(emoji)
    except Exception as e:
        print(f"Error reacting: {e}")

app.run()
