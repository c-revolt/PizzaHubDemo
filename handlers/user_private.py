from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.message):
    await message.answer('Привеееет!')


@user_private_router.message((F.text.lower().contains('продукты')) | (F.text.lower() == 'меню'))
@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.message):
    await message.answer('Вот наше меню:')


@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.message):
    await message.answer('О нашей пиццерии:')


@user_private_router.message((F.text.lower().contains('оплат')) | (F.text.lower() == 'способы оплаты'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.message):
    await message.answer('Способы оплаты:')


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.message):
    await message.answer('Варианты доставки:')