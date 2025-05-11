from aiogram.dispatcher.filters.state import StatesGroup, State


class Lessons(StatesGroup):
    lessons_1 = State()
    lessons_2 = State()
    lessons_3 = State()
    lessons_4 = State()
    lessons_5 = State()
    lessons_6 = State()
    lessons_7 = State()
    lessons_8 = State()
    lessons_9 = State()
    lessons_10 = State()
    lessons_11 = State()
    lessons_12 = State()
    lessons_13 = State()
    lessons_14 = State()
    lessons_15 = State()
    picture = State()
    pdf = State()


class Testt(StatesGroup):
    testt = State()


class ChanelData(StatesGroup):
    add = State()
    delete = State()
