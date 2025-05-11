from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import main
from loader import bot, dp
from states.LessonsState import Lessons

chanel_id = -1001804250794


@dp.message_handler(state=Lessons.picture)
async def picture(message: types.Message, state: FSMContext):
    if message.text == '1-qism':
        try:
            for i in range(62, 71):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '2-qism':
        try:
            for i in range(72, 81):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )
        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '3-qism':
        try:
            for i in range(82, 91):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )

        except Exception as err:
            await message.answer(text=f'{err}')

    elif message.text == '4-qism':
        try:
            for i in range(92, 101):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )
        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '5-qism':
        try:
            for i in range(102, 111):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '6-qism':
        try:
            for i in range(112, 121):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '7-qism':
        try:
            for i in range(122, 131):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == "8-qism":
        try:
            for i in range(132, 141):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '9-qism':
        try:
            for i in range(142, 151):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '10-qism':
        try:
            for i in range(152, 161):
                await bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=chanel_id,
                message_id=i,
            )

        except Exception as err:
            await message.answer(text=f'{err}')
    elif message.text == '🔙️ Orqaga':
        await message.answer('Asosiy qism', reply_markup=main)
        await state.finish()
