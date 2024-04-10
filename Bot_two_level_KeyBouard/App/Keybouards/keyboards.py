from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from App.Function.defes import value_keys, value_keys_level2
'''------------------------------------------------------------------------------------------------------------------'''
values_keys = value_keys('values_keys')
keys = value_keys('keys')
value = value_keys('values')
'''------------------------------------------------------------------------------------------------------------------'''
inl1 = inl6 = []
inl = []
inl0 = []
for i in value_keys('values_keys'):
    (
        inl.append
        (
            [
                InlineKeyboardButton(text=f'id = f{i[1]}',
                                     callback_data=f'{str(i[0]) + "***", str(i[1])}'
                                     ),
                InlineKeyboardButton(text='🔄 Изменить', callback_data=f'...{i[0]}'),
                InlineKeyboardButton(text='🗑 Удалить', callback_data=f'..{i[0]}')
            ]
        )
    )
    inl1.append(i[0])
inl.append([InlineKeyboardButton(text='⬇️ Добавить', callback_data='plus'),
            InlineKeyboardButton(text="🔐 Закрыть ред-р", callback_data='78787878787')],)
keyboard = InlineKeyboardMarkup(inline_keyboard=inl)
'''------------------------------------------------------------------------------------------------------------------'''


def KeyBouard_close():
    global inl, inl1, i, keyboard
    inl.clear(), inl1.clear()
    for i in value_keys('values_keys'):
        (
            inl.append
            (
                [
                    InlineKeyboardButton(text=f'{i[1]} {i[3]}',
                                         callback_data=f'{str(i[0])+"***",str(i[1])}'
                                         ),
                    InlineKeyboardButton(text='🔄 Изменить', callback_data=f'{"..."+str(i[0])+"***",str(i[1])}'),
                    InlineKeyboardButton(text='🗑 Удалить', callback_data=f'{"??"+str(i[0])+"***",str(i[1])}'),
                    ]
            )
        )
        inl1.append(i[0])
    inl.append([InlineKeyboardButton(text='⬇️ Добавить', callback_data='plus'),
                InlineKeyboardButton(text="🔐 Закрыть ред-р", callback_data='656565656565656565')])
    keyboard = InlineKeyboardMarkup(inline_keyboard=inl)
    return keyboard


'''------------------------------------------------------------------------------------------------------------------'''


def KeyBouard():
    global inl, inl1, i, keyboard
    inl.clear(), inl1.clear()
    for i in value_keys('values_keys'):
        (
            inl.append
            (
                [
                    InlineKeyboardButton(text=f'{i[1]} {i[3]}',
                                         callback_data=f'{str(i[0])+"***",str(i[1])}'
                                         ),
                    ]
            )
        )
        inl1.append(i[0])
    inl.append([InlineKeyboardButton(text='⬇️ Добавить', callback_data='plus'),
                InlineKeyboardButton(text="📂 Открыть ред-р", callback_data='9898989898989898')]
               )
    keyboard = InlineKeyboardMarkup(inline_keyboard=inl)
    return keyboard


'''------------------------------------------------------------------------------------------------------------------'''


def inl3_():
    inl3 = []
    [inl3.append(f'{z[0], z[1]}') for z in value_keys('values_keys')]
    inl3 = str(inl3).replace("[", "{").replace("]", "}").replace('"', '')
    return inl3


'''------------------------------------------------------------------------------------------------------------------'''


def inl4_():
    inl4 = []
    [inl4.append(z) for z in range(1, 1000)]
    inl4 = str(inl4).replace("[", "{").replace("]", "}").replace('"', '')
    return inl4


'''------------------------------------------------------------------------------------------------------------------'''


def keyButton_st_rg():
    keyboard_st_reg = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='/start')],
        [KeyboardButton(text='/clear')],
    ],
        resize_keyboard=True,
        input_field_placeholder='Выберите пункт меню.')
    return keyboard_st_reg


'''------------------------------------------------------------------------------------------------------------------'''


def KeyBouard_level2_close(x):
    global inl, inl6, i
    inl.clear(), inl6.clear()
    for i in value_keys_level2(x):
        inl.append(
                [
                    InlineKeyboardButton(text=f'{i[1]} {i[3]}',
                                         callback_data=f'LL{i[0]}LLLL'),
                    InlineKeyboardButton(text='🔄 Изменить',
                                         callback_data=f':::{i[0]}'),
                    InlineKeyboardButton(text='🗑 Удалить',
                                         callback_data=f'{i[0]}:::')
                    ]
            )
        inl6.append(f'!{i[0]}!')
    inl.append([InlineKeyboardButton(text='↩️ Назад', callback_data='down'),
               InlineKeyboardButton(text="⬇️ Добавить", callback_data="7878787878787878"),
                InlineKeyboardButton(text="🔐 Закрыть ред-р", callback_data='121212121221212121')])
    keyboard_level2 = InlineKeyboardMarkup(inline_keyboard=inl)
    return keyboard_level2


'''------------------------------------------------------------------------------------------------------------------'''


def KeyBouard_level2(x):
    global inl, inl6, i
    inl.clear(), inl6.clear()
    for i in value_keys_level2(x):
        inl.append(
                [
                    InlineKeyboardButton(text=f'{i[1]} {i[3]}',
                                         callback_data=f'LL{i[0]}LLLL'),
                    ]
            )
        inl6.append(f'!{i[0]}!')
    inl.append([InlineKeyboardButton(text='↩️ Назад', callback_data='down'),
                InlineKeyboardButton(text="⬇️ Добавить", callback_data="7878787878787878"),
                InlineKeyboardButton(text="📂 Открыть ред-р", callback_data='78787878787')])
    keyboard_level2 = InlineKeyboardMarkup(inline_keyboard=inl)
    return keyboard_level2


