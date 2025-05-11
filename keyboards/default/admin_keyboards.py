from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Xabar Yuborish 🗒 ')
        ],
        [
            KeyboardButton(text='Kanal ➕'),
            KeyboardButton(text='Kanal ➖')
        ],
        [
            KeyboardButton(text="Kanallar 📈"),
            KeyboardButton(text="Statistika 📊")
        ],
        [
            KeyboardButton(text="Rasmni almashtirish 🖼 "),
            KeyboardButton(text="Sovg'alar ro'yxatini kiritish📄"),
        ],
        [
            KeyboardButton(text="Taklif miqdorini kiritish 🎁"),
            KeyboardButton(text="O'yin haqida matn 🎮")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

admin_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Xabar Yuborish 🗒 ')
        ],
        [
            KeyboardButton(text='Kanal ➕'),
            KeyboardButton(text='Kanal ➖')
        ],
        [
            KeyboardButton(text="Kanallar 📈"),
            KeyboardButton(text="Statistika 📊")
        ],
        [
            KeyboardButton(text="🏘 Bosh menu")

        ]
    ],
    resize_keyboard=True
)
