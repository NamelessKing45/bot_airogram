import sqlite3
from aiogram.types import CallbackQuery
import json
'''------------------------------------------------------------------------------------------------------------------'''


def create_string(problem: str, decision: str, name_table: str):
    if decision != '0':
        con = sqlite3.connect("Data_Base/Now_bot.db")
        cur = con.cursor()
        problem = str(problem).replace("\'", "").replace("\"", "").replace("[", "").replace("]", "")
        decision = str(decision).replace("\'", "").replace("\"", "").replace("[", "").replace("]", "")
        name_table = name_table.replace(" .", "").replace("\'", "")
        cur.execute(f"INSERT INTO '{name_table}' VALUES('{problem}', '{decision}', '.')")
        con.commit()
        con.close()
    if decision == '0':
        con = sqlite3.connect("Data_Base/Now_bot.db")
        cur = con.cursor()
        problem = problem.replace("\"", "").replace("\'", "").replace("*", "").replace(",", "")
        if len(problem) <= 34:
            cur.execute(f'INSERT INTO {name_table} VALUES("{str(problem)}", "nan", ".")')
        if len(problem) > 34:
            cur.execute(f'INSERT INTO {name_table} VALUES("{str(problem)[0:34]}", "nan", "{str(problem)[34:]}")')
        cur.execute(f"CREATE TABLE '{problem[0:34]}' ('Problem'	TEXT, 'Decision' TEXT, Pod_problem)")
        con.commit()
        con.close()
    else:
        pass


'''------------------------------------------------------------------------------------------------------------------'''


def update_Problem(id: str, name_table: str, new_problem: str, name_tables: str, new_name_table: str):
    if name_table != "0":
        if len(new_problem) <= 34:
            con = sqlite3.connect("Data_Base/Now_bot.db")
            cur = con.cursor()
            new_problem = new_problem.replace("\"", "").replace("\'", "").replace("*", "")
            new_name_table = new_name_table.replace("\"", "").replace("\'", "").replace("*", "")
            cur.execute(f'UPDATE {name_table} SET Problem = "{new_problem}" WHERE ROWID = {id}')
            cur.execute(f'UPDATE {name_table} SET Pod_problem = "." WHERE ROWID = {id}')
            if name_tables != '0' and new_name_table != '0':
                cur.execute(f"ALTER TABLE '{name_tables}' RENAME TO '{new_name_table}'")
            con.commit()
            con.close()
        if len(new_problem) > 34:
                con = sqlite3.connect("Data_Base/Now_bot.db")
                cur = con.cursor()
                new_problem = new_problem.replace("\"", "").replace("\'", "").replace("*", "")
                new_name_table = new_name_table.replace("\"", "").replace("\'", "").replace("*", "")
                nath = new_problem[0:35]+"\'"
                end = new_problem[35:]
                cur.execute(f'UPDATE {name_table} SET Problem = "{nath}" WHERE ROWID = {id}')
                cur.execute(f'UPDATE {end} SET Pod_problem = "." WHERE ROWID = {id}')
                if name_tables != '0' and new_name_table != '0':
                    cur.execute(f"ALTER TABLE '{name_tables}' RENAME TO {new_problem}")
                con.commit()
                con.close()
    if name_table == "0" and  new_problem == '0':
        con = sqlite3.connect("Data_Base/Now_bot.db")
        cur = con.cursor()
        new_name_table = new_name_table.replace("\"", "").replace("\'", "").replace("*", "")
        cur.execute(f'UPDATE {new_name_table} SET Problem = "{name_tables}" WHERE ROWID = {id}')


'''------------------------------------------------------------------------------------------------------------------'''


def update_Decision_Problem(new_decision: str, name_table: str, id: str, new_problem: str):
    con = sqlite3.connect("Data_Base/Now_bot.db")
    cur = con.cursor()
    new_decision = str(new_decision).replace("[", "").replace("]", "").replace("\'", "")
    print(f"UPDATE '{name_table} SET Decision = '{new_decision}' WHERE rowid = {id}")
    print(f"UPDATE '{name_table} SET Decision = '{new_problem}' WHERE rowid = {id}")
    cur.execute(f"UPDATE '{name_table} SET Decision = '{new_decision}' WHERE rowid = {id}")
    cur.execute(f"UPDATE '{name_table} SET Problem = '{new_problem}' WHERE rowid = {id}")
    cur.execute('')
    con.commit()
    con.close()


'''------------------------------------------------------------------------------------------------------------------'''


