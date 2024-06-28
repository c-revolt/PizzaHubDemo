from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О Нас'),
        ],
        [
            KeyboardButton(text='Способы Оплаты'),
            KeyboardButton(text='Варианты доставки')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите нужное...'
)

del_kb = ReplyKeyboardRemove()

main_kb = ReplyKeyboardBuilder()
main_kb.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='О Нас'),
    KeyboardButton(text='Способы Оплаты'),
    KeyboardButton(text='Варианты доставки')
)
main_kb.adjust(2, 2)

keyboards_builder = ReplyKeyboardBuilder()
keyboards_builder.attach(main_kb)
keyboards_builder.row(KeyboardButton(text='Оставить отзыва'))

request_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text='Отправить номер', request_contact=True),
            KeyboardButton(text='Отправить локацию', request_location=True)
        ]
    ]
)