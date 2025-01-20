from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import SUDOERS, db
from AnonXMusic.utils import AdminRightsCheck
from AnonXMusic.utils.database import is_active_chat, is_nonadmin_chat
from AnonXMusic.utils.decorators.language import languageCB
from AnonXMusic.utils.inline import close_markup, bass_markup
from config import BANNED_USERS, adminlist

checker = []

@app.on_message(
    filters.command(["cbass", "bass"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def bass_boost(cli, message: Message, _, chat_id):
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_41"])
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await message.reply_text(_["admin_41"])
    upl = bass_markup(_, chat_id)
    return await message.reply_text(
        text=_["admin_42"].format(app.mention),
        reply_markup=upl,
    )

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
            if not admins:
                return await CallbackQuery.answer(_["admin_13"], show_alert=True)
            else:
                if CallbackQuery.from_user.id not in admins:
                    return await CallbackQuery.answer(_["admin_14"], show_alert=True)
    playing = db.get(chat_id)
    if not playing:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await CallbackQuery.answer(_["admin_41"], show_alert=True)
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await CallbackQuery.answer(_["admin_41"], show_alert=True)
    check_bass = (playing[0]).get("bass")
    if check_bass:
        if str(check_bass) == str(bass_level):
            if str(bass_level) == str("0"):
                return await CallbackQuery.answer(
                    _["admin_43"],
                    show_alert=True,
                )
    else:
        if str(bass_level) == str("0"):
            return await CallbackQuery.answer(
                _["admin_43"],
                show_alert=True,
            )
    if chat_id in checker:
        return await CallbackQuery.answer(
            _["admin_44"],
            show_alert=True,
        )
    else:
        checker.append(chat_id)
    try:
        await CallbackQuery.answer(
            _["admin_45"],
        )
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(
        text=_["admin_46"].format(CallbackQuery.from_user.mention),
    )
    try:
        await Anony.bass_boost_stream(
            chat_id,
            file_path,
            bass_level,
            playing,
        )
    except Exception as e:
        if chat_id in checker:
            checker.remove(chat_id)
        return await mystic.edit_text(f"{_['admin_47']} Error: {str(e)}", reply_markup=close_markup(_))
    if chat_id in checker:
        checker.remove(chat_id)
    await mystic.edit_text(
        text=_["admin_48"].format(bass_level, CallbackQuery.from_user.mention),
        reply_markup=close_markup(_),
        )
