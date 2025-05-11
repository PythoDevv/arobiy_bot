from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

picture = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1-qism'),
            KeyboardButton(text='2-qism'),
        ],
        [
            KeyboardButton(text='3-qism'),
            KeyboardButton(text='4-qism')
        ],
        [
            KeyboardButton(text='5-qism'),
            KeyboardButton(text='6-qism'),
        ],
        [
            KeyboardButton(text='7-qism'),
            KeyboardButton(text='8-qism')
        ],
        [
            KeyboardButton(text='9-qism'),
            KeyboardButton(text='10-qism'),
        ],
        [
            KeyboardButton(text="🔙️ Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

rekKey1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasm"),
            KeyboardButton(text="Video")
        ],
        [
            KeyboardButton(text='Text'),
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)
back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙️ Orqaga'),
        ]
    ],
    resize_keyboard=True
)

back_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Shart emas'),
         KeyboardButton(text='Back')]
    ],
    resize_keyboard=True
)
back_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Back')]
    ],
    resize_keyboard=True
)
