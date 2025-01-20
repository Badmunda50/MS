from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import subprocess
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import SUDOERS, db
from AnonXMusic.utils import AdminRightsCheck
from AnonXMusic.utils.database import is_active_chat, is_nonadmin_chat
from AnonXMusic.utils.decorators.language import languageCB
from config import BANNED_USERS, adminlist

checker = []


# Generate Buttons for Bass Control
def bass_markup(_, chat_id):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔉 +5", callback_data=f"BassUP {chat_id}|5"),
                InlineKeyboardButton("🔉 +10", callback_data=f"BassUP {chat_id}|10"),
            ],
            [
                InlineKeyboardButton(_["P_B_4"], callback_data=f"BassUP {chat_id}|0"),
            ],
            [
                InlineKeyboardButton("🔊 +15", callback_data=f"BassUP {chat_id}|15"),
                InlineKeyboardButton("🔊 +20", callback_data=f"BassUP {chat_id}|20"),
            ],
            [
                InlineKeyboardButton(_["CLOSE_BUTTON"], callback_data="close"),
            ],
        ]
    )


# FFmpeg Function to Apply Bass Boost
def apply_bass_boost(input_file, bass_level):
    try:
        output_file = f"{input_file}_bass_boosted.mp3"
        bass_filter = f"bass=g={bass_level}"
        subprocess.run(
            ["ffmpeg", "-i", input_file, "-af", bass_filter, output_file],
            check=True
        )
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e}")
        raise


# Bass Boost Command Handler
@app.on_message(filters.command(["cbass", "bass"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def bass_boost(cli, message: Message, _, chat_id):
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_27"])
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await message.reply_text(_["admin_27"])
    upl = bass_markup(_, chat_id)
    return await message.reply_text(
        text=_["admin_28"].format(app.mention),
        reply_markup=upl,
    )


# Callback for Bass Control Buttons
@app.on_callback_query(filters.regex("BassUP") & ~BANNED_USERS)
@languageCB
async def adjust_bass(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat, bass_level = callback_request.split("|")
    chat_id = int(chat)
    
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins or CallbackQuery.from_user.id not in admins:
                return await CallbackQuery.answer(_["admin_14"], show_alert=True)

    try:
        playing = db.get(chat_id)
        if not playing:
            return await CallbackQuery.answer(_["queue_2"], show_alert=True)

        file_path = playing[0]["file"]
        bass_level = int(bass_level)

        # Process Bass Boost
        new_file_path = apply_bass_boost(file_path, bass_level)

        # Restart Stream with New File
        await CallbackQuery.answer(_["admin_31"])
        mystic = await CallbackQuery.edit_message_text(
            text=_["admin_32"].format(CallbackQuery.from_user.mention),
        )
        await Anony.restart_stream(chat_id, new_file_path)

        # Update Playing Data
        playing[0]["bass"] = bass_level

        await mystic.edit_text(
            text=_["admin_34"].format(bass_level, CallbackQuery.from_user.mention),
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(_["CLOSE_BUTTON"], callback_data="close")]]),
        )
    except Exception as e:
        print(f"Error: {e}")
        return await CallbackQuery.answer(_["admin_33"], show_alert=True)
