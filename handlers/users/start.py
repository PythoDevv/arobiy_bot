import asyncio
import json

import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from data.config import ADMINS
from keyboards.default.buttons import main, lessons_1, books_1, vid_1, vid_2, lessons_2, lessons_3, ten
from keyboards.default.rekKeyboards import back, picture
from loader import dp, db, bot
from states.LessonsState import ChanelData, Lessons
from utils.misc import subscription

chanel_id = -1001639246848


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo_id(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    if state:
        await state.finish()
    status = True
    all = await db.select_chanel()
    chanels = []
    url = []
    for i in all:
        chanels.append(i['chanelll'])
        url.append(i['url'])

    for channel in chanels:
        status *= await subscription.check(user_id=message.from_user.id,
                                           channel=f'{channel}')
    if status:
        await message.answer('Kerakli bo`limni tanlang', reply_markup=main)
    else:
        button = types.InlineKeyboardMarkup(row_width=1, )
        for i in url:
            button.add(types.InlineKeyboardButton("📲 | A'zo bo'lish ", url=f'https://t.me/{i}'))
        button.add(types.InlineKeyboardButton(text="✅ Азо бўлдим", callback_data="check_subs"))
        await message.answer(f'Kаналга аъзо бўлинг. '
                             f'Кейин "Аъзо бўлдим" тугмасини босинг',
                             reply_markup=button,
                             disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery, state: FSMContext):
    try:
        user = await db.add_user(telegram_id=call.from_user.id,
                                 full_name=call.from_user.full_name,
                                 username=call.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=call.from_user.id)

    await call.answer()
    result = str()
    result2 = str()
    status = True
    all = await db.select_chanel()
    chanels = []
    url = []
    for i in all:
        chanels.append(i['chanelll'])
        url.append(i['url'])
    for channel in chanels:
        status *= await subscription.check(user_id=call.from_user.id,
                                           channel=f'{channel}')
    if status:
        await call.message.answer('Kerakli bo`limni tanlang', reply_markup=main)
    else:
        button = types.InlineKeyboardMarkup(row_width=1, )
        for i in url:
            button.add(types.InlineKeyboardButton("📲 | A'zo bo'lish ", url=f'https://t.me/{i}'))
        button.add(types.InlineKeyboardButton(text="✅ Азо бўлдим", callback_data="check_subs"))
        await call.message.answer(f'🛑Kаналга аъзо бўлинг. '
                                  f'Кейин "Аъзо бўлдим" тугмасини босинг🛑',
                                  reply_markup=button,
                                  disable_web_page_preview=True)


@dp.message_handler(text='📹 ARAB ALIFBOSI  O DAN 🎞️')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('📹 ARAB ALIFBOSI  O DAN 🎞️', reply_markup=lessons_1)
    await Lessons.lessons_1.set()


@dp.message_handler(text='ARABCHA PDF KITOBLAR 📗')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('ARABCHA PDF KITOBLAR 📗', reply_markup=books_1)
    await Lessons.pdf.set()


@dp.message_handler(text='📺ARAB TILIDA S’OZLASHUV VIDEO 📹')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('📺ARAB TILIDA S’OZLASHUV VIDEO 📹', reply_markup=vid_1)
    await Lessons.lessons_2.set()


@dp.message_handler(text='📷Zakariyyo bilan o’rganing 🎞️تعلم مع زكريا')
async def Zakariyo(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('📷Zakariyyo bilan o’rganing', reply_markup=ten)
    await Lessons.lessons_7.set()


# 111
@dp.message_handler(text='MUALLIM SONIY KITOBI PDF 📚')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    try:
        await bot.copy_message(
            chat_id=message.from_user.id,
            from_chat_id=chanel_id,
            message_id=63,
        )
    except Exception as err:
        await message.answer(text=f'{err}')


# 333
@dp.message_handler(text='📜 ARAB TILIDA SOZLASHUV KITOBI PDF 📘')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    try:
        await bot.copy_message(
            chat_id=message.from_user.id,
            from_chat_id=chanel_id,
            message_id=64,
        )
        await bot.copy_message(
            chat_id=message.from_user.id,
            from_chat_id=chanel_id,
            message_id=65,
        )
        await bot.copy_message(
            chat_id=message.from_user.id,
            from_chat_id=chanel_id,
            message_id=66,
        )

    except Exception as err:
        await message.answer(text=f'{err}')


# 111
@dp.message_handler(text='📚النحو التطبيقي')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    try:
        await bot.copy_message(
            chat_id=message.from_user.id,
            from_chat_id=chanel_id,
            message_id=67,
        )
    except Exception as err:
        await message.answer(text=f'{err}')


@dp.message_handler(text='🎞️ARAB TILINI YUQORI DARAJADA BILGANLAR UCHUN')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('🎞️ARAB TILINI YUQORI DARAJADA BILGANLAR UCHUN', reply_markup=lessons_2)
    await Lessons.lessons_4.set()


@dp.message_handler(text='A1. A2 darajasidagi hikoyalar ARABCHA 📺')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('A1. A2 darajasidagi hikoyalar ARABCHA 📺', reply_markup=lessons_3)
    await Lessons.lessons_5.set()


@dp.message_handler(text='👨‍💻ADMIN BILAN ALOQA')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('@arabiy_aloqa_bot')


@dp.message_handler(text='🇸🇦 RASMLARDA ARABCHA  SO’ZLASHUV ☄️')
async def show_users(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer('🇸🇦 RASMLARDA ARABCHA  SO’ZLASHUV ☄️', reply_markup=picture)
    await Lessons.picture.set()


@dp.message_handler(text='🔝 Asosiy Menyu', state='*')
async def mainMenu(message: types.Message, state: FSMContext):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer("Bosh sahifa", reply_markup=main)
    await state.finish()


@dp.message_handler(Command('jsonFile'))
async def jsonnn(message: types.Message):
    user_list = []
    userss = await db.select_all_users()
    for user in userss:
        user_dict = {}
        user_dict['full_name'] = user[1]
        user_dict['username'] = user[2]
        user_dict['tg_id'] = user[3]
        user_list.append(user_dict)
        await asyncio.sleep(0.05)
    with open("users.json", "w") as outfile:
        json.dump(user_list, outfile)
    document = open('users.json')
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(Command('read_file'))
async def json_reader(message: types.Message):
    f = open('users.json', 'r')
    data = json.loads(f.read())
    for user in data:
        try:
            await db.add_json_file_user(
                username=user['username'],
                full_name=user['full_name'],
                telegram_id=user['tg_id'],
            )
        except Exception as e:
            print(e)
    f.close()
