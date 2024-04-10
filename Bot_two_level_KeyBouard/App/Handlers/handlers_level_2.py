import sqlite3
from aiogram import types, Router, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from App.Keybouards.keyboards import (KeyBouard, inl1, keyButton_st_rg, KeyBouard_level2)
from App.Function.defes import delete, update_Problem, user_id, value_keys
from App.States.FSM_State import Reg_update_problem
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from App.Handlers.handlers_level_1 import admin
sqlite3.connect("Data_Base/Now_bot.db")
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
router = Router()
name_table = table_name = id = []
flag = flag2 = False
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router.message(Command("start", "startt"))
async def cmd_start(message: types.Message):
    print(message.from_user.id, message.from_user.username)
    await message.answer(text='Привет!', reply_markup=keyButton_st_rg())
    await message.answer(f'\n<blockquote>'
                         f'<b>'
                         f'<i>'
                         f'Все доступные проблемы представлены ниже.'
                         f'\nКОРНЕВЫЕ ПРОБЛЕМЫ:'
                         f'</i>'
                         f'</b>'
                         f'</blockquote>', parse_mode="HTML", reply_markup=KeyBouard())


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router.message(Command("clear"))
async def cmd_clear(message: Message, bot: Bot) -> None:
    try:
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        if ex.message == "Bad Request: message to delete not found":
            pass


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router.callback_query()
async def catalog6(call: CallbackQuery, state: FSMContext):
    global name_table, table_name, id
    table_name = []
    name_table = id = []

    for i in inl1:
        if str(((call.model_dump(exclude_none=True))['data'][2:7])).replace("*", "").replace("'", "") == str(i):
            await call.answer()
            chapter = (str(((call.model_dump(exclude_none=True))["data"][7:-1])).replace(",", "").replace("*", "")).upper()
            chapter = chapter.replace("' ", "")
            for val in value_keys('values_keys'):
                if val[0] == i:
                    chapter += f' {val[3]}'.upper()
            await call.message.edit_text(
                text=
                f'<blockquote>'
                f'<b>'
                f'<i>'
                f'РAЗДЕЛ: {chapter}'
                f'</i>'
                f'</b>'
                f'</blockquote>',
                parse_mode="HTML",
                reply_markup=(KeyBouard_level2(str(((call.model_dump(exclude_none=True))["data"][7:-1])).replace(",", "").replace("*", "").replace("' ", ""))))

        id = str(((call.model_dump(exclude_none=True))['data'][2:7])).replace("*", "").replace("'", "")
        if id == '??'+str(i) and user_id(call) == 1:
            name_table.append(str((call.model_dump(exclude_none=True))["data"][7:-1]).
                              replace(",", "").
                              replace("*", "").
                              replace("' ", "").
                              replace("[\" \'", "['''").replace("\\", ""))
            name_table = name_table[0]
            await call.answer()
            delete(id.replace("??", ""), name_table, '0')
            await call.message.edit_text(text=f'\n<blockquote>'
                                              f'<b>'
                                              f'<i>'
                                              f'Все доступные проблемы представлены ниже.'
                                              f'\nКОРНЕВЫЕ ПРОБЛЕМЫ:'
                                              f'</i>'
                                              f'</b>'
                                              f'</blockquote>', parse_mode="HTML", reply_markup=KeyBouard())
        if id == '??'+str(i) and user_id(call) != 1:
            await call.answer('❌❌❌ У вашего аккаунта нет прав для редактирования.\n'
                              'По все всем вопросам обращайтесь к администратору {admin} ❌❌❌ .', show_alert=True)
        if id == f'...{str(i)}' and user_id(call) == 1:
            table_name.clear()
            table_name.append(str((call.model_dump(exclude_none=True))["data"][7:-1]).
                              replace(",", "").
                              replace("*", "").
                              replace("' ", "").
                              replace("[\" \'", "['''"))
            table_name = str(table_name).replace("[", "").replace("]", "").replace('\"\'', "").replace("\'\"", "").replace("\\", "")
            await call.answer()
            await call.message.answer(text='Введите новое название раздела.\nНазвание раздела может содержать в себе не '
                                           'более 4080 символов. Символы "*", "\\" не воспринимаеются. Кавычки доступны для ввода'
                                           'в формате « » .')
            await state.set_state(Reg_update_problem.id)

            @router.message(Reg_update_problem.id)
            async def reg_one(message: Message):
                if len(message.text) <= 4080:
                    await message.answer('Название изменено!')
                    await state.update_data(problem=message.text.lower())
                    data = await state.get_data()
                    con = sqlite3.connect("Data_Base/Now_bot.db")
                    con.commit()
                    con.close()
                    update_Problem(id.replace("...", ""), "DB", data["problem"], f'{table_name}', f'{data["problem"]}')

                    await call.message.edit_text(text=f'\n<blockquote>'
                                                      f'<b>'
                                                      f'<i>'
                                                      f'Все доступные проблемы представлены ниже.'
                                                      f'\nКОРНЕВЫЕ ПРОБЛЕМЫ:'
                                                      f'</i>'
                                                      f'</b>'
                                                      f'</blockquote>', parse_mode="HTML", reply_markup=KeyBouard())
                    await state.clear()
                else:
                    await message.answer(f'Длина сообщения может быть не более 4080 символов.\nВ вашем содержится {len(message.text)} символов.')

        if id == f'...{str(i)}' and user_id(call) != 1:
            await call.answer('❌❌❌ У вашего аккаунта нет прав для редактирования.\n'
                              f'По все всем вопросам обращайтесь к администратору {admin} ❌❌❌ .', show_alert=True)
        else:
            pass
    return name_table
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''





