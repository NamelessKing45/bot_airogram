from aiogram.fsm.state import State, StatesGroup
'''------------------------------------------------------------------------------------------------------------------'''


class Reg_update_problem(StatesGroup):
    problem = State()
    id = State()
    decision = State()


'''------------------------------------------------------------------------------------------------------------------'''


class Reg_update_problem2(StatesGroup):
    problem = State()
    id = State()
    decision = State()


'''------------------------------------------------------------------------------------------------------------------'''


class Reg_update_problem1(StatesGroup):
    problem = State()
    id = State()
    decision = State()


'''------------------------------------------------------------------------------------------------------------------'''


class Reg_update_decision(StatesGroup):
    problem = State()
    id = State()
    decision = State()


'''------------------------------------------------------------------------------------------------------------------'''


class Reg_input_problem_decision(StatesGroup):
    problem = State()
    id = State()
    decision = State()


'''------------------------------------------------------------------------------------------------------------------'''


class Reg_delete(StatesGroup):
    problem = State()
    id = State()
    decision = State()


'''------------------------------------------------------------------------------------------------------------------'''


class Reg_name_table(StatesGroup):
    problem = State()
    id = State()
    decision = State()


'''------------------------------------------------------------------------------------------------------------------'''

