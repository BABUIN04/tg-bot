from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           ReplyKeyboardMarkup, KeyboardButton)
from aiogram.types import CallbackQuery

def subjectkb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text ='ХИМИЯ🧪', url='https://reshak.ru/reshebniki/ximiya/9/gabrielyan/index.html'),
         InlineKeyboardButton(text='ГЕОГРАФИЯ🌍', url='https://reshak.ru/reshebniki/geograph/9/alexeev_nikolina/index.html'),
        ],
        [
            InlineKeyboardButton(text = 'ИСТОРИЯ⚔️', url='https://reshak.ru/reshebniki/istoria/9/udovskaya/index.html'),
            InlineKeyboardButton(text='ИНФОРМАТИКА💻', url='https://reshak.ru/reshebniki/informatika/9/bosova_uchebnik/index.html')
        ],
        [
            InlineKeyboardButton(text='БИОЛОГИЯ🍃', url='https://reshak.ru/reshebniki/biologia/9/pasechnik/index.html'),
            InlineKeyboardButton(text='АНГЛИЙСКИЙ💂', url='https://gdz.ru/class-9/english/reshebnik-spotlight-9-vaulina-yu-e/')
        ],
        [
            InlineKeyboardButton(text='АЛГЕБРА🧮', url='https://reshak.ru/reshebniki/algebra/9/merzlyak/index.html'),
            InlineKeyboardButton(text='ГЕОМЕТРИЯ✏️', url='https://reshak.ru/reshebniki/geometriya/9/merzlyak/index.html')
        ],
        [
            InlineKeyboardButton(text='ОБЩЕСТВОЗНАНИЕ📄', url='https://reshak.ru/reshebniki/obshestvo/9/bogolubov/index.html'),
            InlineKeyboardButton(text='ФИЗИКА⚙️', url='https://gdz.ru/class-9/fizika/peryshkin-gutnik/')
        ],
    ])
    return kb

def timetable():
    ttable = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='ПОНЕДЕЛЬНИК', callback_data='monday')],
        [InlineKeyboardButton(text='ВТОРНИК', callback_data='tuesday')],
        [InlineKeyboardButton(text='СРЕДА', callback_data='wednesday')],
        [InlineKeyboardButton(text='ЧЕТВЕРГ', callback_data='thursday')],
        [InlineKeyboardButton(text='ПЯТНИЦА', callback_data='friday')]
    ])
    return ttable

def subjects():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text ='ХИМИЯ🧪', callback_data='che'),
         InlineKeyboardButton(text='ГЕОГРАФИЯ🌍', callback_data='geo'),
        ],
        [
            InlineKeyboardButton(text = 'ИСТОРИЯ⚔️', callback_data='his'),
            InlineKeyboardButton(text='ИНФОРМАТИКА💻', callback_data='it')
        ],
        [
            InlineKeyboardButton(text='БИОЛОГИЯ🍃', callback_data='bio'),
            InlineKeyboardButton(text='АНГЛИЙСКИЙ💂', callback_data='eng')
        ],
        [
            InlineKeyboardButton(text='АЛГЕБРА🧮', callback_data='alg'),
            InlineKeyboardButton(text='ГЕОМЕТРИЯ✏️', callback_data='gmt')
        ],
        [
            InlineKeyboardButton(text='ОБЩЕСТВОЗНАНИЕ📄', callback_data='obs'),
            InlineKeyboardButton(text='ФИЗИКА⚙️', callback_data='phy')
        ],
    ])
    return kb

def chemistry():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text = 'ДОБАВИТЬ ФОТО', callback_data='addche'),
         InlineKeyboardButton(text = 'ВЫВЕСТИ ФОТО', callback_data= 'allche')],
        [InlineKeyboardButton(text= 'МЕНЮ ПРЕДМЕТОВ', callback_data= 'back')]
    ])
    return kb