from pyrogram.types import InlineKeyboardButton
from pyrogram import filters, Client

import config

def start_panel(client):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{client.get_me().username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons

def private_panel(client):
    user_id = client.get_me().id
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{client.get_me().username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=user_id),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
       [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
    ]
    return buttons
