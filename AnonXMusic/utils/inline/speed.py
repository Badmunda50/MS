from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def speed_markup(_, chat_id):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🕒 0.5x",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                ),
                InlineKeyboardButton(
                    text="🕓 0.75x",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["P_B_4"],
                    callback_data=f"SpeedUP {chat_id}|1.0",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🕤 1.5x",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                ),
                InlineKeyboardButton(
                    text="🕛 2.0x",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def bass_markup(_, chat_id):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🔉 +5",
                    callback_data=f"BassUP {chat_id}|5",
                ),
                InlineKeyboardButton(
                    text="🔉 +10",
                    callback_data=f"BassUP {chat_id}|10",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["P_B_4"],  # Default Bass Level (e.g., 0)
                    callback_data=f"BassUP {chat_id}|0",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔊 +15",
                    callback_data=f"BassUP {chat_id}|15",
                ),
                InlineKeyboardButton(
                    text="🔊 +20",
                    callback_data=f"BassUP {chat_id}|20",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl
