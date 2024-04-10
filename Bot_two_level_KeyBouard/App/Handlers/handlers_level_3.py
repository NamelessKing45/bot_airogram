from aiogram import Router
from aiogram.types import Message
router_three = Router()


@router_three.message()
async def mess(message: Message):
    await message.delete()
    pass





