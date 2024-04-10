import sqlite3
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from App.Function.defes import create_string, delete, user_id, update_Decision_Problem
from App.States.FSM_State import Reg_update_problem, Reg_update_problem1, Reg_update_problem2
from aiogram.fsm.context import FSMContext
from App.Keybouards.keyboards import KeyBouard, KeyBouard_level2, KeyBouard_level2_close, KeyBouard_close

save = None
router_two = Router()
name_table = []
table_name = []
admin = "1234" # Указать Tg к кому обращаться
flag_1board = False
decision = []
flag = False
from App.Function.defes import name_table_from_value_keys_level2
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
inl4 = []
[inl4.append(str('LL')+str(w)+'LLLL') for w in range(1000)]
inl5 = []
[inl5.append(str(':::')+str(w)) for w in range(1000)]
inl6 = []
[inl6.append(str(w)+str(':::')) for w in range(1000)]
a = []


@router_two.callback_query(F.data.in_((str(inl4).replace("[", "{").replace("]", "}"))))
async def catalog(call: CallbackQuery):
    global a
    for i in inl4:
        if str((call.model_dump(exclude_none=True))['data']) == str(i):
            await call.answer(f'Вы выбрали каталог', show_alert=False)
            con = sqlite3.connect('Data_Base/Now_bot.db')
            cur = con.cursor()
            c = (str(call.message.text.lower().replace("рaздел:  ", ""))[0:35] + "\'").replace(".'", "")
            p = cur.execute(f"SELECT Decision FROM {c} WHERE ROWID = {str(i).replace('LL', '')}")
            h = p.fetchall()[0][0].split(',')
            cnt = 0
            pod_problem = cur.execute(f"SELECT Problem FROM {c} WHERE ROWID = {str(i).replace('LL', '')}")
            pod_problem = (str(list(pod_problem)).replace("\'", "").replace("[(", "").replace(".", "").replace(")]", ""))
            await call.message.answer(f"<blockquote><b><i>Раздел: {c}/ Подраздел: {pod_problem}</i></b></blockquote>")
            await call.message.answer(f"<blockquote><b><i>Рещение: </i></b></blockquote>")
            for m in h:
                cnt += 1
            for cnt_str_decision in range(cnt):
                if h[cnt_str_decision][1:3] == 'id':
                    await call.message.answer_photo(photo=str(h[cnt_str_decision][4::]).replace("[", "").replace("]", "").
                                                    replace("\'", "").replace("\"", ""))
                if h[cnt_str_decision][0:3] == 'id=':
                    await call.message.answer_photo(photo=str(h[cnt_str_decision][3::]).replace("[", "").replace("]", "").
                                                    replace("\'", "").replace("\"", ""))
                if h[cnt_str_decision][1:9] == 'document':
                    await call.message.answer_document(document=str(h[cnt_str_decision][10::]).replace("[", "").replace("]", "").
                                                    replace("\'", "").replace("\"", ""))
                if h[cnt_str_decision][0:8] == 'document':
                    await call.message.answer_document(document=str(h[cnt_str_decision][9::]).replace("[", "").replace("]", "").
                                                    replace("\'", "").replace("\"", ""))
                if h[cnt_str_decision][1:6] == 'video':
                    await call.message.answer_video(video=str(h[cnt_str_decision][7::]).replace("[", "").replace("]", "").replace("\'", "").replace("\"", ""))
                if h[cnt_str_decision][0:6] == 'video=':
                    print(str(h[cnt_str_decision][6:]).replace("[", "").replace("]", "").replace("\'", "").replace("\"", ""))
                    await call.message.answer_video(video=str(h[cnt_str_decision][6:]).replace("[", "").replace("]", "").replace("\'", "").replace("\"", ""))

                if h[cnt_str_decision][1:6] == 'textt':
                    await call.message.answer(f'{str(h[cnt_str_decision][6:]).replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "")}')

                if h[cnt_str_decision][0:5] == 'textt':
                    await call.message.answer(f'{str(h[cnt_str_decision][5:]).replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "")}')
            con.commit()
            con.close()
        else:
            pass
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data == '121212121221212121')
async def catalog12(call: CallbackQuery):
    if user_id(call) == 1:
        await call.answer(f'ОТКРЫТЬ РЕДАКТОР', show_alert=False)
        await call.message.edit_text(
            f'<blockquote><b><i>{call.message.text}</i></b></blockquote>', parse_mode="HTML",
            reply_markup=KeyBouard_level2((call.message.text.lower().replace("рaздел:  ", ""))[0:35] + "\'"))
    if user_id(call) != 1:
        await call.answer('❌❌❌ У вашего аккаунта нет прав для редактирования.\n'
                          f'По все всем вопросам обращайтесь к администратору {admin} ❌❌❌ .', show_alert=True)
    else:
        pass


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data == '78787878787')
async def catalog12(call: CallbackQuery):
    if user_id(call) == 1:
        await call.answer(f'ОТКРЫТЬ РЕДАКТОР', show_alert=False)
        await call.message.edit_text(f'<blockquote><b><i>{call.message.text}</i></b></blockquote>',
                                     parse_mode="HTML",
                                     reply_markup=KeyBouard_level2_close((call.message.text.lower().replace("рaздел:  ", ""))[0:35] + "\'"))
    if user_id(call) != 1:
        await call.answer('❌❌❌ У вашего аккаунта нет прав для редактирования.\n'
                          'По все всем вопросам обращайтесь к администратору {admin} ❌❌❌ .', show_alert=True)


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data == '9898989898989898')
async def catalog12(call: CallbackQuery):
    if user_id(call) == 1:
        await call.answer(f'ОТКРЫТЬ РЕДАКТОР', show_alert=False)
        await call.message.edit_text(text=f'\n<blockquote>'
                                          f'<b>'
                                          f'<i>'
                                          f'Все доступные проблемы представлены ниже.'
                                          f'\nКОРНЕВЫЕ ПРОБЛЕМЫ:'
                                          f'</i>'
                                          f'</b>'
                                          f'</blockquote>', parse_mode="HTML", reply_markup=KeyBouard_close())
    if user_id(call) != 1:
        await call.answer('❌❌❌ У вашего аккаунта нет прав для редактирования.\n'
                          f'По все всем вопросам обращайтесь к администратору {admin} ❌❌❌ .', show_alert=True)


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data == '656565656565656565')
async def catalog12(call: CallbackQuery):
    if user_id(call) == 1:
        await call.answer(f'ЗАКРЫТЬ РЕДАКТОР', show_alert=False)
        await call.message.edit_text(text=f'\n<blockquote>'
                                          f'<b>'
                                          f'<i>'
                                          f'Все доступные проблемы представлены ниже.'
                                          f'\nКОРНЕВЫЕ ПРОБЛЕМЫ:'
                                          f'</i>'
                                          f'</b>'
                                          f'</blockquote>', parse_mode="HTML", reply_markup=KeyBouard())
    if user_id(call) != 1:
        await call.answer('❌❌❌ У вашего аккаунта нет прав для редактирования.\n'
                          f'По все всем вопросам обращайтесь к администратору {admin} ❌❌❌ .', show_alert=True)


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data.in_((str(inl6).replace("[", "{").replace("]", "}"))))
async def catalog(call: CallbackQuery):
    for i in inl6:

        if str((call.model_dump(exclude_none=True))['data']) == str(i):
            await call.answer(f'Вы выбрали удалить', show_alert=False)
            i = i.replace(":::", "")
            mess = str(call.message.text.lower()).replace('рaздел:  ', "")
            mess = (str(mess)[0: 35]+'\'')
            delete(i, '0', mess)
            await call.message.edit_text(f"{call.message.text}", reply_markup=KeyBouard_level2(mess))
        else:
            pass
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data.in_((str(inl5).replace("[", "{").replace("]", "}"))))
async def catalog(call: CallbackQuery, state: FSMContext):
    for i in inl5:
        if str((call.model_dump(exclude_none=True))['data']) == str(i):
            idd = str((call.model_dump(exclude_none=True))['data']).replace(":::", "")
            global flag
            await call.message.answer(
                text=f'<blockquote><b><i>Введите новое название подраздела\nНазвание раздела может содержать в себе не '
                     'более 4080 символов. Кавычки доступны для ввода'
                     'в только формате « » .</i></b></blockquote>', parse_mode="HTML")
            await state.set_state(Reg_update_problem2.problem)
            flag = True
            await call.answer()

            @router_two.message(Reg_update_problem2.problem)
            async def plus(message: Message):
                global decision, flag
                decision.clear()
                if flag is False:
                    return await state.clear()
                if flag is True:
                    print((list(message)[22][1]))
                    if list(message)[19][1] is not None:
                        await state.update_data(problem=message.text.lower())
                        await message.answer(f'<blockquote><b><i>Введите решение</i></b></blockquote>', parse_mode="HTML")
                        await state.set_state(Reg_update_problem2.decision)

                        @router_two.message(Reg_update_problem2.decision)
                        async def lu(message: Message, state: FSMContext):
                            global flag
                            global decision
                            name = name_table_from_value_keys_level2[0][1:]
                            await state.update_data(name=name)
                            await message.answer(f'<blockquote><b><i>Введите решение</i></b></blockquote>', parse_mode="HTML")
                            if flag is True:
                                if list(message)[19][1] is  not None:
                                    if message.text != "/end":
                                        decision.append("textt"+message.text)
                                        await state.update_data(decision=decision)
                                        await state.set_state(Reg_update_problem2.decision)
                                    if message.text == '/end':
                                        data = await state.get_data()
                                        update_Decision_Problem(data['decision'], data["name"], idd, data["problem"])
                                        await message.answer(f'<blockquote><b><i>Данные изменены</i></b></blockquote>', parse_mode="HTML")
                                        await call.message.answer(
                                            f'<blockquote><b><i>{call.message.text}</i></b></blockquote>',
                                            parse_mode="HTML",
                                            reply_markup=KeyBouard_level2(
                                                (call.message.text.lower().replace("рaздел:  ", ""))[0:35] + "\'"))
                                        await state.clear()
                                        flag = False
                                        await state.clear()
                                        await state.clear()
                                        await state.clear()
                                        await state.clear()
                                if list(message)[25][1] is not None:
                                    if flag is True:
                                        await message.answer(f'<blockquote><b><i>Фотo</i></b></blockquote>', parse_mode="HTML")
                                        file_id = f'id={message.photo[-1].file_id}'
                                        decision.append(file_id)
                                        await state.update_data(decision=decision)
                                        await state.set_state(Reg_update_problem2.decision)
                                if list(message)[24][1] is not None and list(message)[22][1] is None:
                                    if flag is True:
                                        await message.answer(f'<blockquote><b><i>Документ</i></b></blockquote>', parse_mode="HTML")
                                        file_id = f'document={message.document.file_id}'
                                        decision.append(file_id)
                                        # print("Document")
                                        await state.update_data(decision=decision)
                                        await state.set_state(Reg_update_problem2.decision)
                                if list(message)[22][1] is not None or list(message)[28][1] is not None:
                                    if flag is True:
                                        await message.answer(f'<blockquote><b><i>Видео</i></b></blockquote>',
                                                             parse_mode="HTML")
                                        if list(message)[28][1] is not None:
                                            if len(decision) == 0:
                                                file_id = f' video={message.video.file_id}'
                                                decision.append(file_id)
                                            else:
                                                file_id = f'video={message.video.file_id}'
                                                decision.append(file_id)
                                            await state.update_data(decision=decision)
                                            await state.set_state(Reg_update_problem2.decision)
                                        if list(message)[28][1] is None:
                                            if len(decision) == 0:
                                                file_id = f' video={message.animation.file_id}'
                                                decision.append(file_id)
                                            else:
                                                file_id = f'video={message.animation.file_id}'
                                                decision.append(file_id)
                                            await state.update_data(decision=decision)
                                            await state.set_state(Reg_update_problem2.decision)
                                if list(message)[22][1] is None and list(message)[25][1] is None and list(message)[24][1] is None and list(message)[19][1] is None and list(message)[28][1] is None:
                                    await message.answer(f'<blockquote><b><i>Не верный формат данных \nПоддерживаются только текст, видео, картинки или файлы</i></b></blockquote>', parse_mode="HTML")
                                    await state.set_state(Reg_update_problem2.decision)
                    else:
                        await message.answer(f'<blockquote><b><i>Не поддерживается данный формат, введите текст</i></b></blockquote>', parse_mode="HTML")

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data == 'down')
async def down(call: CallbackQuery):
    global a
    # print(a)
    await call.answer()
    await call.message.edit_text(text=f'\n<blockquote>'
                                      f'<b>'
                                      f'<i>'
                                      f'Все доступные проблемы представлены ниже.'
                                      f'\nКОРНЕВЫЕ ПРОБЛЕМЫ:'
                                      f'</i>'
                                      f'</b>'
                                      f'</blockquote>', parse_mode="HTML", reply_markup=KeyBouard())


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data == 'plus')
async def catalog6(call: CallbackQuery, state: FSMContext):
    global flag_1board
    await call.message.answer(text=f'<blockquote><b><i>Введите название нового раздела\nНазвание раздела может содержать в себе не '
                                           'более 4080 символов. Символ "*", "\\" не воспринимается. Кавычки доступны для ввода'
                                           'в только формате « » .</i></b></blockquote>', parse_mode="HTML")
    await state.set_state(Reg_update_problem1.problem)
    flag_1board = True
    if flag_1board is False:
        await state.clear()
    await call.answer()

    @router_two.message(Reg_update_problem1.problem)
    async def plus(message: Message):
        global flag_1board
        con = sqlite3.connect("Data_Base/Now_bot.db")
        cur = con.cursor()
        proverka_name = cur.execute(f"SELECT Problem FROM DB").fetchall()
        con.close()
        if len(message.text) <= 4080 and flag_1board is True:
            user_message = message.text.lower().replace(",", "").replace("*", "").replace("' ", "").replace("[\" \'", "['''").replace("\\", "")
            await state.update_data(problem=user_message)
            data = await state.get_data()
            numb = (data['problem'],)
            if numb in proverka_name:
                await call.message.answer(f'<blockquote><b><i>Не может быть 2-а одинаковых раздела, попробуйте снова'
                                          f'</i></b></blockquote>', parse_mode="HTML")
                await state.clear()
                flag_1board = False
            else:
                create_string(str(data['problem']), '0', "DB")
                await message.answer('Данные занесены')
                await call.message.edit_text(text=f'\n<blockquote>'
                                                  f'<b>'
                                                  f'<i>'
                                                  f'Все доступные проблемы представлены ниже.'
                                                  f'\nКОРНЕВЫЕ ПРОБЛЕМЫ:'
                                                  f'</i>'
                                                  f'</b>'
                                                  f'</blockquote>', parse_mode="HTML", reply_markup=KeyBouard())
                flag_1board = False
                await state.clear()
        else:
            await message.answer(f'<blockquote><b><i>Длина сообщения может быть не более 4080 символов'
                                 f'.\nВ вашем содержится {len(message.text)} символов.</i></b></blockquote>', parse_mode="HTML")
            await state.clear()


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


@router_two.callback_query(F.data == '7878787878787878')
async def catalog6(call: CallbackQuery, state: FSMContext):
    global flag
    await call.message.answer(text=f'<blockquote><b><i>Введите название нового ПОДраздела\nНазвание раздела может содержать в себе не '
                                           'более 4080 символов. Символ "*" не воспринимается. Кавычки доступны для ввода'
                                           'в только формате « » .</i></b></blockquote>', parse_mode="HTML")
    await state.set_state(Reg_update_problem.problem)
    flag = True
    await call.answer()

    @router_two.message(Reg_update_problem.problem)
    async def plus(message: Message):
        global decision, flag
        decision.clear()
        if flag is False:
            return await state.clear()
        if flag is True:
            if list(message)[19][1] is not None:
                await state.update_data(problem=message.text.lower())
                await message.answer(f'<blockquote><b><i>Введите решение</i></b></blockquote>', parse_mode="HTML")
                await state.set_state(Reg_update_problem.decision)

                @router_two.message(Reg_update_problem.decision)
                async def lu(message: Message, state: FSMContext):
                    global flag
                    global decision
                    name = name_table_from_value_keys_level2[0][1:]
                    await state.update_data(name=name)
                    await message.answer(f'<blockquote><b><i>Введите решение</i></b></blockquote>', parse_mode="HTML")
                    if flag is True:
                        print(list(message)[::])
                        if list(message)[19][1] is  not None:
                            if message.text != "/end":
                                decision.append("textt"+message.text)
                                await state.update_data(decision=decision)
                                await state.set_state(Reg_update_problem.decision)
                            if message.text == '/end':
                                data = await state.get_data()
                                create_string(str(data['problem']), data["decision"], data['name'])
                                await message.answer(f'<blockquote><b><i>Данные изменены</i></b></blockquote>', parse_mode="HTML")
                                await call.message.answer(
                                    f'<blockquote><b><i>{call.message.text}</i></b></blockquote>',
                                    parse_mode="HTML",
                                    reply_markup=KeyBouard_level2(
                                        (call.message.text.lower().replace("рaздел:  ", ""))[0:35] + "\'"))
                                await state.clear()
                                flag = False
                                await state.clear()
                                await state.clear()
                                await state.clear()
                                await state.clear()
                        if list(message)[25][1] is not None:
                            if flag is True:
                                await message.answer(f'<blockquote><b><i>Фотo</i></b></blockquote>', parse_mode="HTML")
                                file_id = f'id={message.photo[-1].file_id}'
                                decision.append(file_id)
                                await state.update_data(decision=decision)
                                await state.set_state(Reg_update_problem.decision)
                        if list(message)[24][1] is not None and list(message)[22][1] is None:
                            if flag is True:
                                await message.answer(f'<blockquote><b><i>Документ</i></b></blockquote>', parse_mode="HTML")
                                file_id = f'document={message.document.file_id}'
                                decision.append(file_id)
                                # print("Document")
                                await state.update_data(decision=decision)
                                await state.set_state(Reg_update_problem.decision)
                        if list(message)[22][1] is not None or list(message)[28][1] is not None:
                            if flag is True:
                                await message.answer(f'<blockquote><b><i>Видео</i></b></blockquote>', parse_mode="HTML")
                                if list(message)[28][1] is not None:
                                    if len(decision) == 0:
                                        file_id = f' video={message.video.file_id}'
                                        decision.append(file_id)
                                    else:
                                        file_id = f'video={message.video.file_id}'
                                        decision.append(file_id)
                                    await state.update_data(decision=decision)
                                    await state.set_state(Reg_update_problem.decision)
                                if list(message)[28][1] is None:
                                    if len(decision) == 0:
                                        file_id = f' video={message.animation.file_id}'
                                        decision.append(file_id)
                                    else:
                                        file_id = f'video={message.animation.file_id}'
                                        decision.append(file_id)
                                    await state.update_data(decision=decision)
                                    await state.set_state(Reg_update_problem.decision)
                        if list(message)[22][1] is None and list(message)[25][1] is None and list(message)[24][1] is None and list(message)[19][1] is None and list(message)[28][1] is None:
                            await message.answer(f'<blockquote><b><i>Не верный формат данных \nПоддерживаются только текст, видео, картинки или файлы</i></b></blockquote>', parse_mode="HTML")
                            await state.set_state(Reg_update_problem.decision)

            else:
                await message.answer(f'<blockquote><b><i>Не поддерживается данный формат, введите текст</i></b></blockquote>', parse_mode="HTML")


