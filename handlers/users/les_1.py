from aiogram import types
from aiogram.dispatcher import FSMContext


from keyboards.default.buttons import main
from loader import bot, dp
from states.LessonsState import Lessons

chanel_id = -1001639246848


@dp.message_handler(state=Lessons.lessons_1)
async def lesson_1_main(message: types.Message, state: FSMContext):
    if message.text == '1-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=3,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '2-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=4,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '3-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=5,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '4-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=6,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '5-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=7,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '6-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=8
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '7-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=9,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "8-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=10,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '9-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=11,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '10-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=12,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '11-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=13,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '12-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=14,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '13-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=15,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "14-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=16,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '15-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=17,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "16-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=18,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '17-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=19,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '18-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=20,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '19-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=21,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '20-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=22,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '21-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=23,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '22-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=24,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '23-dars':
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=25,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "24-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=26,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "25-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=27,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "26-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=28,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "27-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=29,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "28-dars":
        try:
            await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=30,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '🔙️ Orqaga':
        await message.answer('Asosiy Bo`lim', reply_markup=main)
        await state.finish()

