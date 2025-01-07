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
    filters.command(["test"])  # Command is 'test'
    & filters.group
    & ~BANNED_USERS
)
@PlayWrapper
async def test_command(
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
        "Joining the voice chat to play the requested audio file."
    )

    # Path to the audio file (MP3)
    file_path = 'AnonXMusic/assets/shiv.mp3'

    # Check if the file exists
    if not os.path.exists(file_path):
        return await mystic.edit_text("Error: Audio file not found. Please check the file path.")

    # Join the voice chat and play the audio file
    try:
        # Explicitly treat the file as an audio source, no video expected
        await Anony.stream_call(file_path, is_audio=True)  # Pass is_audio=True to ensure it's audio
        await mystic.edit_text("Playing the audio file in the voice chat.")
        await play_logs(message, streamtype="Audio file")
    except NoActiveGroupCall:
        await mystic.edit_text("No active group call. Please start a voice chat first.")
        return await app.send_message(
            chat_id=config.LOGGER_ID,
            text="Failed to join the voice chat due to no active group call."
        )
    except Exception as e:
        await mystic.edit_text(f"Error: {type(e).__name__} - {str(e)}")
