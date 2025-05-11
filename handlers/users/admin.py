#
# import asyncio
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils import exceptions
#
# from data.config import ADMINS
# from keyboards.default.all import first_k
# from keyboards.default.pic_keyboards import menu
# from keyboards.default.rekKeyboards import rekKey1, back
# from loader import dp, db, bot
# from states.rekStates import RekData, ChanelData
#
#
# @dp.message_handler(text="/rekkk", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message):
#     await message.answer(text='Rasm yoki Video kiritishni tanlang', reply_markup=rekKey1)
#     await RekData.choice.set()
#
#
# @dp.message_handler(state=RekData.choice)
# async def choice(message: types.Message, state: FSMContext):
#     if message.text == 'Rasm':
#         await message.answer(text='Rasmni kiriting', reply_markup=back)
#         await RekData.picture.set()
#     elif message.text == 'Video':
#         await message.answer(text='Videoni kiriting', reply_markup=back)
#         await RekData.video.set()
#     elif message.text == 'Text':
#         await message.answer(text='Textni kiriting', reply_markup=back)
#         await RekData.text.set()
#     elif message.text == 'Back':
#         await message.answer(text='Back', reply_markup=menu)
#         await state.finish()
#
#
# #
# #
# @dp.message_handler(state=RekData.video, content_types=types.ContentTypes.VIDEO)
# async def rek_video(message: types.Message, state: FSMContext):
#     if message.text == 'Back':
#         await state.finish()
#         await message.answer('Bosh first_k', reply_markup=first_k)
#     elif message.text == 'Shart emas':
#         await message.answer(text='Text ni kiriting')
#         await RekData.text.set()
#     else:
#         video_id = message.video.file_id
#         await state.update_data(
#             {"video_id": video_id}
#         )
#         await message.answer(text='Video qabul qilindi.\n\n'
#                                   'Button Textni kiriting ')
#         await RekData.but_text.set()
#
#
# @dp.message_handler(state=RekData.picture, content_types=types.ContentTypes.PHOTO)
# async def rek_picture(message: types.Message, state: FSMContext):
#     if message.text == 'Back':
#         await state.finish()
#         await message.answer('Bosh first_k', reply_markup=first_k)
#     elif message.text == 'Shart emas':
#         await message.answer(text='Text ni kiriting')
#         await RekData.text.set()
#     else:
#         image_id = message.photo[-1].file_id
#         await state.update_data(
#             {"image_id": image_id}
#         )
#         await message.answer(text='Rasm qabul qilindi,\n'
#                                   'Button Textni kiriting')
#         await RekData.but_text.set()
#
#
# @dp.message_handler(state=RekData.but_text)
# async def rek_Keyboard(message: types.Message, state: FSMContext):
#     if message.text == 'Back':
#         await state.finish()
#         await message.answer('Bosh first_k', reply_markup=first_k)
#     # elif message.text == 'Shart emas':
#     #     await message.answer(text='Url kiriting')
#     #     await RekData.hashTag.set()
#     else:
#         but_text = message.text.split(',')
#         await state.update_data(
#             {'but_text': but_text}
#         )
#         await message.answer(text='Button text qabul qilindin\n'
#                                   'Url kiriting')
#         await RekData.url.set()
#
#
# @dp.message_handler(state=RekData.url)
# async def rek_Keyboard(message: types.Message, state: FSMContext):
#     if message.text == 'Back':
#         await state.finish()
#         await message.answer('Bosh first_k', reply_markup=first_k)
#     # elif message.text == 'Shart emas':
#     #     await message.answer(text='Hashtagni kiriting')
#     #     await RekData.hashTag.set()
#     else:
#         url = message.text.split(',')
#         await state.update_data(
#             {'url': url}
#         )
#         await message.answer(text='Url qabul qilindin\n'
#                                   'Text ni kiriting')
#         await RekData.text.set()
#
#
# # @dp.message_handler(state=RekData.hashTag)
# # async def rek_Hashtags(message: types.Message, state: FSMContext):
# #     if message.text == 'Back':
# #         await state.finish()
# #         await message.answer('Bosh first_k', reply_markup=first_k)
# #     elif message.text == 'Shart emas':
# #         await message.answer(text='Textni kiriting')
# #         await RekData.text.set()
# #     else:
# #         hashTag = message.text
# #         await state.update_data(
# #             {'hashTag': hashTag}
# #         )
# #         await message.answer(text='Hash Tag qabul qilindi\n'
# #                                   'Text ni kiriting')
# #         await RekData.text.set()
#
#
# @dp.message_handler(state=RekData.text)
# async def rek_text(message: types.Message, state: FSMContext):
#     counter = 0
#     err_counter = 0
#     if message.text == 'Back':
#         await message.answer('Bosh first_k', reply_markup=first_k)
#         await state.finish()
#     else:
#         rek_text = message.text
#         await state.update_data(
#             {"text": rek_text}
#         )
#         # await RekData.next()
#         data = await state.get_data()
#         image_id = data.get("image_id")
#         video = data.get("video_id")
#         text = ''
#
#         # if data.get('text') is not None:
#         #     text += '\n'
#         #     text += f'{data.get("text")}'
#         # if data.get('hashTag') is not None:
#         #     text += '\n'
#         #     text += f'{data.get("hashTag")}'
#         # button = types.InlineKeyboardMarkup(row_width=1, )
#         # button.add(types.InlineKeyboardButton("📲 | A'zo bo'lish ", url=f'https://t.me/'))
#         # button.add(*(types.InlineKeyboardButton(text=str(i) for i in data, url='sadasd')))
#         rek_but = types.InlineKeyboardMarkup(row_width=1, )
#
#         if data.get('bu_text') is not None:
#             but_text = data.get('but_text')
#             url_text = data.get('url')
#             rek_but = types.InlineKeyboardMarkup(row_width=1, )
#             for i in range((len(but_text))):
#                 print(but_text[0])
#                 # rek_but = InlineKeyboardMarkup(
#                 #     inline_keyboard=[[
#                 #         InlineKeyboardButton(text=f"{but_text[i]}", url=f"{url_text[i]}"),
#                 #     ]
#                 #     ])
#                 rek_but.add(types.InlineKeyboardButton(text=f'{but_text[i]}', url=f'{url_text[i]}'))
#
#         users = await db.select_all_users()
#         for user in users:
#             user_id = user[6]
#             try:
#                 if data.get('image_id') is not None:
#                     await bot.send_photo(chat_id=user_id, photo=image_id, caption=message.text,
#                                          reply_markup=rek_but)
#                     counter += 1
#                 elif data.get('video_id') is not None:
#                     await bot.send_video(chat_id=user_id, video=video, caption=message.text,
#                                          )
#                     counter += 1
#                 else:
#                     await message.send_copy(chat_id=user_id, protect_content=message.text)
#                     counter += 1
#             except:
#                 err_counter += 1
#                 continue
#             await asyncio.sleep(0.05)
#     await state.finish()
#     userssss = await db.count_users()
#     await message.answer(f"<b>Xabar {counter}-ta foydalanuchiga jo'natildi"
#                          f"Xabar {err_counter}-ta foydalanuvchiga yuborilmadi"
#                          f"Bazada {userssss}-ta foydalanuvchi bor</b>", reply_markup=first_k)
#
#
# @dp.message_handler(state='*')
# async def back_all(message: types.Message, state: FSMContext):
#     if message.text == 'Back':
#         await message.answer(text='Bosh menu', reply_markup=first_k)
#         await state.finish()
# # import asyncio
# #
# # from aiogram import types
# # from aiogram.dispatcher import FSMContext
# #
# # from data.config import ADMINS
# # from loader import db, dp
# # from states.LessonsState import Testt
#
#
# # @dp.message_handler(text='POST', user_id=ADMINS)
# # async def bot_start(msg: types.Message, state: FSMContext):
# #     await msg.answer("<b>POST ni yuboring</b>")
# #     await Testt.testt.set()
# #
# #
# # @dp.message_handler(content_types=['video', 'audio', 'voice', 'photo', 'document', 'text'], user_id=ADMINS,
# #                     state=Testt.testt)
# # async def contumum(msg: types.Message, state: FSMContext):
# #     if msg.video or msg.audio or msg.voice or msg.document or msg.photo or msg.text:
# #
# #         await state.finish()
# #
# #         users = await db.select_all_users()
# #         count_baza = await db.count_users()
# #         count_err = 0
# #         count = 0
# #         for user in users:
# #             user_id = user[3]
# #             try:
# #                 await msg.forward(chat_id=user_id)
# #
# #                 count += 1
# #
# #             except Exception as err:
# #                 count_err += 1
# #
# #             await asyncio.sleep(0.1)
# #         await asyncio.sleep(0.1)
# #
# #         await msg.answer(f"Ҳабар юборилганлар: <b>{count}</b> та."
# #                          f"\n\nЮборилмаганлар: <b>{count_err}</b> та."
# #                          f"\n\nБазада жами: <b>{count_baza}</b> та"
# #                          f" фойдаланувчи мавжуд."
# #                          )
import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin_keyboards import admin_key
from loader import db, dp
from states.LessonsState import Testt


# from states.pic import Testt


@dp.message_handler(text='Xabar Yuborish 🗒', user_id=ADMINS)
async def bot_start(msg: types.Message, state: FSMContext):
    await msg.answer("<b>Xabarni ni yuboring</b>")
    await Testt.testt.set()


@dp.message_handler(content_types=['video', 'audio', 'voice', 'photo', 'document', 'text'], user_id=ADMINS,
                    state=Testt.testt)
async def contumum(msg: types.Message, state: FSMContext):
    if msg.video or msg.audio or msg.voice or msg.document or msg.photo or msg.text:

        await state.finish()

        users = await db.select_all_users()
        count_baza = await db.count_users()
        count_err = 0
        count = 0
        for user in users:
            user_id = user[3]
            try:
                await msg.send_copy(chat_id=user_id)
                count += 1
                await asyncio.sleep(0.1)

            except Exception as err:
                count_err += 1
                await asyncio.sleep(0.1)

        await msg.answer(f"Ҳабар юборилганлар: <b>{count}</b> та."
                         f"\n\nЮборилмаганлар: <b>{count_err}</b> та."
                         f"\n\nБазада жами: <b>{count_baza}</b> та"
                         f" фойдаланувчи мавжуд.", reply_markup=admin_key
                         )
