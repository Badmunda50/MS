from pyrogram.types import InlineKeyboardButton
from pymongo import MongoClient  # Import MongoClient to access the database

import config
from AnonXMusic import app

# Define the clonebotdb (imported from clone.py)
client = MongoClient('mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/')
db = client['anonmusic']
clonebotdb = db['clonebotdb']

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_, user_id):
    # Fetch the cloned bot owner details from the database
    cloned_bot = clonebotdb.find_one({"user_id": user_id})
    owner_name = cloned_bot["name"] if cloned_bot else "Owner"

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=user_id),
            InlineKeyboardButton(text=owner_name, url=config.SUPPORT_CHAT),  # Display the owner's name
        ],
       [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
    ]
    return buttons
