from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID, add_premium_user
from bot import bot

# Command to add/upgrade a user to premium
@bot.on_message(filters.command("addpro") & filters.private)
async def add_premium_user_command(client, message: Message):
    # Check if the user is the owner
    if message.from_user.id == int(OWNER_ID):
        # Parse the command arguments
        command_parts = message.text.split()
        if len(command_parts) == 3:
            _, user_id, days = command_parts
            user_id = int(user_id)
            days = int(days)
            # Add the user to premium
            add_premium_user(user_id, days)
            # Notify the user
            await client.send_message(chat_id=user_id, text=f"Your premium plan has been added for {days} days.")
        else:
            # Invalid command format
            await message.reply_text("Invalid command format. Use /addpro {user_id} {days}")
    else:
        # User is not authorized to use this command
        await message.reply_text("You are not authorized to use this command.")
