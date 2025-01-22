from pyrogram.types import InlineKeyboardButton
from AnonXMusic import app
import requests

def get_cloner_username():
    # Fetch the username of the person who cloned the repository
    response = requests.get("https://api.github.com/repos/Badmunda50/MS")
    if response.status_code == 200:
        repo_data = response.json()
        owner_username = repo_data["owner"]["login"]
        return owner_username
    return "Unknown"

def start_panel(_):
    cloner_username = get_cloner_username()
    buttons = [
        [
            InlineKeyboardButton(
                text=_[ "S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_[ "S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"], url=f"https://t.me/{cloner_username}"
            ),
        ],
    ]
    return buttons
    
    
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{cloner_username}"),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
       [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
    ]
    return buttons
