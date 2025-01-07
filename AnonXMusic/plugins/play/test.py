import os
from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.decorators.play import PlayWrapper
from AnonXMusic.utils.logger import play_logs
from config import BANNED_USERS

@app.on_message(
    filters.command(["hello"]) 
    & filters.group
    & ~BANNED_USERS
)
@PlayWrapper
async def hello_command(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
    fplay,
):
    mystic = await message.reply_text(
        "Hello! Preparing to join the voice chat and play the requested file."
    )
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    # Path to the file to be played
    file_path = 'AnonXMusic/assets/shiv.mp3'

    # Check if the file exists
    if not os.path.exists(file_path):
        return await mystic.edit_text("Error: File not found. Please check the file path.")

    # Join the voice chat and play the file
    try:
        await Anony.stream_call(file_path)
        await mystic.edit_text("Successfully joined the voice chat and playing the file.")
        await play_logs(message, streamtype="Local file")
    except NoActiveGroupCall:
        await mystic.edit_text("No active group call. Please start a voice chat first.")
        return await app.send_message(
            chat_id=config.LOGGER_ID,
            text="Failed to join the voice chat due to no active group call."
        )
    except Exception as e:
        await mystic.edit_text(f"Error: {type(e).__name__} - {str(e)}")
