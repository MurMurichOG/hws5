from aiogram import Router, types, F
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш адрес", callback_data="address"),
                types.InlineKeyboardButton(text="Наши контакты", callback_data="contacts"),
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Магазин", callback_data="shop")
            ]
        ]
    )
    await message.answer(f"""Привет, {message.from_user.full_name}. Мы - книжный магазин. У нас ты найдешь много интересных произведений! """, reply_markup=kb)


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("""Ассортимент предлагаемой магазинами литературы удовлетворит любые вкусы и потребности любителей книги. 
    Постоянным ассортиментом магазина являются культурно-исторические издания, фотоальбомы о природе, истории и этнографии Кыргызстана, а также туристские карты и открытки с видами красивейших мест Кыргызстана. 
    Кроме розничной книжной торговли Фирма выполняет заказы организаций и учебных заведений по комплектованию своих библиотек.""")

@start_router.callback_query(F.data == "address")
async def address(callback: types.CallbackQuery):
    await callback.message.answer("""Площадь Ала-Тоо,
    ТЦ Детский Мир,
    пр. Чуй 271,
    ТЦ Гум Чынар,
    ТРЦ Азия Молл""")

@start_router.callback_query(F.data == "contacts")
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer("""0(312)66-45-24,
    0(312)43-17-90,
    0(312)34-19-78,
    0(312)88-24-45,
    0(312)97-55-42""")


@start_router.callback_query(F.data == "Книги")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("""Книга развивает образность мышления, творческое воображение, обогащает словарный запас и даже предостерегает от ошибок, описывая прошлое и указывая на ошибки. 
    Чтение – это своеобразный диалог с нашим прошлым. 
    Литература, как один из видов искусства, неотъемлемая часть жизни человека.""")



@start_router.callback_query(F.data == "comics")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("""Комикс — издание, в котором история рассказывается с помощью рисунков и сопровождающего их текста и находится на стыке литературы и изобразительного искусства. 
    Комикс — общее название для всех рассказов в картинках, где сюжет рассказывается преимущественно с помощью иллюстраций, а не текста.""")

@start_router.callback_query(F.data == "manga")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("""Манга — японские комиксы со своей уникальной манерой рисования и сюжетами, превратившиеся в самостоятельную культуру. 
    Манга, как и другие комиксы, рассказывает историю с помощью рисунков и текста.""")