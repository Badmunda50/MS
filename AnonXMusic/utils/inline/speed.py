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
                    text="🔉 10×",
                    callback_data=f"BassUP {chat_id}|10",
                ),
                InlineKeyboardButton(
                    text="🔉 20×",
                    callback_data=f"BassUP {chat_id}|20",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["P_B_4"] + " 00",  # Default Bass Level with 00 added
                    callback_data=f"BassUP {chat_id}|1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔊 30×",
                    callback_data=f"BassUP {chat_id}|30",
                ),
                InlineKeyboardButton(
                    text="🔊 40×",
                    callback_data=f"BassUP {chat_id}|40",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔊 50×",
                    callback_data=f"BassUP {chat_id}|50",
                ),
                InlineKeyboardButton(
                    text="🔊 60×",
                    callback_data=f"BassUP {chat_id}|60",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔊 70×",
                    callback_data=f"BassUP {chat_id}|70",
                ),
                InlineKeyboardButton(
                    text="🔊 80×",
                    callback_data=f"BassUP {chat_id}|80",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔊 90×",
                    callback_data=f"BassUP {chat_id}|90",
                ),
                InlineKeyboardButton(
                    text="🔊 100×",
                    callback_data=f"BassUP {chat_id}|100",
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