def value_keys(values_keys: str):
    con = sqlite3.connect("Data_Base/Now_bot.db")
    cur = con.cursor()
    save_problem = []
    cur.execute("SELECT Problem, Decision FROM DB")
    alla = cur.fetchall()
    for i in alla:
        save_problem.append(i[::])
    save_problem = dict(save_problem)
    keys = list(save_problem.keys())
    values = list(save_problem.values())
    if values_keys == 'key':
        con.commit()
        con.close()
        return keys
    if values_keys == 'values':
        con.commit()
        con.close()
        return values
    if values_keys == 'values_keys':
        con.commit()
        con.close()
        save_problem = []
        con = sqlite3.connect("Data_Base/Now_bot.db")
        cur = con.cursor()
        cur.execute("SELECT rowid, Problem, Decision, Pod_problem FROM DB")
        alla1 = cur.fetchall()
        for i in alla1:
            save_problem.append(i[::])
        save_problem = list(save_problem)
        con.commit()
        con.close()
        return save_problem


'''------------------------------------------------------------------------------------------------------------------'''


def delete(id, name_table: str, two_level_table: str):
    if name_table == '0':
        con = sqlite3.connect("Data_Base/Now_bot.db")
        cur = con.cursor()
        two_level_table = two_level_table.replace('раздел: ', '').replace("\"", "").replace("\'", "")
        id = str(id).replace(':::', '')
        two_level_table = str(two_level_table).replace(' .', '')
        cur.execute(f"DELETE FROM '{two_level_table}' WHERE rowid = {id}")
        a = [i for i in cur.execute(f"SELECT Problem, Decision, Pod_problem FROM '{str(two_level_table)}'")]     # ПРЕЗАПИСЬ ТАБЛИЦЫ!!!
        cur.execute(f"DROP TABLE '{two_level_table}'")                                   # ПРЕЗАПИСЬ ТАБЛИЦЫ!!
        cur.execute(f"CREATE TABLE '{two_level_table}' ('Problem'	TEXT, 'Decision', 'Pod_problem' TEXT)")# ПРЕЗАПИСЬ ТАБЛИЦЫ!!
        for i in a:                                                      # ПРЕЗ"АПИСЬ ТАБЛИЦЫ!!
            cur.execute(f"INSERT INTO '{str(two_level_table)}' VALUES('{i[0]}', '{i[1]}', '{i[2]}')")            # ПРЕЗАПИСЬ ТАБЛИЦЫ!!
        con.commit()
        con.close()
    if name_table != '0':
        con = sqlite3.connect("Data_Base/Now_bot.db")
        cur = con.cursor()
        cur.execute(f'DELETE FROM DB WHERE rowid = {id}')
        cur.execute(f"DROP TABLE {name_table} ")
        a = [i for i in cur.execute('SELECT Problem, Decision, Pod_problem FROM DB')]     # ПРЕЗАПИСЬ ТАБЛИЦЫ!!!
        cur.execute(f"DROP TABLE DB")                                   # ПРЕЗАПИСЬ ТАБЛИЦЫ!!
        cur.execute('CREATE TABLE "DB" ("Problem"	TEXT, "Decision", Pod_problem	TEXT)')# ПРЕЗАПИСЬ ТАБЛИЦЫ!!
        for i in a:                                                      # ПРЕЗАПИСЬ ТАБЛИЦЫ!!
            cur.execute(f'INSERT INTO DB VALUES("{i[0]}", "{i[1]}", "{i[2]}")')            # ПРЕЗАПИСЬ ТАБЛИЦЫ!!
        con.commit()
        con.close()


'''------------------------------------------------------------------------------------------------------------------'''
name_table_from_value_keys_level2 = []


def value_keys_level2(name_table: str):
    global name_table_from_value_keys_level2
    name_table_from_value_keys_level2.clear()
    con = sqlite3.connect("Data_Base/Now_bot.db")
    con.commit()
    con.close()
    save_problem = []
    con = sqlite3.connect("Data_Base/Now_bot.db")
    cur = con.cursor()
    name_table = name_table.replace(" .'", "")
    name_table_from_value_keys_level2.append(name_table)
    print(name_table, "Name table")
    cur.execute(f"SELECT rowid, Problem, Decision, Pod_problem FROM {name_table}")
    alla1 = cur.fetchall()
    for i in alla1:
        save_problem.append(i[::])
    save_problem = list(save_problem)
    con.commit()
    con.close()
    return save_problem


'''------------------------------------------------------------------------------------------------------------------'''


def user_id(call: CallbackQuery):
    save_id = str(call.from_user.id)
    save_user_name = str(call.from_user.username)
    success = f"('{save_id}', ['{save_user_name}'])"
    with open('Id_Name_admin_users/ID_True.json', 'r') as f_id:
        f_id = f_id.read()
    for i in dict.items(json.loads(f_id)):
        if str(i) == success:
            return 1


'''------------------------------------------------------------------------------------------------------------------'''
