from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboards.reply import keyboards_builder, del_kb

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привеееет!', reply_markup=keyboards_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Что вас интересует?'))


@user_private_router.message((F.text.lower().contains('продукты')) | (F.text.lower() == 'меню'))
@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Вот наше меню:', reply_markup=del_kb)


@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('О нашей пиццерии:')


@user_private_router.message((F.text.lower().contains('оплат')) | (F.text.lower() == 'способы оплаты'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold("Способы оплаты:"),
        "Картой в боте",
        "При получении карта/кэш",
        "В заведении",
        marker='✅ '
    )

    await message.answer(text.as_html())


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовынос (сейчас прибегу заберу)",
            "Покушаю у Вас (сейчас прибегу)",
            marker='✅ '
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Почта",
            "Голуби",
            marker='❌ '
        ),
        sep='\n----------------------\n'
    )
    await message.answer(text.as_html())


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f'номер получен')
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f'локация получена')
    await message.answer(str(message.location))
