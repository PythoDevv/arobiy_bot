from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import main
from loader import bot, dp
from states.LessonsState import Lessons

chanel_id = -1001639246848


@dp.message_handler(state=Lessons.pdf)
async def pdf(message: types.Message, state: FSMContext):
    if message.text == '1-5':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=31,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=32,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=33,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=34,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=35,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '6-10':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=36,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=37,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=38,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=39,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=40,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '11-15':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=41,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=42,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=43,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=44,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=45,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '16':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=46,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '🔙️ Orqaga':
        await message.answer('Asosiy Bo`lim', reply_markup=main)
        await state.finish()

@dp.message_handler(state=Lessons.lessons_2)
async def les_2(message: types.Message, state: FSMContext):
    if message.text == '1-3':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=47,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=48,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=49,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '4-7':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=50,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=51,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=52,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=53,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '8-10':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=54,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=55,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=56,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '11-14':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=54,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=55,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=56,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '15-20':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=57,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=58,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=59,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=60,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '🔙️ Orqaga':
        await message.answer('Asosiy Bo`lim', reply_markup=main)
        await state.finish()



# @dp.message_handler(state=Lessons.lessons_3)
# async def les_3(message: types.Message, state: FSMContext):
#     if message.text == '1-2':
#         try:
#             await bot.copy_message(
#                 chat_id=message.from_user.id,
#                 from_chat_id=chanel_id,
#                 message_id=61,
#             )
#             await bot.copy_message(
#                 chat_id=message.from_user.id,
#                 from_chat_id=chanel_id,
#                 message_id=62,
#             )
#         except Exception as err:
#             await message.answer(text=f'{err}')
#     elif message.text == '3-4':
#         try:
#             await bot.copy_message(
#                 chat_id=message.from_user.id,
#                 from_chat_id=chanel_id,
#                 message_id=63,
#             )
#             await bot.copy_message(
#                 chat_id=message.from_user.id,
#                 from_chat_id=chanel_id,
#                 message_id=64,
#             )
#         except Exception as err:
#             await message.answer(text=f'{err}')
#     elif message.text == '🔙️ Orqaga':
#         await message.answer('Asosiy Bo`lim', reply_markup=main)
#         await state.finish()
