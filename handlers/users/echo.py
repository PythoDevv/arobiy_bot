import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import db, dp
from states.LessonsState import Testt


@dp.message_handler(text='POST', user_id=ADMINS)
async def bot_start(msg: types.Message, state: FSMContext):
    await msg.answer("<b>POST ni yuboring</b>")
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

            except Exception as err:
                count_err += 1

            await asyncio.sleep(0.1)
        await asyncio.sleep(0.1)

        await msg.answer(f"Ҳабар юборилганлар: <b>{count}</b> та."
                         f"\n\nЮборилмаганлар: <b>{count_err}</b> та."
                         f"\n\nБазада жами: <b>{count_baza}</b> та"
                         f" фойдаланувчи мавжуд."
                         )
