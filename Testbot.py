from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import aiosqlite


import keyboards as kb
from aiogram.types import CallbackQuery


bot = Bot('7679576329:AAFE1jUR8SvSY8i2IjUmOcUamVg7PdWzEOI')
dispatcher = Dispatcher()
SUBJECT = None

async def newuser(login, tg_id):
    async with aiosqlite.connect('БД.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users (login TEXT, tg_id BIGINT)')
        await db.execute('INSERT INTO users (login, tg_id) VALUES (?, ?)', (login, tg_id))
        await db.execute('CREATE TABLE IF NOT EXISTS images(image_id TEXT, subject TEXT)')
        await db.commit()

@dispatcher.message(Command('start'))
async def handler_message(msg: Message):
    await msg.answer('Привет, это бот для домашки.')
    print('ok')
    login = msg.from_user.username
    tg_id = msg.from_user.id
    await  newuser(login, tg_id)

@dispatcher.message(Command('savephoto'))
async def handler_message(msg: Message):
    await msg.answer(text = 'ПРЕДМЕТЫ:', reply_markup= kb.subjects())

@dispatcher.callback_query(F.data == 'che')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'хим'

@dispatcher.callback_query(F.data == 'geo')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'гео'

@dispatcher.callback_query(F.data == 'his')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'ист'

@dispatcher.callback_query(F.data == 'it')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'ит'

@dispatcher.callback_query(F.data == 'bio')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'био'

@dispatcher.callback_query(F.data == 'eng')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'анг'

@dispatcher.callback_query(F.data == 'alg')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'алг'

@dispatcher.callback_query(F.data == 'gmt')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'гем'

@dispatcher.callback_query(F.data == 'obs')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'общ'

@dispatcher.callback_query(F.data == 'phy')
async def addchemistry(callback: CallbackQuery):
    global SUBJECT
    await callback.message.edit_text(text = 'ДОБАВЬТЕ ФОТО:', reply_markup=kb.chemistry())
    SUBJECT = 'физ'

@dispatcher.callback_query(F.data == 'back')
async def show_photos(cb: CallbackQuery):
    await cb.message.edit_text(text = 'ПРЕДМЕТЫ:', reply_markup= kb.subjects())

@dispatcher.callback_query(F.data == 'allche')
async def show_photos(cb: CallbackQuery):
    global SUBJECT
    async with aiosqlite.connect('БД.db') as db:
        cursor = await db.execute(f"SELECT * FROM images WHERE subject = '{SUBJECT}'")
        result = await cursor.fetchall()
        for i in result:
            await cb.message.answer_photo(i[0])
        if not result:
            await cb.message.answer(text = 'Фоток нет')
    #SUBJECT = None

@dispatcher.callback_query(F.data == 'addche')
async def save_photo(cb: CallbackQuery):
        await cb.message.answer('Загрузите фото')

@dispatcher.message(F.photo)
async def save_phot(cb: Message):
    global SUBJECT
    if SUBJECT is None:
        await cb.answer('Выберите предмет')
        return
    subject = 'хим'
    print(cb.photo)
    file_id = cb.photo[-1].file_id
    await cb.bot.download(file=file_id, destination='images/' + file_id + '.jpeg')
    async with aiosqlite.connect('БД.db') as db:
        await db.execute('INSERT INTO images (image_id, subject) VALUES (?, ?)', (file_id, SUBJECT,))
        await db.commit()
    await cb.answer(text='Ваше фото загружено!')
    #SUBJECT = None

@dispatcher.message(Command('timetable'))
async def gdz(msg: Message):
    await msg.answer(
        text = 'Расписание:',
        reply_markup = kb.timetable()
    )

@dispatcher.callback_query(F.data == 'monday')
async def timetable_handler(callback: CallbackQuery):
    await callback.message.answer('''ПОНЕДЕЛЬНИК: 
1. Химия 
2. История 
3. География 
4. Английский язык 
5. Разговор о важном
6. Математика 
7. Родной язык ''')

@dispatcher.callback_query(F.data == 'tuesday')
async def timetable_handler(callback: CallbackQuery):
    await callback.message.answer('''ВТОРНИК: 
1. История
2. Физра
3. Русский 
4. Литература
5. Математика
6. Математика 
7. Физика ''')

@dispatcher.callback_query(F.data == 'wednesday')
async def timetable_handler(callback: CallbackQuery):
    await callback.message.answer('''СРЕДА: 
1. Информатика 
2. Биология 
3. Английский язык 
4. Русский язык 
5. Литература
6. Математика 
7. Основы программирования на Python ''')

@dispatcher.callback_query(F.data == 'thursday')
async def timetable_handler(callback: CallbackQuery):
    await callback.message.answer('''ЧЕТВЕРГ: 
1. Физика 
2. Русский язык 
3. Обществознание 
4. Физическая культура 
5. Химия
6. География 
7. Математика ''')

@dispatcher.callback_query(F.data == 'friday')
async def timetable_handler(callback: CallbackQuery):
    await callback.message.answer('''ПЯТНИЦА: 
1. английский язык 
2. Биология 
3. История 
4. литература
5. ОБЗР(обж)
6. физика
7. Математика ''')

@dispatcher.message(Command('subjects'))
async def handler_message(msg: Message):
    await msg.answer('ПРЕДМЕТЫ:',reply_markup=kb.subjectkb())



@dispatcher.message(Command('dates'))
async def find_dates(msg: Message):
    async with aiosqlite.connect('БД.db') as db:
        cursor = await db.execute(f"SELECT subject,date, COUNT(subject) FROM images GROUP BY date, subject")
        print(cursor)
        result = await cursor.fetchall()
        text = ''
        for i in result:
            text += str(i) + '\n'
        txt = 'ДАТЫ ОТПРАВКИ ФОТОГРАФИЙ:' + '\n' + text
        await msg.answer(txt)
dispatcher.run_polling(bot)