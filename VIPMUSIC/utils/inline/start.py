from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from VIPMUSIC import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🫠𝗕𝗮𝗯𝘆 𝗠𝘂𝗷𝗵𝗲 𝗟𝗲 𝗖𝗵𝗮𝗹𝗼🥺",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="🫣 𝗛𝗲𝗹𝗽 🫣", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="⚙️𝗦𝗲𝘁⚙️", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="❤️𝗚𝗿𝗼𝘂𝗽❤️", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🐽 𝗕𝗮𝗯𝘆 𝗠𝘂𝗷𝗵𝗲 𝗟𝗲 𝗖𝗵𝗮𝗹𝗼 🥺",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="💟𝗚𝗿𝗼𝘂𝗽💟", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="💥𝗠𝗼𝗿𝗲💥", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="💞𝗧𝗮𝗽 𝗧𝗼 𝗞𝗻𝗼𝘄 𝗠𝗼𝗿𝗲 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀💞", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="😚𝗠𝘂𝗷𝗵𝗲 𝗗𝗮𝗯𝗮𝗼 𝗡𝗮😉", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
