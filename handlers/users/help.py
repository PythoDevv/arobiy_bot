from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.default.buttons import main
from loader import dp, bot
from states.LessonsState import Lessons

chanel_id = -1001804250794


@dp.message_handler(state=Lessons.lessons_4)
async def lesson_4_main(message: types.Message, state: FSMContext):
    if message.text == '1-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=11,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '2-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=12,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '3-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=13,
            )

        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '4-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=14,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '5-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=15,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '6-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=16,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '7-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=17,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "8-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=18,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '9-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=19,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '10-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=20,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '🔙️ Orqaga':
        await message.answer('Asosiy Bo`lim', reply_markup=main)
        await state.finish()


@dp.message_handler(state=Lessons.lessons_5)
async def lesson_5_main(message: types.Message, state: FSMContext):
    if message.text == '1-5 darslar':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=22,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=23,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=24,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=25,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=26,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '6-10 darslar':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=27,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=28,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=29,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=30,
            )
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=31,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '11-15 darslar':
        try:
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
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=36,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '16-20 darslar':
        try:
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
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=41,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '21-25 darslar':
        try:
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
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=46,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '26-30 darslar':
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
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '🔙️ Orqaga':
        await message.answer('Asosiy Bo`lim', reply_markup=main)
        await state.finish()


@dp.message_handler(state=Lessons.lessons_7)
async def lessons_7_main(message: types.Message, state: FSMContext):
    if message.text == '1-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=52,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '2-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=53,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '3-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=54,
            )

        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '4-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=55,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '5-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=56,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '6-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=57,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '7-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=58,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "8-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=59,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '9-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=60,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '10-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=61,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '🔙️ Orqaga':
        await message.answer('Asosiy Bo`lim', reply_markup=main)
        await state.finish()
