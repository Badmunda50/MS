import random
import string

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.decorators.language import languageCB
from AnonXMusic.utils.decorators.play import PlayWrapper
from AnonXMusic.utils.logger import play_logs
from AnonXMusic.utils.stream.stream import stream
from config import BANNED_USERS

@app.on_message(
    filters.command(["hello"]) 
    & filters.group
    & ~BANNED_USERS
)
@PlayWrapper
async def hello_commnd(
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
        "Hello! Joining voice chat to play the requested file content."
    )
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    # Path to the file to be played
    file_path = 'AnonXMusic/path/shiv.mp3'
    
    # Join the voice chat and play the content
    try:
        await Anony.stream_call(file_path)
    except NoActiveGroupCall:
        await mystic.edit_text("No active group call.")
        return await app.send_message(
            chat_id=config.LOGGER_ID,
            text="Failed to join voice chat."
        )
    except Exception as e:
        return await mystic.edit_text(f"Error: {type(e).__name__}")
    
    await mystic.edit_text("Playing the path file content in the voice chat.")
    await play_logs(message, streamtype="Path file content")
