from aiogram import F, types, Router
from aiogram.filters import Command

shop_router = Router()

@shop_router.message(Command("shop"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Книги"),
                types.KeyboardButton(text="Комиксы"),
                types.KeyboardButton(text="Манга")
            ]
        ]
    )
    await message.answer("Выберите категорию", reply_markup=kb)

@shop_router.message(F.text == "Книги")
async def books(message: types.Message):
    await message.answer("""Книга развивает образность мышления, творческое воображение, обогащает словарный запас и даже предостерегает от ошибок, описывая прошлое и указывая на ошибки. 
    Чтение – это своеобразный диалог с нашим прошлым. 
    Литература, как один из видов искусства, неотъемлемая часть жизни человека.""")



@shop_router.message(F.text == "Комиксы")
async def comics(message: types.Message):
    await message.answer("""Комикс — издание, в котором история рассказывается с помощью рисунков и сопровождающего их текста и находится на стыке литературы и изобразительного искусства. 
    Комикс — общее название для всех рассказов в картинках, где сюжет рассказывается преимущественно с помощью иллюстраций, а не текста.""")

@shop_router.message(F.text == "Манга")
async def manga(message: types.Message):
    await message.answer("""Манга — японские комиксы со своей уникальной манерой рисования и сюжетами, превратившиеся в самостоятельную культуру. 
    Манга, как и другие комиксы, рассказывает историю с помощью рисунков и текста.""")