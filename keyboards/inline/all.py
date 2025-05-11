from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import db

invite_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Одам таклиф қилиб балларни тўплаш", callback_data="invite")
        ]

    ]
)
